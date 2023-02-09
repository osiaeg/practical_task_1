"""
Final version of asyncio socket server.
Using standard high-level API with streams.
"""

import asyncio
from datetime import datetime
from loguru import logger

from config import HOST, PORT
from message import *

users = []
# logger.add("file_{time}.log")


async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    logger.info(f"Connected by {addr}")
    users.append((reader, writer))
    while True:
        # Receive
        try:
            buf = await reader.read(1024)  # New
        except ConnectionError:
            logger.info(f"Client suddenly closed while receiving from {addr}")
            break
        msg = get_message_from_buff(buf)

        logger.info(f"\nReceived:\n{msg}from: {addr}")

        if msg.HasField('request_for_fast_response'):
            now = datetime.now()
            response = fast_response(now.strftime("%Y%m%dT%H%M%S.%f")[:-3])
        elif msg.HasField('request_for_slow_response'):
            milliseconds = msg.request_for_slow_response.time_in_seconds_to_sleep
            await asyncio.sleep(milliseconds / 1000)
            response = slow_response(len(users))

        try:
            package = encode_varint(response) + response.SerializeToString()
            writer.write(package)  # New
            await writer.drain()
        except ConnectionError:
            logger.info(f"Client suddenly closed, cannot send")
            break

    users.remove((reader, writer))
    writer.close()
    logger.info(f"Disconnected by {addr}")


async def main(host, port):
    server = await asyncio.start_server(handle_connection, host, port)
    logger.info(f"Start server on ({host}:{port})")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))
