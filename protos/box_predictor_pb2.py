# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/box_predictor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import hyperparams_pb2 as protos_dot_hyperparams__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/box_predictor.proto',
  package='protos',
  syntax='proto2',
  serialized_pb=_b('\n\x1aprotos/box_predictor.proto\x12\x06protos\x1a\x18protos/hyperparams.proto\"\xc3\x02\n\x0c\x42oxPredictor\x12H\n\x1b\x63onvolutional_box_predictor\x18\x01 \x01(\x0b\x32!.protos.ConvolutionalBoxPredictorH\x00\x12?\n\x17mask_rcnn_box_predictor\x18\x02 \x01(\x0b\x32\x1c.protos.MaskRCNNBoxPredictorH\x00\x12\x36\n\x12rfcn_box_predictor\x18\x03 \x01(\x0b\x32\x18.protos.RfcnBoxPredictorH\x00\x12Y\n$oriented_convolutional_box_predictor\x18\x04 \x01(\x0b\x32).protos.OrientedConvolutionalBoxPredictorH\x00\x42\x15\n\x13\x62ox_predictor_oneof\"\xba\x02\n\x19\x43onvolutionalBoxPredictor\x12-\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32\x13.protos.Hyperparams\x12\x14\n\tmin_depth\x18\x02 \x01(\x05:\x01\x30\x12\x14\n\tmax_depth\x18\x03 \x01(\x05:\x01\x30\x12&\n\x1bnum_layers_before_predictor\x18\x04 \x01(\x05:\x01\x30\x12\x19\n\x0buse_dropout\x18\x05 \x01(\x08:\x04true\x12%\n\x18\x64ropout_keep_probability\x18\x06 \x01(\x02:\x03\x30.8\x12\x16\n\x0bkernel_size\x18\x07 \x01(\x05:\x01\x31\x12\x18\n\rbox_code_size\x18\x08 \x01(\x05:\x01\x34\x12&\n\x17\x61pply_sigmoid_to_scores\x18\t \x01(\x08:\x05\x66\x61lse\"\xe5\x02\n!OrientedConvolutionalBoxPredictor\x12-\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32\x13.protos.Hyperparams\x12\x14\n\tmin_depth\x18\x02 \x01(\x05:\x01\x30\x12\x14\n\tmax_depth\x18\x03 \x01(\x05:\x01\x30\x12&\n\x1bnum_layers_before_predictor\x18\x04 \x01(\x05:\x01\x30\x12\x19\n\x0buse_dropout\x18\x05 \x01(\x08:\x04true\x12%\n\x18\x64ropout_keep_probability\x18\x06 \x01(\x02:\x03\x30.8\x12\x16\n\x0bkernel_size\x18\x07 \x01(\x05:\x01\x31\x12\x18\n\rbox_code_size\x18\x08 \x01(\x05:\x01\x34\x12&\n\x17\x61pply_sigmoid_to_scores\x18\t \x01(\x08:\x05\x66\x61lse\x12!\n\x16oriented_box_code_size\x18\n \x01(\x05:\x01\x38\"\xc1\x02\n\x14MaskRCNNBoxPredictor\x12+\n\x0e\x66\x63_hyperparams\x18\x01 \x01(\x0b\x32\x13.protos.Hyperparams\x12\x1a\n\x0buse_dropout\x18\x02 \x01(\x08:\x05\x66\x61lse\x12%\n\x18\x64ropout_keep_probability\x18\x03 \x01(\x02:\x03\x30.5\x12\x18\n\rbox_code_size\x18\x04 \x01(\x05:\x01\x34\x12-\n\x10\x63onv_hyperparams\x18\x05 \x01(\x0b\x32\x13.protos.Hyperparams\x12%\n\x16predict_instance_masks\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\'\n\x1amask_prediction_conv_depth\x18\x07 \x01(\x05:\x03\x32\x35\x36\x12 \n\x11predict_keypoints\x18\x08 \x01(\x08:\x05\x66\x61lse\"\xe8\x01\n\x10RfcnBoxPredictor\x12-\n\x10\x63onv_hyperparams\x18\x01 \x01(\x0b\x32\x13.protos.Hyperparams\x12\"\n\x17num_spatial_bins_height\x18\x02 \x01(\x05:\x01\x33\x12!\n\x16num_spatial_bins_width\x18\x03 \x01(\x05:\x01\x33\x12\x13\n\x05\x64\x65pth\x18\x04 \x01(\x05:\x04\x31\x30\x32\x34\x12\x18\n\rbox_code_size\x18\x05 \x01(\x05:\x01\x34\x12\x17\n\x0b\x63rop_height\x18\x06 \x01(\x05:\x02\x31\x32\x12\x16\n\ncrop_width\x18\x07 \x01(\x05:\x02\x31\x32')
  ,
  dependencies=[protos_dot_hyperparams__pb2.DESCRIPTOR,])




_BOXPREDICTOR = _descriptor.Descriptor(
  name='BoxPredictor',
  full_name='protos.BoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='convolutional_box_predictor', full_name='protos.BoxPredictor.convolutional_box_predictor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_rcnn_box_predictor', full_name='protos.BoxPredictor.mask_rcnn_box_predictor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rfcn_box_predictor', full_name='protos.BoxPredictor.rfcn_box_predictor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oriented_convolutional_box_predictor', full_name='protos.BoxPredictor.oriented_convolutional_box_predictor', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='box_predictor_oneof', full_name='protos.BoxPredictor.box_predictor_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=65,
  serialized_end=388,
)


_CONVOLUTIONALBOXPREDICTOR = _descriptor.Descriptor(
  name='ConvolutionalBoxPredictor',
  full_name='protos.ConvolutionalBoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='protos.ConvolutionalBoxPredictor.conv_hyperparams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_depth', full_name='protos.ConvolutionalBoxPredictor.min_depth', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_depth', full_name='protos.ConvolutionalBoxPredictor.max_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_layers_before_predictor', full_name='protos.ConvolutionalBoxPredictor.num_layers_before_predictor', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_dropout', full_name='protos.ConvolutionalBoxPredictor.use_dropout', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout_keep_probability', full_name='protos.ConvolutionalBoxPredictor.dropout_keep_probability', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.8),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernel_size', full_name='protos.ConvolutionalBoxPredictor.kernel_size', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_code_size', full_name='protos.ConvolutionalBoxPredictor.box_code_size', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply_sigmoid_to_scores', full_name='protos.ConvolutionalBoxPredictor.apply_sigmoid_to_scores', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=705,
)


_ORIENTEDCONVOLUTIONALBOXPREDICTOR = _descriptor.Descriptor(
  name='OrientedConvolutionalBoxPredictor',
  full_name='protos.OrientedConvolutionalBoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='protos.OrientedConvolutionalBoxPredictor.conv_hyperparams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_depth', full_name='protos.OrientedConvolutionalBoxPredictor.min_depth', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_depth', full_name='protos.OrientedConvolutionalBoxPredictor.max_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_layers_before_predictor', full_name='protos.OrientedConvolutionalBoxPredictor.num_layers_before_predictor', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_dropout', full_name='protos.OrientedConvolutionalBoxPredictor.use_dropout', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout_keep_probability', full_name='protos.OrientedConvolutionalBoxPredictor.dropout_keep_probability', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.8),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernel_size', full_name='protos.OrientedConvolutionalBoxPredictor.kernel_size', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_code_size', full_name='protos.OrientedConvolutionalBoxPredictor.box_code_size', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply_sigmoid_to_scores', full_name='protos.OrientedConvolutionalBoxPredictor.apply_sigmoid_to_scores', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oriented_box_code_size', full_name='protos.OrientedConvolutionalBoxPredictor.oriented_box_code_size', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=708,
  serialized_end=1065,
)


_MASKRCNNBOXPREDICTOR = _descriptor.Descriptor(
  name='MaskRCNNBoxPredictor',
  full_name='protos.MaskRCNNBoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fc_hyperparams', full_name='protos.MaskRCNNBoxPredictor.fc_hyperparams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_dropout', full_name='protos.MaskRCNNBoxPredictor.use_dropout', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout_keep_probability', full_name='protos.MaskRCNNBoxPredictor.dropout_keep_probability', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_code_size', full_name='protos.MaskRCNNBoxPredictor.box_code_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='protos.MaskRCNNBoxPredictor.conv_hyperparams', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_instance_masks', full_name='protos.MaskRCNNBoxPredictor.predict_instance_masks', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_prediction_conv_depth', full_name='protos.MaskRCNNBoxPredictor.mask_prediction_conv_depth', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_keypoints', full_name='protos.MaskRCNNBoxPredictor.predict_keypoints', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1068,
  serialized_end=1389,
)


_RFCNBOXPREDICTOR = _descriptor.Descriptor(
  name='RfcnBoxPredictor',
  full_name='protos.RfcnBoxPredictor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv_hyperparams', full_name='protos.RfcnBoxPredictor.conv_hyperparams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_spatial_bins_height', full_name='protos.RfcnBoxPredictor.num_spatial_bins_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_spatial_bins_width', full_name='protos.RfcnBoxPredictor.num_spatial_bins_width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depth', full_name='protos.RfcnBoxPredictor.depth', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1024,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_code_size', full_name='protos.RfcnBoxPredictor.box_code_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crop_height', full_name='protos.RfcnBoxPredictor.crop_height', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=12,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crop_width', full_name='protos.RfcnBoxPredictor.crop_width', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=12,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1392,
  serialized_end=1624,
)

_BOXPREDICTOR.fields_by_name['convolutional_box_predictor'].message_type = _CONVOLUTIONALBOXPREDICTOR
_BOXPREDICTOR.fields_by_name['mask_rcnn_box_predictor'].message_type = _MASKRCNNBOXPREDICTOR
_BOXPREDICTOR.fields_by_name['rfcn_box_predictor'].message_type = _RFCNBOXPREDICTOR
_BOXPREDICTOR.fields_by_name['oriented_convolutional_box_predictor'].message_type = _ORIENTEDCONVOLUTIONALBOXPREDICTOR
_BOXPREDICTOR.oneofs_by_name['box_predictor_oneof'].fields.append(
  _BOXPREDICTOR.fields_by_name['convolutional_box_predictor'])
_BOXPREDICTOR.fields_by_name['convolutional_box_predictor'].containing_oneof = _BOXPREDICTOR.oneofs_by_name['box_predictor_oneof']
_BOXPREDICTOR.oneofs_by_name['box_predictor_oneof'].fields.append(
  _BOXPREDICTOR.fields_by_name['mask_rcnn_box_predictor'])
_BOXPREDICTOR.fields_by_name['mask_rcnn_box_predictor'].containing_oneof = _BOXPREDICTOR.oneofs_by_name['box_predictor_oneof']
_BOXPREDICTOR.oneofs_by_name['box_predictor_oneof'].fields.append(
  _BOXPREDICTOR.fields_by_name['rfcn_box_predictor'])
_BOXPREDICTOR.fields_by_name['rfcn_box_predictor'].containing_oneof = _BOXPREDICTOR.oneofs_by_name['box_predictor_oneof']
_BOXPREDICTOR.oneofs_by_name['box_predictor_oneof'].fields.append(
  _BOXPREDICTOR.fields_by_name['oriented_convolutional_box_predictor'])
_BOXPREDICTOR.fields_by_name['oriented_convolutional_box_predictor'].containing_oneof = _BOXPREDICTOR.oneofs_by_name['box_predictor_oneof']
_CONVOLUTIONALBOXPREDICTOR.fields_by_name['conv_hyperparams'].message_type = protos_dot_hyperparams__pb2._HYPERPARAMS
_ORIENTEDCONVOLUTIONALBOXPREDICTOR.fields_by_name['conv_hyperparams'].message_type = protos_dot_hyperparams__pb2._HYPERPARAMS
_MASKRCNNBOXPREDICTOR.fields_by_name['fc_hyperparams'].message_type = protos_dot_hyperparams__pb2._HYPERPARAMS
_MASKRCNNBOXPREDICTOR.fields_by_name['conv_hyperparams'].message_type = protos_dot_hyperparams__pb2._HYPERPARAMS
_RFCNBOXPREDICTOR.fields_by_name['conv_hyperparams'].message_type = protos_dot_hyperparams__pb2._HYPERPARAMS
DESCRIPTOR.message_types_by_name['BoxPredictor'] = _BOXPREDICTOR
DESCRIPTOR.message_types_by_name['ConvolutionalBoxPredictor'] = _CONVOLUTIONALBOXPREDICTOR
DESCRIPTOR.message_types_by_name['OrientedConvolutionalBoxPredictor'] = _ORIENTEDCONVOLUTIONALBOXPREDICTOR
DESCRIPTOR.message_types_by_name['MaskRCNNBoxPredictor'] = _MASKRCNNBOXPREDICTOR
DESCRIPTOR.message_types_by_name['RfcnBoxPredictor'] = _RFCNBOXPREDICTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoxPredictor = _reflection.GeneratedProtocolMessageType('BoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _BOXPREDICTOR,
  __module__ = 'protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:protos.BoxPredictor)
  ))
_sym_db.RegisterMessage(BoxPredictor)

ConvolutionalBoxPredictor = _reflection.GeneratedProtocolMessageType('ConvolutionalBoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _CONVOLUTIONALBOXPREDICTOR,
  __module__ = 'protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:protos.ConvolutionalBoxPredictor)
  ))
_sym_db.RegisterMessage(ConvolutionalBoxPredictor)

OrientedConvolutionalBoxPredictor = _reflection.GeneratedProtocolMessageType('OrientedConvolutionalBoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _ORIENTEDCONVOLUTIONALBOXPREDICTOR,
  __module__ = 'protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:protos.OrientedConvolutionalBoxPredictor)
  ))
_sym_db.RegisterMessage(OrientedConvolutionalBoxPredictor)

MaskRCNNBoxPredictor = _reflection.GeneratedProtocolMessageType('MaskRCNNBoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _MASKRCNNBOXPREDICTOR,
  __module__ = 'protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:protos.MaskRCNNBoxPredictor)
  ))
_sym_db.RegisterMessage(MaskRCNNBoxPredictor)

RfcnBoxPredictor = _reflection.GeneratedProtocolMessageType('RfcnBoxPredictor', (_message.Message,), dict(
  DESCRIPTOR = _RFCNBOXPREDICTOR,
  __module__ = 'protos.box_predictor_pb2'
  # @@protoc_insertion_point(class_scope:protos.RfcnBoxPredictor)
  ))
_sym_db.RegisterMessage(RfcnBoxPredictor)


# @@protoc_insertion_point(module_scope)
