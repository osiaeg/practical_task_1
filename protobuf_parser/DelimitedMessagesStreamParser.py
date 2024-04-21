from .helpers import parse_delimited
from typing import Optional


class DelimitedMessagesStreamParser:
    _m_buffer = b''

    def __init__(self, protocol):
        self.protocol = protocol

    def parse(self, data: Optional[bytes]):
        msg_list = []

        if data is None:
            return []

        for byte in data:
            bytes_int = byte.to_bytes(1, byteorder="big")
            self._m_buffer += bytes_int
            msg = parse_delimited(self._m_buffer, len(self._m_buffer), self.protocol)

            if msg:
                self._m_buffer = b''
                msg_list.append(msg)

        return msg_list
