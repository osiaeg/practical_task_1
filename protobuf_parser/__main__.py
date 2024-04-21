from .DelimitedMessagesStreamParser import DelimitedMessagesStreamParser
from protobuf.message_pb2 import *

parser = DelimitedMessagesStreamParser(WrapperMessage)

message_list = [
    WrapperMessage(request_for_fast_response=RequestForFastResponse()),
    WrapperMessage(fast_response=FastResponse(current_date_time="aksdjfasdf")),
    WrapperMessage(request_for_slow_response=RequestForSlowResponse(time_in_seconds_to_sleep=0)),
    WrapperMessage(slow_response=SlowResponse(connected_client_count=0)),
]

print("Show test messages.")

for message in message_list:
    print(message)

print("Show serialized stream with messages above.")
