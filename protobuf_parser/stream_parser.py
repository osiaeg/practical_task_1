from .helpers import parse_delimited
import io

class DelimitedMessagesStreamParser:
    _m_buffer = io.BytesIO()

    def __init__(self, protocol):
        self.protocol = protocol

    def parse(self, data):
        msg_list = list()
        for byte in data:
            self._m_buffer.write(data)
            msg = parse_delimited(self._m_buffer, len(self._m_buffer.getbuffer()), self.protocol)

            if msg:
                self._m_buffer.close()
                self._m_buffer = io.BytesIO()
                msg_list.append(msg)

        return msg_list

