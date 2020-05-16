# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protos/flights.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Protos/flights.proto',
  package='nycflights',
  syntax='proto3',
  serialized_options=b'\252\002\013GrpcFlights',
  serialized_pb=b'\n\x14Protos/flights.proto\x12\nnycflights\x1a\x1bgoogle/protobuf/empty.proto\"$\n\x12\x44\x65stinationRequest\x12\x0e\n\x06origin\x18\x01 \x01(\t\"W\n\x13\x44\x65stinationResponse\x12@\n\x15\x66lightsPerDestination\x18\x01 \x03(\x0b\x32!.nycflights.FlightsPerDestination\"U\n\x15\x46lightsPerDestination\x12\x17\n\x0fnumberOfFlights\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t\"4\n\x0e\x46lightResponse\x12\"\n\x06\x66light\x18\x01 \x03(\x0b\x32\x12.nycflights.Flight\" \n\x0e\x41irtimeRequest\x12\x0e\n\x06origin\x18\x01 \x01(\t\"3\n\x0f\x41irtimeAtOrigin\x12\x10\n\x08\x61ir_time\x18\x01 \x01(\x05\x12\x0e\n\x06origin\x18\x02 \x01(\t\"\x8e\x02\n\x06\x46light\x12\x0e\n\x06origin\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61rrier\x18\x03 \x01(\t\x12\x0f\n\x07tailnum\x18\x04 \x01(\t\x12\x0e\n\x06\x66light\x18\x05 \x01(\x05\x12\x0c\n\x04year\x18\x06 \x01(\x05\x12\r\n\x05month\x18\x07 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x08 \x01(\x05\x12\x10\n\x08\x64\x65p_time\x18\t \x01(\x05\x12\x11\n\tdep_delay\x18\n \x01(\x05\x12\x10\n\x08\x61rr_time\x18\x0b \x01(\x05\x12\x11\n\tarr_delay\x18\x0c \x01(\x05\x12\x10\n\x08\x61ir_time\x18\r \x01(\x05\x12\x10\n\x08\x64istance\x18\x0e \x01(\x05\x12\x0c\n\x04hour\x18\x0f \x01(\x05\x12\x0e\n\x06minute\x18\x10 \x01(\x05\"\x1d\n\x0bMonthNumber\x12\x0e\n\x06number\x18\x01 \x01(\x05\":\n\tAllMonths\x12-\n\x0cmonthNumbers\x18\x01 \x03(\x0b\x32\x17.nycflights.MonthNumber\"U\n\x0f\x46lightsPerMonth\x12,\n\x0bmonthNumber\x18\x01 \x01(\x0b\x32\x17.nycflights.MonthNumber\x12\x14\n\x0c\x66lightsCount\x18\x02 \x01(\x05\"G\n\x0f\x46lightsInMonths\x12\x34\n\x0f\x66lightsPerMonth\x18\x01 \x03(\x0b\x32\x1b.nycflights.FlightsPerMonth2\xa2\x03\n\x07\x46lights\x12@\n\nGetFlights\x12\x16.google.protobuf.Empty\x1a\x1a.nycflights.FlightResponse\x12R\n\x1aGetNumberOfFlightsPerMonth\x12\x17.nycflights.MonthNumber\x1a\x1b.nycflights.FlightsPerMonth\x12P\n\x1aGetNumberOfFlightsInMonths\x12\x15.nycflights.AllMonths\x1a\x1b.nycflights.FlightsInMonths\x12`\n\x1dGetTop10DestinationsForOrigin\x12\x1e.nycflights.DestinationRequest\x1a\x1f.nycflights.DestinationResponse\x12M\n\x12GetAirtimeAtOrigin\x12\x1a.nycflights.AirtimeRequest\x1a\x1b.nycflights.AirtimeAtOriginB\x0e\xaa\x02\x0bGrpcFlightsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DESTINATIONREQUEST = _descriptor.Descriptor(
  name='DestinationRequest',
  full_name='nycflights.DestinationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.DestinationRequest.origin', index=0,
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
  serialized_start=65,
  serialized_end=101,
)


_DESTINATIONRESPONSE = _descriptor.Descriptor(
  name='DestinationResponse',
  full_name='nycflights.DestinationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flightsPerDestination', full_name='nycflights.DestinationResponse.flightsPerDestination', index=0,
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
  serialized_start=103,
  serialized_end=190,
)


_FLIGHTSPERDESTINATION = _descriptor.Descriptor(
  name='FlightsPerDestination',
  full_name='nycflights.FlightsPerDestination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numberOfFlights', full_name='nycflights.FlightsPerDestination.numberOfFlights', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='nycflights.FlightsPerDestination.destination', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.FlightsPerDestination.origin', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=192,
  serialized_end=277,
)


_FLIGHTRESPONSE = _descriptor.Descriptor(
  name='FlightResponse',
  full_name='nycflights.FlightResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flight', full_name='nycflights.FlightResponse.flight', index=0,
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
  serialized_start=279,
  serialized_end=331,
)


_AIRTIMEREQUEST = _descriptor.Descriptor(
  name='AirtimeRequest',
  full_name='nycflights.AirtimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.AirtimeRequest.origin', index=0,
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
  serialized_start=333,
  serialized_end=365,
)


_AIRTIMEATORIGIN = _descriptor.Descriptor(
  name='AirtimeAtOrigin',
  full_name='nycflights.AirtimeAtOrigin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='air_time', full_name='nycflights.AirtimeAtOrigin.air_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.AirtimeAtOrigin.origin', index=1,
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
  serialized_start=367,
  serialized_end=418,
)


_FLIGHT = _descriptor.Descriptor(
  name='Flight',
  full_name='nycflights.Flight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='nycflights.Flight.origin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest', full_name='nycflights.Flight.dest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='carrier', full_name='nycflights.Flight.carrier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tailnum', full_name='nycflights.Flight.tailnum', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flight', full_name='nycflights.Flight.flight', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='nycflights.Flight.year', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='nycflights.Flight.month', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='nycflights.Flight.day', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dep_time', full_name='nycflights.Flight.dep_time', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dep_delay', full_name='nycflights.Flight.dep_delay', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arr_time', full_name='nycflights.Flight.arr_time', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arr_delay', full_name='nycflights.Flight.arr_delay', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='air_time', full_name='nycflights.Flight.air_time', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='nycflights.Flight.distance', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='nycflights.Flight.hour', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minute', full_name='nycflights.Flight.minute', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=421,
  serialized_end=691,
)


_MONTHNUMBER = _descriptor.Descriptor(
  name='MonthNumber',
  full_name='nycflights.MonthNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='nycflights.MonthNumber.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=693,
  serialized_end=722,
)


_ALLMONTHS = _descriptor.Descriptor(
  name='AllMonths',
  full_name='nycflights.AllMonths',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='monthNumbers', full_name='nycflights.AllMonths.monthNumbers', index=0,
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
  serialized_start=724,
  serialized_end=782,
)


_FLIGHTSPERMONTH = _descriptor.Descriptor(
  name='FlightsPerMonth',
  full_name='nycflights.FlightsPerMonth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='monthNumber', full_name='nycflights.FlightsPerMonth.monthNumber', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flightsCount', full_name='nycflights.FlightsPerMonth.flightsCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=784,
  serialized_end=869,
)


_FLIGHTSINMONTHS = _descriptor.Descriptor(
  name='FlightsInMonths',
  full_name='nycflights.FlightsInMonths',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flightsPerMonth', full_name='nycflights.FlightsInMonths.flightsPerMonth', index=0,
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
  serialized_start=871,
  serialized_end=942,
)

_DESTINATIONRESPONSE.fields_by_name['flightsPerDestination'].message_type = _FLIGHTSPERDESTINATION
_FLIGHTRESPONSE.fields_by_name['flight'].message_type = _FLIGHT
_ALLMONTHS.fields_by_name['monthNumbers'].message_type = _MONTHNUMBER
_FLIGHTSPERMONTH.fields_by_name['monthNumber'].message_type = _MONTHNUMBER
_FLIGHTSINMONTHS.fields_by_name['flightsPerMonth'].message_type = _FLIGHTSPERMONTH
DESCRIPTOR.message_types_by_name['DestinationRequest'] = _DESTINATIONREQUEST
DESCRIPTOR.message_types_by_name['DestinationResponse'] = _DESTINATIONRESPONSE
DESCRIPTOR.message_types_by_name['FlightsPerDestination'] = _FLIGHTSPERDESTINATION
DESCRIPTOR.message_types_by_name['FlightResponse'] = _FLIGHTRESPONSE
DESCRIPTOR.message_types_by_name['AirtimeRequest'] = _AIRTIMEREQUEST
DESCRIPTOR.message_types_by_name['AirtimeAtOrigin'] = _AIRTIMEATORIGIN
DESCRIPTOR.message_types_by_name['Flight'] = _FLIGHT
DESCRIPTOR.message_types_by_name['MonthNumber'] = _MONTHNUMBER
DESCRIPTOR.message_types_by_name['AllMonths'] = _ALLMONTHS
DESCRIPTOR.message_types_by_name['FlightsPerMonth'] = _FLIGHTSPERMONTH
DESCRIPTOR.message_types_by_name['FlightsInMonths'] = _FLIGHTSINMONTHS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DestinationRequest = _reflection.GeneratedProtocolMessageType('DestinationRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESTINATIONREQUEST,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.DestinationRequest)
  })
_sym_db.RegisterMessage(DestinationRequest)

DestinationResponse = _reflection.GeneratedProtocolMessageType('DestinationResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESTINATIONRESPONSE,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.DestinationResponse)
  })
_sym_db.RegisterMessage(DestinationResponse)

FlightsPerDestination = _reflection.GeneratedProtocolMessageType('FlightsPerDestination', (_message.Message,), {
  'DESCRIPTOR' : _FLIGHTSPERDESTINATION,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.FlightsPerDestination)
  })
_sym_db.RegisterMessage(FlightsPerDestination)

FlightResponse = _reflection.GeneratedProtocolMessageType('FlightResponse', (_message.Message,), {
  'DESCRIPTOR' : _FLIGHTRESPONSE,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.FlightResponse)
  })
_sym_db.RegisterMessage(FlightResponse)

AirtimeRequest = _reflection.GeneratedProtocolMessageType('AirtimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _AIRTIMEREQUEST,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.AirtimeRequest)
  })
_sym_db.RegisterMessage(AirtimeRequest)

AirtimeAtOrigin = _reflection.GeneratedProtocolMessageType('AirtimeAtOrigin', (_message.Message,), {
  'DESCRIPTOR' : _AIRTIMEATORIGIN,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.AirtimeAtOrigin)
  })
_sym_db.RegisterMessage(AirtimeAtOrigin)

Flight = _reflection.GeneratedProtocolMessageType('Flight', (_message.Message,), {
  'DESCRIPTOR' : _FLIGHT,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.Flight)
  })
_sym_db.RegisterMessage(Flight)

MonthNumber = _reflection.GeneratedProtocolMessageType('MonthNumber', (_message.Message,), {
  'DESCRIPTOR' : _MONTHNUMBER,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.MonthNumber)
  })
_sym_db.RegisterMessage(MonthNumber)

AllMonths = _reflection.GeneratedProtocolMessageType('AllMonths', (_message.Message,), {
  'DESCRIPTOR' : _ALLMONTHS,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.AllMonths)
  })
_sym_db.RegisterMessage(AllMonths)

FlightsPerMonth = _reflection.GeneratedProtocolMessageType('FlightsPerMonth', (_message.Message,), {
  'DESCRIPTOR' : _FLIGHTSPERMONTH,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.FlightsPerMonth)
  })
_sym_db.RegisterMessage(FlightsPerMonth)

FlightsInMonths = _reflection.GeneratedProtocolMessageType('FlightsInMonths', (_message.Message,), {
  'DESCRIPTOR' : _FLIGHTSINMONTHS,
  '__module__' : 'Protos.flights_pb2'
  # @@protoc_insertion_point(class_scope:nycflights.FlightsInMonths)
  })
_sym_db.RegisterMessage(FlightsInMonths)


DESCRIPTOR._options = None

_FLIGHTS = _descriptor.ServiceDescriptor(
  name='Flights',
  full_name='nycflights.Flights',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=945,
  serialized_end=1363,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFlights',
    full_name='nycflights.Flights.GetFlights',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_FLIGHTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNumberOfFlightsPerMonth',
    full_name='nycflights.Flights.GetNumberOfFlightsPerMonth',
    index=1,
    containing_service=None,
    input_type=_MONTHNUMBER,
    output_type=_FLIGHTSPERMONTH,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNumberOfFlightsInMonths',
    full_name='nycflights.Flights.GetNumberOfFlightsInMonths',
    index=2,
    containing_service=None,
    input_type=_ALLMONTHS,
    output_type=_FLIGHTSINMONTHS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTop10DestinationsForOrigin',
    full_name='nycflights.Flights.GetTop10DestinationsForOrigin',
    index=3,
    containing_service=None,
    input_type=_DESTINATIONREQUEST,
    output_type=_DESTINATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAirtimeAtOrigin',
    full_name='nycflights.Flights.GetAirtimeAtOrigin',
    index=4,
    containing_service=None,
    input_type=_AIRTIMEREQUEST,
    output_type=_AIRTIMEATORIGIN,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FLIGHTS)

DESCRIPTOR.services_by_name['Flights'] = _FLIGHTS

# @@protoc_insertion_point(module_scope)
