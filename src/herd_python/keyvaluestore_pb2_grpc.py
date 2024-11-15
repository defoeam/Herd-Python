# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import keyvaluestore_pb2 as proto_dot_keyvaluestore__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto/keyvaluestore_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class KeyValueServiceStub(object):
    """KeyValueService defines the gRPC service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/keyvaluestore.KeyValueService/Get',
                request_serializer=proto_dot_keyvaluestore__pb2.GetRequest.SerializeToString,
                response_deserializer=proto_dot_keyvaluestore__pb2.KeyValue.FromString,
                _registered_method=True)
        self.GetAll = channel.unary_unary(
                '/keyvaluestore.KeyValueService/GetAll',
                request_serializer=proto_dot_keyvaluestore__pb2.GetAllRequest.SerializeToString,
                response_deserializer=proto_dot_keyvaluestore__pb2.GetAllResponse.FromString,
                _registered_method=True)
        self.GetKeys = channel.unary_unary(
                '/keyvaluestore.KeyValueService/GetKeys',
                request_serializer=proto_dot_keyvaluestore__pb2.GetKeysRequest.SerializeToString,
                response_deserializer=proto_dot_keyvaluestore__pb2.GetKeysResponse.FromString,
                _registered_method=True)
        self.GetValues = channel.unary_unary(
                '/keyvaluestore.KeyValueService/GetValues',
                request_serializer=proto_dot_keyvaluestore__pb2.GetValuesRequest.SerializeToString,
                response_deserializer=proto_dot_keyvaluestore__pb2.GetValuesResponse.FromString,
                _registered_method=True)
        self.Set = channel.unary_unary(
                '/keyvaluestore.KeyValueService/Set',
                request_serializer=proto_dot_keyvaluestore__pb2.SetRequest.SerializeToString,
                response_deserializer=proto_dot_keyvaluestore__pb2.SetResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/keyvaluestore.KeyValueService/Delete',
                request_serializer=proto_dot_keyvaluestore__pb2.DeleteRequest.SerializeToString,
                response_deserializer=proto_dot_keyvaluestore__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.DeleteAll = channel.unary_unary(
                '/keyvaluestore.KeyValueService/DeleteAll',
                request_serializer=proto_dot_keyvaluestore__pb2.DeleteAllRequest.SerializeToString,
                response_deserializer=proto_dot_keyvaluestore__pb2.DeleteAllResponse.FromString,
                _registered_method=True)


class KeyValueServiceServicer(object):
    """KeyValueService defines the gRPC service
    """

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetKeys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=proto_dot_keyvaluestore__pb2.GetRequest.FromString,
                    response_serializer=proto_dot_keyvaluestore__pb2.KeyValue.SerializeToString,
            ),
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=proto_dot_keyvaluestore__pb2.GetAllRequest.FromString,
                    response_serializer=proto_dot_keyvaluestore__pb2.GetAllResponse.SerializeToString,
            ),
            'GetKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKeys,
                    request_deserializer=proto_dot_keyvaluestore__pb2.GetKeysRequest.FromString,
                    response_serializer=proto_dot_keyvaluestore__pb2.GetKeysResponse.SerializeToString,
            ),
            'GetValues': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValues,
                    request_deserializer=proto_dot_keyvaluestore__pb2.GetValuesRequest.FromString,
                    response_serializer=proto_dot_keyvaluestore__pb2.GetValuesResponse.SerializeToString,
            ),
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=proto_dot_keyvaluestore__pb2.SetRequest.FromString,
                    response_serializer=proto_dot_keyvaluestore__pb2.SetResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=proto_dot_keyvaluestore__pb2.DeleteRequest.FromString,
                    response_serializer=proto_dot_keyvaluestore__pb2.DeleteResponse.SerializeToString,
            ),
            'DeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=proto_dot_keyvaluestore__pb2.DeleteAllRequest.FromString,
                    response_serializer=proto_dot_keyvaluestore__pb2.DeleteAllResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'keyvaluestore.KeyValueService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('keyvaluestore.KeyValueService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class KeyValueService(object):
    """KeyValueService defines the gRPC service
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/keyvaluestore.KeyValueService/Get',
            proto_dot_keyvaluestore__pb2.GetRequest.SerializeToString,
            proto_dot_keyvaluestore__pb2.KeyValue.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/keyvaluestore.KeyValueService/GetAll',
            proto_dot_keyvaluestore__pb2.GetAllRequest.SerializeToString,
            proto_dot_keyvaluestore__pb2.GetAllResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/keyvaluestore.KeyValueService/GetKeys',
            proto_dot_keyvaluestore__pb2.GetKeysRequest.SerializeToString,
            proto_dot_keyvaluestore__pb2.GetKeysResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/keyvaluestore.KeyValueService/GetValues',
            proto_dot_keyvaluestore__pb2.GetValuesRequest.SerializeToString,
            proto_dot_keyvaluestore__pb2.GetValuesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/keyvaluestore.KeyValueService/Set',
            proto_dot_keyvaluestore__pb2.SetRequest.SerializeToString,
            proto_dot_keyvaluestore__pb2.SetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/keyvaluestore.KeyValueService/Delete',
            proto_dot_keyvaluestore__pb2.DeleteRequest.SerializeToString,
            proto_dot_keyvaluestore__pb2.DeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/keyvaluestore.KeyValueService/DeleteAll',
            proto_dot_keyvaluestore__pb2.DeleteAllRequest.SerializeToString,
            proto_dot_keyvaluestore__pb2.DeleteAllResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
