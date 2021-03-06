# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dodo_servicer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dodo_servicer.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x64odo_servicer.proto\x12\x04grpc\"\"\n\x0fSuccessResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"S\n\x04ToDo\x12\x0b\n\x03tid\x18\x01 \x01(\r\x12\x11\n\tcreatorID\x18\x02 \x01(\r\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0e\n\x06isDone\x18\x04 \x01(\x08\x12\r\n\x05\x63olor\x18\x06 \x01(\t\"0\n\x0eToDoIdentifier\x12\x0b\n\x03tid\x18\x01 \x01(\r\x12\x11\n\tcreatorID\x18\x02 \x01(\r\"\x95\x01\n\x04Note\x12\x0b\n\x03nid\x18\x01 \x01(\r\x12\x11\n\tcreatorID\x18\x02 \x01(\r\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x11\n\tisVisible\x18\x05 \x01(\x08\x12\x15\n\risHighlighted\x18\x06 \x01(\x08\x12\r\n\x05\x63olor\x18\x07 \x01(\t\x12\x14\n\x0c\x63reationDate\x18\x08 \x01(\t\"0\n\x0eNoteIdentifier\x12\x0b\n\x03nid\x18\x01 \x01(\r\x12\x11\n\tcreatorID\x18\x02 \x01(\r\":\n\x07Profile\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x63reationDate\x18\x03 \x01(\t\"!\n\x03Tag\x12\x0c\n\x04taid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\'\n\nNoteTagRel\x12\x0b\n\x03nid\x18\x01 \x01(\r\x12\x0c\n\x04taid\x18\x02 \x01(\r\"\x07\n\x05\x45mpty2\x86\x05\n\x04\x44oDo\x12/\n\nInsertToDo\x12\n.grpc.ToDo\x1a\x15.grpc.SuccessResponse\x12/\n\nUpdateToDo\x12\n.grpc.ToDo\x1a\x15.grpc.SuccessResponse\x12\x39\n\nDeleteToDo\x12\x14.grpc.ToDoIdentifier\x1a\x15.grpc.SuccessResponse\x12/\n\nInsertNote\x12\n.grpc.Note\x1a\x15.grpc.SuccessResponse\x12/\n\nUpdateNote\x12\n.grpc.Note\x1a\x15.grpc.SuccessResponse\x12\x39\n\nDeleteNote\x12\x14.grpc.NoteIdentifier\x1a\x15.grpc.SuccessResponse\x12\x35\n\rInsertProfile\x12\r.grpc.Profile\x1a\x15.grpc.SuccessResponse\x12\x35\n\rDeleteProfile\x12\r.grpc.Profile\x1a\x15.grpc.SuccessResponse\x12-\n\tInsertTag\x12\t.grpc.Tag\x1a\x15.grpc.SuccessResponse\x12-\n\tDeleteTag\x12\t.grpc.Tag\x1a\x15.grpc.SuccessResponse\x12;\n\x10InsertNoteTagRel\x12\x10.grpc.NoteTagRel\x1a\x15.grpc.SuccessResponse\x12;\n\x10\x44\x65leteNoteTagRel\x12\x10.grpc.NoteTagRel\x1a\x15.grpc.SuccessResponseb\x06proto3'
)




_SUCCESSRESPONSE = _descriptor.Descriptor(
  name='SuccessResponse',
  full_name='grpc.SuccessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc.SuccessResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=29,
  serialized_end=63,
)


_TODO = _descriptor.Descriptor(
  name='ToDo',
  full_name='grpc.ToDo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='grpc.ToDo.tid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creatorID', full_name='grpc.ToDo.creatorID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='grpc.ToDo.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isDone', full_name='grpc.ToDo.isDone', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='grpc.ToDo.color', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=148,
)


_TODOIDENTIFIER = _descriptor.Descriptor(
  name='ToDoIdentifier',
  full_name='grpc.ToDoIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='grpc.ToDoIdentifier.tid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creatorID', full_name='grpc.ToDoIdentifier.creatorID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=150,
  serialized_end=198,
)


_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='grpc.Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nid', full_name='grpc.Note.nid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creatorID', full_name='grpc.Note.creatorID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='grpc.Note.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='grpc.Note.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isVisible', full_name='grpc.Note.isVisible', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isHighlighted', full_name='grpc.Note.isHighlighted', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='grpc.Note.color', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creationDate', full_name='grpc.Note.creationDate', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=201,
  serialized_end=350,
)


_NOTEIDENTIFIER = _descriptor.Descriptor(
  name='NoteIdentifier',
  full_name='grpc.NoteIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nid', full_name='grpc.NoteIdentifier.nid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creatorID', full_name='grpc.NoteIdentifier.creatorID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=352,
  serialized_end=400,
)


_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='grpc.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='grpc.Profile.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc.Profile.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creationDate', full_name='grpc.Profile.creationDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=402,
  serialized_end=460,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='grpc.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='taid', full_name='grpc.Tag.taid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc.Tag.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=462,
  serialized_end=495,
)


_NOTETAGREL = _descriptor.Descriptor(
  name='NoteTagRel',
  full_name='grpc.NoteTagRel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nid', full_name='grpc.NoteTagRel.nid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='taid', full_name='grpc.NoteTagRel.taid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=497,
  serialized_end=536,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=538,
  serialized_end=545,
)

DESCRIPTOR.message_types_by_name['SuccessResponse'] = _SUCCESSRESPONSE
DESCRIPTOR.message_types_by_name['ToDo'] = _TODO
DESCRIPTOR.message_types_by_name['ToDoIdentifier'] = _TODOIDENTIFIER
DESCRIPTOR.message_types_by_name['Note'] = _NOTE
DESCRIPTOR.message_types_by_name['NoteIdentifier'] = _NOTEIDENTIFIER
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['NoteTagRel'] = _NOTETAGREL
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SuccessResponse = _reflection.GeneratedProtocolMessageType('SuccessResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESSRESPONSE,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.SuccessResponse)
  })
_sym_db.RegisterMessage(SuccessResponse)

ToDo = _reflection.GeneratedProtocolMessageType('ToDo', (_message.Message,), {
  'DESCRIPTOR' : _TODO,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ToDo)
  })
_sym_db.RegisterMessage(ToDo)

ToDoIdentifier = _reflection.GeneratedProtocolMessageType('ToDoIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _TODOIDENTIFIER,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ToDoIdentifier)
  })
_sym_db.RegisterMessage(ToDoIdentifier)

Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), {
  'DESCRIPTOR' : _NOTE,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Note)
  })
_sym_db.RegisterMessage(Note)

NoteIdentifier = _reflection.GeneratedProtocolMessageType('NoteIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _NOTEIDENTIFIER,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.NoteIdentifier)
  })
_sym_db.RegisterMessage(NoteIdentifier)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {
  'DESCRIPTOR' : _PROFILE,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Profile)
  })
_sym_db.RegisterMessage(Profile)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Tag)
  })
_sym_db.RegisterMessage(Tag)

NoteTagRel = _reflection.GeneratedProtocolMessageType('NoteTagRel', (_message.Message,), {
  'DESCRIPTOR' : _NOTETAGREL,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.NoteTagRel)
  })
_sym_db.RegisterMessage(NoteTagRel)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'dodo_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Empty)
  })
_sym_db.RegisterMessage(Empty)



_DODO = _descriptor.ServiceDescriptor(
  name='DoDo',
  full_name='grpc.DoDo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=548,
  serialized_end=1194,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsertToDo',
    full_name='grpc.DoDo.InsertToDo',
    index=0,
    containing_service=None,
    input_type=_TODO,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateToDo',
    full_name='grpc.DoDo.UpdateToDo',
    index=1,
    containing_service=None,
    input_type=_TODO,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteToDo',
    full_name='grpc.DoDo.DeleteToDo',
    index=2,
    containing_service=None,
    input_type=_TODOIDENTIFIER,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertNote',
    full_name='grpc.DoDo.InsertNote',
    index=3,
    containing_service=None,
    input_type=_NOTE,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateNote',
    full_name='grpc.DoDo.UpdateNote',
    index=4,
    containing_service=None,
    input_type=_NOTE,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteNote',
    full_name='grpc.DoDo.DeleteNote',
    index=5,
    containing_service=None,
    input_type=_NOTEIDENTIFIER,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertProfile',
    full_name='grpc.DoDo.InsertProfile',
    index=6,
    containing_service=None,
    input_type=_PROFILE,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteProfile',
    full_name='grpc.DoDo.DeleteProfile',
    index=7,
    containing_service=None,
    input_type=_PROFILE,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertTag',
    full_name='grpc.DoDo.InsertTag',
    index=8,
    containing_service=None,
    input_type=_TAG,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTag',
    full_name='grpc.DoDo.DeleteTag',
    index=9,
    containing_service=None,
    input_type=_TAG,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsertNoteTagRel',
    full_name='grpc.DoDo.InsertNoteTagRel',
    index=10,
    containing_service=None,
    input_type=_NOTETAGREL,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteNoteTagRel',
    full_name='grpc.DoDo.DeleteNoteTagRel',
    index=11,
    containing_service=None,
    input_type=_NOTETAGREL,
    output_type=_SUCCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DODO)

DESCRIPTOR.services_by_name['DoDo'] = _DODO

# @@protoc_insertion_point(module_scope)
