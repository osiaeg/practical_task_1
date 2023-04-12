import unittest
from protobuf_parser import DelimitedMessagesStreamParser

class TestDelimitedMessagesStreamParser(unittest.TestCase):
     def test_upper(self):
         self.assertEqual('foo'.upper(), 'FOO')
