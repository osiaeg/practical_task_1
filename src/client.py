"""
Simple socket client for testing servers.

https://docs.python.org/3/library/socket.html#example

Run one of the servers and a few of clients.

All servers are functionally identical, so the client is same for them all.
Only an implementation is different.

For more control, don't enable auto-reconnect, but restart the client on
each disconnection.
"""

import socket
from config import HOST, PORT
from message import *


IS_RECONNECT_ENABLED = False


if __name__ == "__main__":
    is_started = False
    while IS_RECONNECT_ENABLED or not is_started:
        is_started = True
        print("Create client")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            print("Client connected")
            while True:
                # Input
                data = input("-> ")
                if data == "exit":
                    print("Close by client")
                    break
                elif data == 'fast':
                    data_bytes = request_for_fast_response()
                elif 'slow' in data:
                    data = data.replace('slow', '')
                    data_bytes = request_for_slow_response(int(data))
                # Send
                sock.sendall(encode_varint(data_bytes) + data_bytes.SerializeToString())
                # Receive
                data_bytes = sock.recv(1024)
                data = data_bytes.decode()
                print("Received:", repr(data))
                if not data:
                    print("Closed by server")
                    break
            sock.close()
            print("Client disconnected")
