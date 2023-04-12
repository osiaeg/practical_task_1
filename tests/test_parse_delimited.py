import unittest, io
from protobuf_parser import *

class TestParseDelimited(unittest.TestCase):

    def test_slow_response(self):
        response = slow_response(100)
        buffer = io.BytesIO(serialize_delimited(response))
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()))
        self.assertEqual(response, parsed_msg)


    def test_fast_response(self):
        response = fast_response("alksdjf")
        buffer = io.BytesIO(serialize_delimited(response))
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()))
        self.assertEqual(response, parsed_msg)


    def test_request_for_fast_response(self):
        response = request_for_fast_response()
        buffer = io.BytesIO(serialize_delimited(response))
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()))
        self.assertEqual(response, parsed_msg)


    def test_request_for_slow_response(self):
        response = request_for_slow_response(1000)
        buffer = io.BytesIO(serialize_delimited(response))
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()))
        self.assertEqual(response, parsed_msg)


    def test_none_answer(self):
        response = request_for_slow_response(1000)
        buffer = io.BytesIO(serialize_delimited(response)[:-2])
        parsed_msg = parse_delimited(buffer, len(buffer.getbuffer()))
        self.assertEqual(parsed_msg, None)

