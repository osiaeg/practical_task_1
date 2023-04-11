from .wrappermessage_pb2 import *
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes


def encode_varint(msg: WrapperMessage) -> bytes:
    return _VarintBytes(msg.ByteSize())


def decode_varint(buf: bytes, pos: int) -> tuple[int, int]:
    msg_size, new_pos = _DecodeVarint32(buf, pos)
    return msg_size, new_pos


def serialize_delimited(msg):
    return b""


def parse_delimited(data: bytes, size: int):
    pass


def fast_response(date: str) -> WrapperMessage :
    return WrapperMessage(**{
        'fast_response': FastResponse(**{
            'current_date_time': date
            })
        })


def slow_response(client_count: int) -> WrapperMessage :
    return WrapperMessage(**{
        'slow_response': SlowResponse(**{
            'connected_client_count': client_count
            })
        })


def request_for_fast_response() -> WrapperMessage :
    return WrapperMessage(**{
        'request_for_fast_response': RequestForFastResponse()
        })


def request_for_slow_response(milliseconds: int) -> WrapperMessage :
    try:
        return WrapperMessage(**{
            'request_for_slow_response': RequestForSlowResponse(**{
                    'time_in_seconds_to_sleep': milliseconds
                })
            })
    except ValueError:
        print(f'{milliseconds} out of range uint32')
        return WrapperMessage()

