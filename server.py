import logging
from concurrent import futures


import grpc

from modules.status import status_pb2
from modules.message import message_pb2_grpc
from modules.service import service_pb2_grpc


class Service(service_pb2_grpc.ChatServiceServicer):
    def SendMessage(self, request, context):
        return status_pb2.Status(status=1)


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