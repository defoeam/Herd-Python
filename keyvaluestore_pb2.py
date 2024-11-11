# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: keyvaluestore.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'keyvaluestore.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13keyvaluestore.proto\x12\rkeyvaluestore\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x10\n\x0eGetKeysRequest\"\x1f\n\x0fGetKeysResponse\x12\x0c\n\x04keys\x18\x01 \x03(\t\"\x12\n\x10GetValuesRequest\"#\n\x11GetValuesResponse\x12\x0e\n\x06values\x18\x01 \x03(\x0c\"\x0f\n\rGetAllRequest\"8\n\x0eGetAllResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.keyvaluestore.KeyValue\"(\n\nSetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"4\n\x0bSetResponse\x12%\n\x04item\x18\x01 \x01(\x0b\x32\x17.keyvaluestore.KeyValue\"\x1c\n\rDeleteRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"?\n\x0e\x44\x65leteResponse\x12-\n\x0c\x64\x65leted_item\x18\x01 \x01(\x0b\x32\x17.keyvaluestore.KeyValue\"\x12\n\x10\x44\x65leteAllRequest\"\x13\n\x11\x44\x65leteAllResponse2\x82\x04\n\x0fKeyValueService\x12\x39\n\x03Get\x12\x19.keyvaluestore.GetRequest\x1a\x17.keyvaluestore.KeyValue\x12\x45\n\x06GetAll\x12\x1c.keyvaluestore.GetAllRequest\x1a\x1d.keyvaluestore.GetAllResponse\x12H\n\x07GetKeys\x12\x1d.keyvaluestore.GetKeysRequest\x1a\x1e.keyvaluestore.GetKeysResponse\x12N\n\tGetValues\x12\x1f.keyvaluestore.GetValuesRequest\x1a .keyvaluestore.GetValuesResponse\x12<\n\x03Set\x12\x19.keyvaluestore.SetRequest\x1a\x1a.keyvaluestore.SetResponse\x12\x45\n\x06\x44\x65lete\x12\x1c.keyvaluestore.DeleteRequest\x1a\x1d.keyvaluestore.DeleteResponse\x12N\n\tDeleteAll\x12\x1f.keyvaluestore.DeleteAllRequest\x1a .keyvaluestore.DeleteAllResponseB\x1fZ\x1dgithub.com/defoeam/herd/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'keyvaluestore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035github.com/defoeam/herd/proto'
  _globals['_KEYVALUE']._serialized_start=38
  _globals['_KEYVALUE']._serialized_end=76
  _globals['_GETREQUEST']._serialized_start=78
  _globals['_GETREQUEST']._serialized_end=103
  _globals['_GETKEYSREQUEST']._serialized_start=105
  _globals['_GETKEYSREQUEST']._serialized_end=121
  _globals['_GETKEYSRESPONSE']._serialized_start=123
  _globals['_GETKEYSRESPONSE']._serialized_end=154
  _globals['_GETVALUESREQUEST']._serialized_start=156
  _globals['_GETVALUESREQUEST']._serialized_end=174
  _globals['_GETVALUESRESPONSE']._serialized_start=176
  _globals['_GETVALUESRESPONSE']._serialized_end=211
  _globals['_GETALLREQUEST']._serialized_start=213
  _globals['_GETALLREQUEST']._serialized_end=228
  _globals['_GETALLRESPONSE']._serialized_start=230
  _globals['_GETALLRESPONSE']._serialized_end=286
  _globals['_SETREQUEST']._serialized_start=288
  _globals['_SETREQUEST']._serialized_end=328
  _globals['_SETRESPONSE']._serialized_start=330
  _globals['_SETRESPONSE']._serialized_end=382
  _globals['_DELETEREQUEST']._serialized_start=384
  _globals['_DELETEREQUEST']._serialized_end=412
  _globals['_DELETERESPONSE']._serialized_start=414
  _globals['_DELETERESPONSE']._serialized_end=477
  _globals['_DELETEALLREQUEST']._serialized_start=479
  _globals['_DELETEALLREQUEST']._serialized_end=497
  _globals['_DELETEALLRESPONSE']._serialized_start=499
  _globals['_DELETEALLRESPONSE']._serialized_end=518
  _globals['_KEYVALUESERVICE']._serialized_start=521
  _globals['_KEYVALUESERVICE']._serialized_end=1035
# @@protoc_insertion_point(module_scope)
