import logging


import grpc

from modules.message import message_pb2
from modules.service import service_pb2
from modules.service import service_pb2_grpc


def make_message():
    data = {
        "from": "berk",
        "receiver": "ali",
        "message": "Hello World"
    } 
    
    return message_pb2.Message(**data)

def list_of_messages():
    for _ in range(10):
        yield make_message()


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.ChatServiceStub(channel)
        data = {
            "from": "berk",
            "receiver": "ali",
            "message": "Hello World"
        }
        msg = message_pb2.Message(**data)
        response = stub.SendMessage(iter([msg]))
        print(response)

        response = stub.retrieveMessage(service_pb2.Empty())
        print(response)
        breakpoint()


if __name__ == "__main__":
    run()