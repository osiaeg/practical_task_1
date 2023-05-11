from .wrappermessage_pb2 import *
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.message import DecodeError, Message
from typing import Any
from functools import wraps
import io


def message_type(type_name):
    def _wrapper(f):
        @wraps(f)
        def inner(*args, **kwargs):
            global message
            message = type_name()
            f(*args, **kwargs)
        return inner
    return _wrapper


def encode_varint(msg: Any) -> bytes:
    return _VarintBytes(msg.ByteSize())


def decode_varint(buf: bytes, pos: int) -> tuple[int, int]:
    msg_size, new_pos = _DecodeVarint32(buf, pos)
    return msg_size, new_pos


def serialize_delimited(msg):
    return encode_varint(msg) + msg.SerializeToString()


def parse_delimited(data: io.BytesIO, size: int, protocol):
    if size == 1:
        return None

    message = protocol()
    data_bytes = data.getbuffer()
    msg_size, new_pos = decode_varint(data.getvalue(), 0)

    try:
        message.ParseFromString(data_bytes[new_pos : new_pos + msg_size])
    except DecodeError:
        message = None

    return message


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


