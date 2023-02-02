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
logger.add("file_{time}.log")


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
        logger.info(f"Received {data} from: {addr}")
        msg_size, new_pos = decode_varint(data, 0)
        msg_buf = buf[new_pos:new_pos + msg_size]
        msg = wm.WrapperMessage()
        msg.ParseFromString(msg_buf)
        logger.info(f"Received {msg} from: {addr}")


        if not data:
            break
        # Process
        if data == b"close":
            break
        elif data == b'fast':
            data = f"{datetime.now()}".encode()
        elif data == b'slow':
            await asyncio.sleep(30)
            data = f'{len(users)}'.encode()
        else:
            data = data.upper()
        # Send
        logger.info(f"Send: {data} to: {addr}")
        try:
            writer.write(data)  # New
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
