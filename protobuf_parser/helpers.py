from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.message import DecodeError, Message
from typing import Any, Optional
import io


def encode_varint(msg: Any) -> bytes:
    return _VarintBytes(msg.ByteSize())


def decode_varint(buf: bytes, pos: int) -> tuple[int, int]:
    msg_size, new_pos = _DecodeVarint32(buf, pos)
    return msg_size, new_pos


def serialize_delimited(msg):
    return encode_varint(msg) + msg.SerializeToString()


def parse_delimited(data: Optional[bytes], size: int, protocol):
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

