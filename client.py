import logging


import grpc

from modules.message import message_pb2
from modules.service import service_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.ChatServiceStub(channel)
        response = stub.SendMessage(message_pb2.Message(receiver="ali", message="hello"))
        print(response)


if __name__ == "__main__":
    run()