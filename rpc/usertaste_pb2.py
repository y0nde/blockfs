# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: usertaste.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fusertaste.proto\x12\tusertaste\"\x14\n\x04User\x12\x0c\n\x04root\x18\x01 \x01(\t\"\x16\n\x04Stat\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\'\n\x04Want\x12\x11\n\tsomething\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x05\"\"\n\x04\x46ile\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x05\x32\x96\x01\n\tUserTaste\x12*\n\x04init\x12\x0f.usertaste.User\x1a\x0f.usertaste.Stat\"\x00\x12+\n\x05greet\x12\x0f.usertaste.Want\x1a\x0f.usertaste.Stat\"\x00\x12\x30\n\x08listfile\x12\x0f.usertaste.Want\x1a\x0f.usertaste.File\"\x00\x30\x01\x62\x06proto3')



_USER = DESCRIPTOR.message_types_by_name['User']
_STAT = DESCRIPTOR.message_types_by_name['Stat']
_WANT = DESCRIPTOR.message_types_by_name['Want']
_FILE = DESCRIPTOR.message_types_by_name['File']
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'usertaste_pb2'
  # @@protoc_insertion_point(class_scope:usertaste.User)
  })
_sym_db.RegisterMessage(User)

Stat = _reflection.GeneratedProtocolMessageType('Stat', (_message.Message,), {
  'DESCRIPTOR' : _STAT,
  '__module__' : 'usertaste_pb2'
  # @@protoc_insertion_point(class_scope:usertaste.Stat)
  })
_sym_db.RegisterMessage(Stat)

Want = _reflection.GeneratedProtocolMessageType('Want', (_message.Message,), {
  'DESCRIPTOR' : _WANT,
  '__module__' : 'usertaste_pb2'
  # @@protoc_insertion_point(class_scope:usertaste.Want)
  })
_sym_db.RegisterMessage(Want)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'usertaste_pb2'
  # @@protoc_insertion_point(class_scope:usertaste.File)
  })
_sym_db.RegisterMessage(File)

_USERTASTE = DESCRIPTOR.services_by_name['UserTaste']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=30
  _USER._serialized_end=50
  _STAT._serialized_start=52
  _STAT._serialized_end=74
  _WANT._serialized_start=76
  _WANT._serialized_end=115
  _FILE._serialized_start=117
  _FILE._serialized_end=151
  _USERTASTE._serialized_start=154
  _USERTASTE._serialized_end=304
# @@protoc_insertion_point(module_scope)
