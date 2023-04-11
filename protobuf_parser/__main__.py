from .helpers import *
from .stream_parser import DelimitedMessagesStreamParser as Parser
import io

messages = io.BytesIO()
parser = Parser()

message_list = [
        fast_response("alskdjf"),
        slow_response(20),
        request_for_fast_response(),
        request_for_slow_response(1000),
        ]

for message in message_list:
    messages.write(message.SerializeToString())

print(messages.read())


