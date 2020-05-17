# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protos/weather.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Protos/weather.proto',
  package='nycflights',
  syntax='proto3',
  serialized_options=b'\252\002\013GrpcWeather',
  serialized_pb=b'\n\x14Protos/weather.proto\x12\nnycflights\x1a\x1bgoogle/protobuf/empty.proto\"C\n\x13ObservationResponse\x12\x1c\n\x14observationsAtOrigin\x18\x01 \x01(\x05\x12\x0e\n\x06origin\x18\x02 \x01(\t\"M\n\x14ObservationsResponse\x12\x35\n\x0cobservations\x18\x01 \x03(\x0b\x32\x1f.nycflights.ObservationResponse\"\x1f\n\rOriginRequest\x12\x0e\n\x06origin\x18\x01 \x01(\t\"<\n\x0eOriginsRequest\x12*\n\x07origins\x18\x01 \x03(\x0b\x32\x19.nycflights.OriginRequest\"d\n\x14\x41llOriginTemperature\x12<\n\x13temperatureAtOrigin\x18\x01 \x01(\x0b\x32\x1f.nycflights.TemperatureAtOrigin\x12\x0e\n\x06origin\x18\x02 \x01(\t\"_\n\x1c\x41llOriginTemperatureResponse\x12?\n\x15\x61llOriginTemperatures\x18\x01 \x03(\x0b\x32 .nycflights.AllOriginTemperature\"_\n\x1c\x44\x61ilyMeanTemperatureResponse\x12?\n\x15\x64\x61ilyMeanTemperatures\x18\x01 \x03(\x0b\x32 .nycflights.DailyMeanTemperature\"b\n\x14\x44\x61ilyMeanTemperature\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\x12\x10\n\x08meanTemp\x18\x04 \x01(\x02\x12\x0e\n\x06origin\x18\x05 \x01(\t\"k\n\x13TemperatureAtOrigin\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\x12\x0c\n\x04hour\x18\x04 \x01(\x05\x12\x0c\n\x04temp\x18\x05 \x01(\x02\x12\x0e\n\x06origin\x18\x06 \x01(\t\"T\n\x13TemperatureResponse\x12=\n\x14temperatureAtOrigins\x18\x01 \x03(\x0b\x32\x1f.nycflights.TemperatureAtOrigin\"7\n\x0fWeatherResponse\x12$\n\x07weather\x18\x01 \x03(\x0b\x32\x13.nycflights.Weather\"\xf9\x01\n\x07Weather\x12\x0e\n\x06origin\x18\x01 \x01(\t\x12\x0c\n\x04year\x18\x02 \x01(\x05\x12\r\n\x05month\x18\x03 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x05\x12\x0c\n\x04hour\x18\x05 \x01(\x05\x12\x0c\n\x04temp\x18\x06 \x01(\x02\x12\x0c\n\x04\x64\x65wp\x18\x07 \x01(\x02\x12\r\n\x05humid\x18\x08 \x01(\x02\x12\x10\n\x08wind_dir\x18\t \x01(\x05\x12\x12\n\nwind_speed\x18\n \x01(\x02\x12\x11\n\twind_gust\x18\x0b \x01(\x02\x12\x0e\n\x06precip\x18\x0c \x01(\x02\x12\x10\n\x08pressure\x18\r \x01(\x02\x12\r\n\x05visib\x18\x0e \x01(\x02\x12\x11\n\ttime_hour\x18\x0f \x01(\t2\x95\x05\n\x08Weathers\x12\x41\n\nGetWeather\x12\x16.google.protobuf.Empty\x1a\x1b.nycflights.WeatherResponse\x12T\n\x16GetTemperatureAtOrigin\x12\x19.nycflights.OriginRequest\x1a\x1f.nycflights.TemperatureResponse\x12\\\n\x1eGetWeatherObservationsAtOrigin\x12\x19.nycflights.OriginRequest\x1a\x1f.nycflights.ObservationResponse\x12_\n\x1fGetWeatherObservationsAtOrigins\x12\x1a.nycflights.OriginsRequest\x1a .nycflights.ObservationsResponse\x12_\n\x17GetTemperatureAtOrigins\x12\x1a.nycflights.OriginsRequest\x1a(.nycflights.AllOriginTemperatureResponse\x12\x66\n\x1fGetDailyMeanTemperatureAtOrigin\x12\x19.nycflights.OriginRequest\x1a(.nycflights.DailyMeanTemperatureResponse\x12h\n GetDailyMeanTemperatureAtOrigins\x12\x1a.nycflights.OriginsRequest\x1a(.nycflights.DailyMeanTemperatureResponseB\x0e\xaa\x02\x0bGrpcWeatherb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_OBSERVATIONRESPONSE = _descriptor.Descriptor(
  name='ObservationResponse',
  full_name='nycflights.ObservationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observationsAtOrigin', full_name='nycflights.ObservationResponse.observationsAtOrigin', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.ObservationResponse.origin', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=132,
)


_OBSERVATIONSRESPONSE = _descriptor.Descriptor(
  name='ObservationsResponse',
  full_name='nycflights.ObservationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observations', full_name='nycflights.ObservationsResponse.observations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=211,
)


_ORIGINREQUEST = _descriptor.Descriptor(
  name='OriginRequest',
  full_name='nycflights.OriginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.OriginRequest.origin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=244,
)


_ORIGINSREQUEST = _descriptor.Descriptor(
  name='OriginsRequest',
  full_name='nycflights.OriginsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origins', full_name='nycflights.OriginsRequest.origins', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=306,
)


_ALLORIGINTEMPERATURE = _descriptor.Descriptor(
  name='AllOriginTemperature',
  full_name='nycflights.AllOriginTemperature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperatureAtOrigin', full_name='nycflights.AllOriginTemperature.temperatureAtOrigin', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.AllOriginTemperature.origin', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=408,
)


_ALLORIGINTEMPERATURERESPONSE = _descriptor.Descriptor(
  name='AllOriginTemperatureResponse',
  full_name='nycflights.AllOriginTemperatureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allOriginTemperatures', full_name='nycflights.AllOriginTemperatureResponse.allOriginTemperatures', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=505,
)


_DAILYMEANTEMPERATURERESPONSE = _descriptor.Descriptor(
  name='DailyMeanTemperatureResponse',
  full_name='nycflights.DailyMeanTemperatureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dailyMeanTemperatures', full_name='nycflights.DailyMeanTemperatureResponse.dailyMeanTemperatures', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=602,
)


_DAILYMEANTEMPERATURE = _descriptor.Descriptor(
  name='DailyMeanTemperature',
  full_name='nycflights.DailyMeanTemperature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='nycflights.DailyMeanTemperature.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='nycflights.DailyMeanTemperature.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='nycflights.DailyMeanTemperature.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meanTemp', full_name='nycflights.DailyMeanTemperature.meanTemp', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.DailyMeanTemperature.origin', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=702,
)


_TEMPERATUREATORIGIN = _descriptor.Descriptor(
  name='TemperatureAtOrigin',
  full_name='nycflights.TemperatureAtOrigin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='nycflights.TemperatureAtOrigin.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='nycflights.TemperatureAtOrigin.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='nycflights.TemperatureAtOrigin.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='nycflights.TemperatureAtOrigin.hour', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temp', full_name='nycflights.TemperatureAtOrigin.temp', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.TemperatureAtOrigin.origin', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=704,
  serialized_end=811,
)


_TEMPERATURERESPONSE = _descriptor.Descriptor(
  name='TemperatureResponse',
  full_name='nycflights.TemperatureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperatureAtOrigins', full_name='nycflights.TemperatureResponse.temperatureAtOrigins', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=813,
  serialized_end=897,
)


_WEATHERRESPONSE = _descriptor.Descriptor(
  name='WeatherResponse',
  full_name='nycflights.WeatherResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weather', full_name='nycflights.WeatherResponse.weather', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=899,
  serialized_end=954,
)


_WEATHER = _descriptor.Descriptor(
  name='Weather',
  full_name='nycflights.Weather',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.Weather.origin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='nycflights.Weather.year', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='nycflights.Weather.month', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='nycflights.Weather.day', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='nycflights.Weather.hour', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temp', full_name='nycflights.Weather.temp', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dewp', full_name='nycflights.Weather.dewp', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='humid', full_name='nycflights.Weather.humid', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wind_dir', full_name='nycflights.Weather.wind_dir', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wind_speed', full_name='nycflights.Weather.wind_speed', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wind_gust', full_name='nycflights.Weather.wind_gust', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precip', full_name='nycflights.Weather.precip', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pressure', full_name='nycflights.Weather.pressure', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visib', full_name='nycflights.Weather.visib', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_hour', full_name='nycflights.Weather.time_hour', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=957,
  serialized_end=1206,
)

_OBSERVATIONSRESPONSE.fields_by_name['observations'].message_type = _OBSERVATIONRESPONSE
_ORIGINSREQUEST.fields_by_name['origins'].message_type = _ORIGINREQUEST
_ALLORIGINTEMPERATURE.fields_by_name['temperatureAtOrigin'].message_type = _TEMPERATUREATORIGIN
_ALLORIGINTEMPERATURERESPONSE.fields_by_name['allOriginTemperatures'].message_type = _ALLORIGINTEMPERATURE
_DAILYMEANTEMPERATURERESPONSE.fields_by_name['dailyMeanTemperatures'].message_type = _DAILYMEANTEMPERATURE
_TEMPERATURERESPONSE.fields_by_name['temperatureAtOrigins'].message_type = _TEMPERATUREATORIGIN
_WEATHERRESPONSE.fields_by_name['weather'].message_type = _WEATHER
DESCRIPTOR.message_types_by_name['ObservationResponse'] = _OBSERVATIONRESPONSE
DESCRIPTOR.message_types_by_name['ObservationsResponse'] = _OBSERVATIONSRESPONSE
DESCRIPTOR.message_types_by_name['OriginRequest'] = _ORIGINREQUEST
DESCRIPTOR.message_types_by_name['OriginsRequest'] = _ORIGINSREQUEST
DESCRIPTOR.message_types_by_name['AllOriginTemperature'] = _ALLORIGINTEMPERATURE
DESCRIPTOR.message_types_by_name['AllOriginTemperatureResponse'] = _ALLORIGINTEMPERATURERESPONSE
DESCRIPTOR.message_types_by_name['DailyMeanTemperatureResponse'] = _DAILYMEANTEMPERATURERESPONSE
DESCRIPTOR.message_types_by_name['DailyMeanTemperature'] = _DAILYMEANTEMPERATURE
DESCRIPTOR.message_types_by_name['TemperatureAtOrigin'] = _TEMPERATUREATORIGIN
DESCRIPTOR.message_types_by_name['TemperatureResponse'] = _TEMPERATURERESPONSE
DESCRIPTOR.message_types_by_name['WeatherResponse'] = _WEATHERRESPONSE
DESCRIPTOR.message_types_by_name['Weather'] = _WEATHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObservationResponse = _reflection.GeneratedProtocolMessageType('ObservationResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATIONRESPONSE,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.ObservationResponse)
  })
_sym_db.RegisterMessage(ObservationResponse)

ObservationsResponse = _reflection.GeneratedProtocolMessageType('ObservationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATIONSRESPONSE,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.ObservationsResponse)
  })
_sym_db.RegisterMessage(ObservationsResponse)

OriginRequest = _reflection.GeneratedProtocolMessageType('OriginRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORIGINREQUEST,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.OriginRequest)
  })
_sym_db.RegisterMessage(OriginRequest)

OriginsRequest = _reflection.GeneratedProtocolMessageType('OriginsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORIGINSREQUEST,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.OriginsRequest)
  })
_sym_db.RegisterMessage(OriginsRequest)

AllOriginTemperature = _reflection.GeneratedProtocolMessageType('AllOriginTemperature', (_message.Message,), {
  'DESCRIPTOR' : _ALLORIGINTEMPERATURE,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.AllOriginTemperature)
  })
_sym_db.RegisterMessage(AllOriginTemperature)

AllOriginTemperatureResponse = _reflection.GeneratedProtocolMessageType('AllOriginTemperatureResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLORIGINTEMPERATURERESPONSE,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.AllOriginTemperatureResponse)
  })
_sym_db.RegisterMessage(AllOriginTemperatureResponse)

DailyMeanTemperatureResponse = _reflection.GeneratedProtocolMessageType('DailyMeanTemperatureResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYMEANTEMPERATURERESPONSE,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.DailyMeanTemperatureResponse)
  })
_sym_db.RegisterMessage(DailyMeanTemperatureResponse)

DailyMeanTemperature = _reflection.GeneratedProtocolMessageType('DailyMeanTemperature', (_message.Message,), {
  'DESCRIPTOR' : _DAILYMEANTEMPERATURE,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.DailyMeanTemperature)
  })
_sym_db.RegisterMessage(DailyMeanTemperature)

TemperatureAtOrigin = _reflection.GeneratedProtocolMessageType('TemperatureAtOrigin', (_message.Message,), {
  'DESCRIPTOR' : _TEMPERATUREATORIGIN,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.TemperatureAtOrigin)
  })
_sym_db.RegisterMessage(TemperatureAtOrigin)

TemperatureResponse = _reflection.GeneratedProtocolMessageType('TemperatureResponse', (_message.Message,), {
  'DESCRIPTOR' : _TEMPERATURERESPONSE,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.TemperatureResponse)
  })
_sym_db.RegisterMessage(TemperatureResponse)

WeatherResponse = _reflection.GeneratedProtocolMessageType('WeatherResponse', (_message.Message,), {
  'DESCRIPTOR' : _WEATHERRESPONSE,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.WeatherResponse)
  })
_sym_db.RegisterMessage(WeatherResponse)

Weather = _reflection.GeneratedProtocolMessageType('Weather', (_message.Message,), {
  'DESCRIPTOR' : _WEATHER,
  '__module__' : 'Protos.weather_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.Weather)
  })
_sym_db.RegisterMessage(Weather)


DESCRIPTOR._options = None

_WEATHERS = _descriptor.ServiceDescriptor(
  name='Weathers',
  full_name='nycflights.Weathers',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1209,
  serialized_end=1870,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetWeather',
    full_name='nycflights.Weathers.GetWeather',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_WEATHERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTemperatureAtOrigin',
    full_name='nycflights.Weathers.GetTemperatureAtOrigin',
    index=1,
    containing_service=None,
    input_type=_ORIGINREQUEST,
    output_type=_TEMPERATURERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWeatherObservationsAtOrigin',
    full_name='nycflights.Weathers.GetWeatherObservationsAtOrigin',
    index=2,
    containing_service=None,
    input_type=_ORIGINREQUEST,
    output_type=_OBSERVATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWeatherObservationsAtOrigins',
    full_name='nycflights.Weathers.GetWeatherObservationsAtOrigins',
    index=3,
    containing_service=None,
    input_type=_ORIGINSREQUEST,
    output_type=_OBSERVATIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTemperatureAtOrigins',
    full_name='nycflights.Weathers.GetTemperatureAtOrigins',
    index=4,
    containing_service=None,
    input_type=_ORIGINSREQUEST,
    output_type=_ALLORIGINTEMPERATURERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDailyMeanTemperatureAtOrigin',
    full_name='nycflights.Weathers.GetDailyMeanTemperatureAtOrigin',
    index=5,
    containing_service=None,
    input_type=_ORIGINREQUEST,
    output_type=_DAILYMEANTEMPERATURERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDailyMeanTemperatureAtOrigins',
    full_name='nycflights.Weathers.GetDailyMeanTemperatureAtOrigins',
    index=6,
    containing_service=None,
    input_type=_ORIGINSREQUEST,
    output_type=_DAILYMEANTEMPERATURERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WEATHERS)

DESCRIPTOR.services_by_name['Weathers'] = _WEATHERS

# @@protoc_insertion_point(module_scope)
