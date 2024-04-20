import unittest, io
from protobuf_parser.messages import Messages
from protobuf_parser.helpers import serialize_delimited, parse_delimited
from protobuf.message_pb2 import *

class TestParseDelimited(unittest.TestCase):

    def test_slow_response(self):
        response = Messages.slow_response(100)
        buffer = io.BytesIO(serialize_delimited(response))
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()), WrapperMessage)
        self.assertEqual(response, parsed_msg)


    def test_fast_response(self):
        response = Messages.fast_response("alksdjf")
        buffer = io.BytesIO(serialize_delimited(response))
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()), WrapperMessage)
        self.assertEqual(response, parsed_msg)


    def test_request_for_fast_response(self):
        response = Messages.request_for_fast_response()
        buffer = io.BytesIO(serialize_delimited(response))
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()), WrapperMessage)
        self.assertEqual(response, parsed_msg)


    def test_request_for_slow_response(self):
        response = Messages.request_for_slow_response(1000)
        buffer = io.BytesIO(serialize_delimited(response))
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()), WrapperMessage)
        self.assertEqual(response, parsed_msg)


    def test_none_answer(self):
        response = Messages.request_for_slow_response(1000)
        buffer = io.BytesIO(serialize_delimited(response)[:-2])
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()), WrapperMessage)
        self.assertEqual(parsed_msg, None)

