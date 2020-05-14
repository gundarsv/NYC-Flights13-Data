import Protos.weather_pb2_grpc as weather_pb2_grpc
import Protos.weather_pb2 as weather_pb2


def add_weather_controller_to_server(server, repository):
    weather_pb2_grpc.add_WeathersServicer_to_server(WeatherController(repository), server)


class WeatherController(weather_pb2_grpc.WeathersServicer):
    repository = None

    def __init__(self, repository):
        self.repository = repository

    def GetWeather(self, request, context):
        all_weather = self.repository.get_all_weather()
        grpc_weather = []
        for data in all_weather:
            grpc_weather.append(weather_pb2.Weather(origin=data.origin, year=data.year, month=data.month, day=data.day, hour=data.hour, temp=data.temp, dewp=data.dewp, humid=data.humid, wind_dir=data.wind_dir, wind_speed=data.wind_speed, wind_gust=data.wind_gust, precip=data.precip, pressure=data.pressure, visib=data.visib, time_hour=data.time_hour))
        return weather_pb2.WeatherResponse(weather=grpc_weather)

    def GetTemperatureAtOrigin(self, request, context):
        all_temperature_at_origin = self.repository.get_temperature_at_origin(request.origin)
        grpc_temperature_at_origins = []
        for data in all_temperature_at_origin:
            grpc_temperature_at_origins.append(weather_pb2.TemperatureAtOrigin(year=data.year, month=data.month, day=data.day, hour=data.hour, temp=data.temp))

        return weather_pb2.TemperatureResponse(temperatureAtOrigins=grpc_temperature_at_origins)

    def GetWeatherObservationsAtOrigin(self, request, context):
        all_observations_at_origin = self.repository.get_weather_observations_at_origin(request.origin)
        return weather_pb2.ObservationsResponse(observationsAtOrigin=all_observations_at_origin.observationsAtOrigin, origin=all_observations_at_origin.origin)

