import wrappermessage_pb2 as wm
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.message import DecodeError

class DelimitedMessagesStreamParser:
    def parse(self, data) -> list:
        messages = list()

        start = 0

        while start < len(data):
            message_size, pos = decode_varint(data, start)
            msg = wm.WrapperMessage()
            try:
                msg.ParseFromString(data[pos:pos + message_size])
                messages.append(msg)
            except DecodeError:
                print('Decoding faild.')
            start += pos + message_size

        return messages

    def _parseDelimited(self, data, start = 0):
        message_size, pos = decode_varint(data, start)
        msg = wm.WrapperMessage()
        try:
            msg.ParseFromString(data[pos:pos + message_size])
        except DecodeError:
            print('Decoding faild.')
            return None
        return msg


def encode_varint(msg: wm.WrapperMessage) -> bytes:
    return _VarintBytes(msg.ByteSize())


def decode_varint(buf: bytes, pos: int) -> tuple[int, int]:
    msg_size, new_pos = _DecodeVarint32(buf, pos)
    return msg_size, new_pos


def fast_response(date: str) -> wm.WrapperMessage:
    return wm.WrapperMessage(**{
        'fast_response': wm.FastResponse(**{
            'current_date_time': date
        })
    })


def slow_response(client_count: int) -> wm.WrapperMessage:
    return wm.WrapperMessage(**{
        'slow_response': wm.SlowResponse(**{
            'connected_client_count': client_count
        })
    })


def request_for_fast_response() -> wm.WrapperMessage:
    return wm.WrapperMessage(**{
        'request_for_fast_response': wm.RequestForFastResponse()
    })


def request_for_slow_response(milliseconds: int) -> wm.WrapperMessage:
    try:
        return wm.WrapperMessage(**{
            'request_for_slow_response': wm.RequestForSlowResponse(**{
                'time_in_seconds_to_sleep': milliseconds
            })
        })
    except ValueError:
        print(f'{milliseconds} out of range uint32')
        return wm.WrapperMessage()


def get_message_from_buff(buf) -> wm.WrapperMessage:
    msg_size, new_pos = decode_varint(buf, 0)
    msg_buf = buf[new_pos:new_pos + msg_size]
    msg = wm.WrapperMessage()
    msg.ParseFromString(msg_buf)
    return msg

