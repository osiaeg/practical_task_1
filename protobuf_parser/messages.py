from .wrappermessage_pb2 import *

class Messages:
    @staticmethod
    def fast_response(date: str) -> WrapperMessage :
        return WrapperMessage(**{
            'fast_response': FastResponse(**{
                'current_date_time': date
                })
            })


    @staticmethod
    def slow_response(client_count: int) -> WrapperMessage :
        return WrapperMessage(**{
            'slow_response': SlowResponse(**{
                'connected_client_count': client_count
                })
            })


    @staticmethod
    def request_for_fast_response() -> WrapperMessage :
        return WrapperMessage(**{
            'request_for_fast_response': RequestForFastResponse()
            })


    @staticmethod
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

