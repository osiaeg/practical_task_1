from .helpers import *
from .DelimitedMessagesStreamParser import DelimitedMessagesStreamParser
from protobuf.message_pb2 import *
from .messages import Messages

parser = DelimitedMessagesStreamParser(WrapperMessage)

message_list = [
        Messages.fast_response("alskdjf"),
        Messages.slow_response(20),
        Messages.request_for_fast_response(),
        Messages.request_for_slow_response(1000),
        ]

print("Show test messages.")

for message in message_list:
    print(message)

print("Show serialized stream with messages above.")

for message in message_list:
    serialized_message = serialize_delimited(message)
    print(serialized_message)

buffer = b''.join([serialize_delimited(message) for message in message_list])
print(buffer)


