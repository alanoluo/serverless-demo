# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cls_kv.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cls_kv.proto',
  package='cls',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63ls_kv.proto\x12\x03\x63ls\"^\n\x03Log\x12\x0c\n\x04time\x18\x01 \x02(\x03\x12\"\n\x08\x63ontents\x18\x02 \x03(\x0b\x32\x10.cls.Log.Content\x1a%\n\x07\x43ontent\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"$\n\x06LogTag\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"w\n\x08LogGroup\x12\x16\n\x04logs\x18\x01 \x03(\x0b\x32\x08.cls.Log\x12\x13\n\x0b\x63ontextFlow\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x1c\n\x07logTags\x18\x05 \x03(\x0b\x32\x0b.cls.LogTag\"3\n\x0cLogGroupList\x12#\n\x0clogGroupList\x18\x01 \x03(\x0b\x32\r.cls.LogGroup')
)




_LOG_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='cls.Log.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cls.Log.Content.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cls.Log.Content.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=115,
)

_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='cls.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='cls.Log.time', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='cls.Log.contents', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOG_CONTENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=115,
)


_LOGTAG = _descriptor.Descriptor(
  name='LogTag',
  full_name='cls.LogTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cls.LogTag.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cls.LogTag.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=153,
)


_LOGGROUP = _descriptor.Descriptor(
  name='LogGroup',
  full_name='cls.LogGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logs', full_name='cls.LogGroup.logs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contextFlow', full_name='cls.LogGroup.contextFlow', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='cls.LogGroup.filename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='cls.LogGroup.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logTags', full_name='cls.LogGroup.logTags', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=274,
)


_LOGGROUPLIST = _descriptor.Descriptor(
  name='LogGroupList',
  full_name='cls.LogGroupList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logGroupList', full_name='cls.LogGroupList.logGroupList', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=327,
)

_LOG_CONTENT.containing_type = _LOG
_LOG.fields_by_name['contents'].message_type = _LOG_CONTENT
_LOGGROUP.fields_by_name['logs'].message_type = _LOG
_LOGGROUP.fields_by_name['logTags'].message_type = _LOGTAG
_LOGGROUPLIST.fields_by_name['logGroupList'].message_type = _LOGGROUP
DESCRIPTOR.message_types_by_name['Log'] = _LOG
DESCRIPTOR.message_types_by_name['LogTag'] = _LOGTAG
DESCRIPTOR.message_types_by_name['LogGroup'] = _LOGGROUP
DESCRIPTOR.message_types_by_name['LogGroupList'] = _LOGGROUPLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), dict(

  Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), dict(
    DESCRIPTOR = _LOG_CONTENT,
    __module__ = 'cls_kv_pb2'
    # @@protoc_insertion_point(class_scope:cls.Log.Content)
    ))
  ,
  DESCRIPTOR = _LOG,
  __module__ = 'cls_kv_pb2'
  # @@protoc_insertion_point(class_scope:cls.Log)
  ))
_sym_db.RegisterMessage(Log)
_sym_db.RegisterMessage(Log.Content)

LogTag = _reflection.GeneratedProtocolMessageType('LogTag', (_message.Message,), dict(
  DESCRIPTOR = _LOGTAG,
  __module__ = 'cls_kv_pb2'
  # @@protoc_insertion_point(class_scope:cls.LogTag)
  ))
_sym_db.RegisterMessage(LogTag)

LogGroup = _reflection.GeneratedProtocolMessageType('LogGroup', (_message.Message,), dict(
  DESCRIPTOR = _LOGGROUP,
  __module__ = 'cls_kv_pb2'
  # @@protoc_insertion_point(class_scope:cls.LogGroup)
  ))
_sym_db.RegisterMessage(LogGroup)

LogGroupList = _reflection.GeneratedProtocolMessageType('LogGroupList', (_message.Message,), dict(
  DESCRIPTOR = _LOGGROUPLIST,
  __module__ = 'cls_kv_pb2'
  # @@protoc_insertion_point(class_scope:cls.LogGroupList)
  ))
_sym_db.RegisterMessage(LogGroupList)


# @@protoc_insertion_point(module_scope)
