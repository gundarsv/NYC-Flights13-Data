# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import Protos.weather_pb2 as weather__pb2



class WeathersStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetWeather = channel.unary_unary(
                '/nycflights.Weathers/GetWeather',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=weather__pb2.WeatherResponse.FromString,
                )


class WeathersServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetWeather(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WeathersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetWeather': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWeather,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=weather__pb2.WeatherResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nycflights.Weathers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Weathers(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetWeather(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nycflights.Weathers/GetWeather',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            weather__pb2.WeatherResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
