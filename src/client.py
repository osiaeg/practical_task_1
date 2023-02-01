from message import *

if __name__ == '__main__':
    with open('out.bin', 'wb') as f:
        first_message = fast_response('127498127489127498124')
        f.write(encode_varint(first_message))
        f.write(first_message.SerializeToString())

        second_message = slow_response(100)
        f.write(encode_varint(second_message))
        f.write(second_message.SerializeToString())

        third_message = request_for_fast_response()
        f.write(encode_varint(third_message))
        f.write(third_message.SerializeToString())


    with open('out.bin', 'rb') as f:
        buf = f.read()
        n = 0
        while n < len(buf):
            msg_size, new_pos = decode_varint(buf, n)
            msg_buf = buf[new_pos:new_pos + msg_size]
            msg = wm.WrapperMessage()
            msg.ParseFromString(msg_buf)
            print(msg)
            n = new_pos + msg_size
