# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import usertaste_pb2 as usertaste__pb2


class UserTasteStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.init = channel.unary_unary(
                '/usertaste.UserTaste/init',
                request_serializer=usertaste__pb2.User.SerializeToString,
                response_deserializer=usertaste__pb2.Stat.FromString,
                )
        self.greet = channel.unary_unary(
                '/usertaste.UserTaste/greet',
                request_serializer=usertaste__pb2.Want.SerializeToString,
                response_deserializer=usertaste__pb2.Stat.FromString,
                )
        self.listfile = channel.unary_stream(
                '/usertaste.UserTaste/listfile',
                request_serializer=usertaste__pb2.Want.SerializeToString,
                response_deserializer=usertaste__pb2.File.FromString,
                )


class UserTasteServicer(object):
    """Missing associated documentation comment in .proto file."""

    def init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def greet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserTasteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'init': grpc.unary_unary_rpc_method_handler(
                    servicer.init,
                    request_deserializer=usertaste__pb2.User.FromString,
                    response_serializer=usertaste__pb2.Stat.SerializeToString,
            ),
            'greet': grpc.unary_unary_rpc_method_handler(
                    servicer.greet,
                    request_deserializer=usertaste__pb2.Want.FromString,
                    response_serializer=usertaste__pb2.Stat.SerializeToString,
            ),
            'listfile': grpc.unary_stream_rpc_method_handler(
                    servicer.listfile,
                    request_deserializer=usertaste__pb2.Want.FromString,
                    response_serializer=usertaste__pb2.File.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'usertaste.UserTaste', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserTaste(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/usertaste.UserTaste/init',
            usertaste__pb2.User.SerializeToString,
            usertaste__pb2.Stat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def greet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/usertaste.UserTaste/greet',
            usertaste__pb2.Want.SerializeToString,
            usertaste__pb2.Stat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/usertaste.UserTaste/listfile',
            usertaste__pb2.Want.SerializeToString,
            usertaste__pb2.File.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
