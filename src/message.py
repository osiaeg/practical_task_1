import wrappermessage_pb2 as wm
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes

def encode_varint(msg: wm.WrapperMessage) -> bytes:
    return _VarintBytes(msg.ByteSize())

def decode_varint(buf: bytes, pos: int) -> tuple[int, int]:
    msg_size, new_pos = _DecodeVarint32(buf, pos)
    return msg_size, new_pos

def fast_response(date: str) -> wm.WrapperMessage :
    return wm.WrapperMessage(**{
        'fast_response': wm.FastResponse(**{
            'current_date_time': date
            })
        })

def slow_response(client_count: int) -> wm.WrapperMessage :
    return wm.WrapperMessage(**{
        'slow_response': wm.SlowResponse(**{
            'connected_client_count': client_count
            })
        })

def request_for_fast_response() -> wm.WrapperMessage :
    return wm.WrapperMessage(**{
        'request_for_fast_response': wm.RequestForFastResponse()
        })

def request_for_slow_response(milliseconds: int) -> wm.WrapperMessage :
    try:
        return wm.WrapperMessage(**{
            'request_for_slow_response': wm.RequestForSlowResponse(**{
                'time_in_seconds_to_sleep': milliseconds
                })
            })
    except ValueError:
        print(f'{milliseconds} out of range uint32')
        return wm.WrapperMessage()

def parseDelimited(data, size, bytesConsumed = 0):
    msg_size, new_pos = decode_varint(buff, 0)
    msg = wm.WrapperMessage()
    msg.ParseFromString(buff[new_pos:new_pos + bytesConsumed])
    return msg

