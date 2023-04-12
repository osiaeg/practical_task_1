from .helpers import parse_delimited
import io

class DelimitedMessagesStreamParser:
    _m_buffer = io.BytesIO()
    _msg_list = list()

    def parse(self, data):
        self._m_buffer.write(data)
        msg = parse_delimited(self._m_buffer, len(self._m_buffer.getbuffer()))

        if msg:
            self._m_buffer.close()
            self._m_buffer = io.BytesIO()
            self._msg_list.append(msg)

        return self._msg_list

