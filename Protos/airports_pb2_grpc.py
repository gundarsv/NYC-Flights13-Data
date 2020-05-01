# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Protos.airports_pb2 as airports__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AirportsStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAirports = channel.unary_unary(
                '/nycflights.Airports/GetAirports',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=airports__pb2.AirportResponse.FromString,
                )


class AirportsServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetAirports(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AirportsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAirports': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAirports,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=airports__pb2.AirportResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nycflights.Airports', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Airports(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetAirports(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nycflights.Airports/GetAirports',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            airports__pb2.AirportResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
