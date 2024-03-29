# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import modules.message.message_pb2 as message__pb2
import modules.message_status.message_status_pb2 as message__status__pb2
import modules.service.service_pb2 as service__pb2


class ChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.stream_unary(
                '/ChatService/SendMessage',
                request_serializer=message__pb2.Message.SerializeToString,
                response_deserializer=message__status__pb2.MessageStatus.FromString,
                )
        self.retrieveMessage = channel.unary_stream(
                '/ChatService/retrieveMessage',
                request_serializer=service__pb2.Empty.SerializeToString,
                response_deserializer=message__pb2.Message.FromString,
                )


class ChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def retrieveMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.stream_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=message__pb2.Message.FromString,
                    response_serializer=message__status__pb2.MessageStatus.SerializeToString,
            ),
            'retrieveMessage': grpc.unary_stream_rpc_method_handler(
                    servicer.retrieveMessage,
                    request_deserializer=service__pb2.Empty.FromString,
                    response_serializer=message__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ChatService/SendMessage',
            message__pb2.Message.SerializeToString,
            message__status__pb2.MessageStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def retrieveMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ChatService/retrieveMessage',
            service__pb2.Empty.SerializeToString,
            message__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
