import logging
from concurrent import futures

import grpc

from modules.message_status import message_status_pb2
from modules.message import message_pb2
from modules.service import service_pb2, service_pb2_grpc


class Service(service_pb2_grpc.ChatServiceServicer):
    __messages = {}

    def SendMessage(self, request, context):
        return message_status_pb2.MessageStatus(status=1)

    def retrieveMessage(self, *args, **kwargs):
        data = {
            "from": "berk",
            "receiver": "ali",
            "message": "Hello World"
        }
        yield message_pb2.Message(**data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    service_pb2_grpc.add_ChatServiceServicer_to_server(Service(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("The server is running")
    serve()