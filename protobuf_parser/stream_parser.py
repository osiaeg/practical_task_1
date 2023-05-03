from .helpers import parse_delimited
import io

class DelimitedMessagesStreamParser:
    _m_buffer = io.BytesIO()

    def parse(self, data):
        msg_list = list()
        self._m_buffer.write(data)
        msg = parse_delimited(self._m_buffer, len(self._m_buffer.getbuffer()))

        if msg:
            self._m_buffer.close()
            self._m_buffer = io.BytesIO()
            msg_list.append(msg)

        return msg_list

