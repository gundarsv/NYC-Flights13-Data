# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from Protos import planes_pb2 as Protos_dot_planes__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class PlanesStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPlanes = channel.unary_unary(
                '/nycflights.Planes/GetPlanes',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=Protos_dot_planes__pb2.PlaneResponse.FromString,
                )
        self.GetManufacturersWithMoreThan200Planes = channel.unary_unary(
                '/nycflights.Planes/GetManufacturersWithMoreThan200Planes',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=Protos_dot_planes__pb2.ManufacturersResponse.FromString,
                )
        self.GetNumberOfPlanesForEachManufacturerModel = channel.unary_unary(
                '/nycflights.Planes/GetNumberOfPlanesForEachManufacturerModel',
                request_serializer=Protos_dot_planes__pb2.Manufacturer.SerializeToString,
                response_deserializer=Protos_dot_planes__pb2.NumberOfPlanesForModelResponse.FromString,
                )


class PlanesServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetPlanes(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetManufacturersWithMoreThan200Planes(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNumberOfPlanesForEachManufacturerModel(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlanesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPlanes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlanes,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=Protos_dot_planes__pb2.PlaneResponse.SerializeToString,
            ),
            'GetManufacturersWithMoreThan200Planes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetManufacturersWithMoreThan200Planes,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=Protos_dot_planes__pb2.ManufacturersResponse.SerializeToString,
            ),
            'GetNumberOfPlanesForEachManufacturerModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNumberOfPlanesForEachManufacturerModel,
                    request_deserializer=Protos_dot_planes__pb2.Manufacturer.FromString,
                    response_serializer=Protos_dot_planes__pb2.NumberOfPlanesForModelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nycflights.Planes', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Planes(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetPlanes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nycflights.Planes/GetPlanes',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            Protos_dot_planes__pb2.PlaneResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetManufacturersWithMoreThan200Planes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nycflights.Planes/GetManufacturersWithMoreThan200Planes',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            Protos_dot_planes__pb2.ManufacturersResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNumberOfPlanesForEachManufacturerModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nycflights.Planes/GetNumberOfPlanesForEachManufacturerModel',
            Protos_dot_planes__pb2.Manufacturer.SerializeToString,
            Protos_dot_planes__pb2.NumberOfPlanesForModelResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
