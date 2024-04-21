from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.message import DecodeError, Message
from typing import Any, Optional, TypeVar

M = TypeVar("M", bound=Message)


def encode_varint(msg: M) -> bytes:
    return _VarintBytes(msg.ByteSize())


def decode_varint(buf: bytes, pos: int) -> tuple[int, int]:
    msg_size, new_pos = _DecodeVarint32(buf, pos)
    return msg_size, new_pos


def serialize_delimited(msg: M) -> bytes:
    return encode_varint(msg) + msg.SerializeToString()


def parse_delimited(data: bytes, size: int, protocol) -> Optional[M]:
    message = protocol()
    msg_size, new_pos = decode_varint(data, 0)

    if msg_size != size - new_pos:
        return None

    try:
        message.ParseFromString(data[new_pos: new_pos + msg_size])
    except DecodeError:
        raise ValueError('Corrupt message')

    return message
