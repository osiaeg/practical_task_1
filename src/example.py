from google.protobuf.message import DecodeError

from message import *

if __name__ == '__main__':
    messages = [
        fast_response('127498127489127498124'),
        slow_response(100),
        request_for_fast_response(),
        request_for_slow_response(1000),
    ]

    with open('out.bin', 'wb') as f:
        buff = b''
        for message in messages:
            head_size = encode_varint(message)
            package = head_size + message.SerializeToString()
            buff += package
        f.write(buff[:-1])

    with open('out.bin', 'rb') as f:
        buf = f.read()
        n = 0
        while n < len(buf):
            msg_size, new_pos = decode_varint(buf, n)
            msg_buf = buf[new_pos:new_pos + msg_size]
            msg = wm.WrapperMessage()
            try:
                msg.ParseFromString(msg_buf)
            except DecodeError:
                break
            print(msg)
            n = new_pos + msg_size
