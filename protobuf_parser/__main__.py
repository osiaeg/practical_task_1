from .helpers import *
from .stream_parser import DelimitedMessagesStreamParser as Parser
import io
import time

messages = io.BytesIO()
parser = Parser()

message_list = [
        fast_response("alskdjf"),
        slow_response(20),
        request_for_fast_response(),
        request_for_slow_response(1000),
        ]
print("Show test messages.")

for message in message_list:
    print(message)

print("Show serialized stream with messages above.")

for message in message_list:
    serialized_message = serialize_delimited(message)
    messages.write(serialized_message)

print(messages.getvalue())

print("Show deserialized messages form stream.")
messages.seek(0)
while messages.tell() < len(messages.getbuffer()):
    parsedMessages = parser.parse(messages.read(1))

for item in parsedMessages:
    print(item)

