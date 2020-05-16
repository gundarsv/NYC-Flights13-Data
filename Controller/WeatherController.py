import Protos.weather_pb2_grpc as weather_pb2_grpc
import Protos.weather_pb2 as weather_pb2
from Repository.repository_helper import get_daily_mean_temperature


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
        return weather_pb2.ObservationResponse(observationsAtOrigin=all_observations_at_origin.observationsAtOrigin, origin=all_observations_at_origin.origin)

    def GetWeatherObservationsAtOrigins(self, request, context):
        origins = []

        for data in request.origins:
            origins.append(data.origin)

        observations_at_origins = self.repository.get_weather_observations_at_origins(origins=origins)

        grpc_observations_at_origins = []

        for data in observations_at_origins:
            grpc_observations_at_origins.append(weather_pb2.ObservationResponse(observationsAtOrigin=data.observationsAtOrigin, origin=data.origin))

        return weather_pb2.ObservationsResponse(observations=grpc_observations_at_origins)

    def GetTemperatureAtOrigins(self, request, context):
        origins = []

        for data in request.origins:
            origins.append(data.origin)

        temperature_at_origins = self.repository.get_temperature_at_origins(origins=origins)

        grpc_temperature_at_origins = []

        for data in temperature_at_origins:
            grpc_temperature_at_origins.append(
                weather_pb2.AllOriginTemperature(temperatureAtOrigin=weather_pb2.TemperatureAtOrigin(year=data.year, month=data.month, day=data.day, hour=data.hour, temp=data.temp),
                                            origin=data.origin))

        return weather_pb2.AllOriginTemperatureResponse(allOriginTemperatures=grpc_temperature_at_origins)

    def GetDailyMeanTemperatureAtOrigin(self, request, context):
        all_temperature_data_at_origin = self.repository.get_temperature_at_origin(request.origin)

        grpc_temperature_data_with_daily_mean = []

        for _, data in get_daily_mean_temperature(all_temperature_data_at_origin).iterrows():
            grpc_temperature_data_with_daily_mean.append(weather_pb2.DailyMeanTemperature(year=int(data.year), month=int(data.month), day=int(data.day),
                                               meanTemp=data.mean_temperature))

        return weather_pb2.DailyMeanTemperatureResponse(dailyMeanTemperatures=grpc_temperature_data_with_daily_mean)

