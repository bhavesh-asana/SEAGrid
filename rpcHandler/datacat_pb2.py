# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datacat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdatacat.proto\x12\x1c\x63om.smiles.server.controller\x1a\x1cgoogle/protobuf/struct.proto\"\xa1\x02\n\x07\x45xecEnv\x12\x13\n\x06\x43\x61lcBy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rJobCPURunTime\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x18\n\x0b\x43\x61lcMachine\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1d\n\x10\x41\x63tualJobRunTime\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x14\n\x07\x46inTime\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x13\n\x06Memory\x18\x06 \x01(\x05H\x05\x88\x01\x01\x12\x18\n\x0bNProcShared\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\t\n\x07_CalcByB\x10\n\x0e_JobCPURunTimeB\x0e\n\x0c_CalcMachineB\x13\n\x11_ActualJobRunTimeB\n\n\x08_FinTimeB\t\n\x07_MemoryB\x0e\n\x0c_NProcShared\"\xe1\x01\n\x0e\x43\x61lcProperties\x12\x11\n\x05Homos\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x13\n\x06\x45nergy\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x44ipole\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x0f\n\x02HF\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\'\n\x1bMaximumGradientDistribution\x18\x05 \x03(\x01\x42\x02\x10\x01\x12#\n\x17RMSGradientDistribution\x18\x06 \x03(\x01\x42\x02\x10\x01\x12\x16\n\nIterations\x18\x07 \x03(\x01\x42\x02\x10\x01\x42\t\n\x07_EnergyB\t\n\x07_DipoleB\x05\n\x03_HF\"I\n\x13\x46MStructuralFormats\x12\x10\n\x03SDF\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03PDB\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x06\n\x04_SDFB\x06\n\x04_PDB\"\xd3\x01\n\x03Mol\x12\x14\n\x07\x46ormula\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05NAtom\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x19\n\x0cMultiplicity\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06\x43harge\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x13\n\x06OrbSym\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07\x45lecSym\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\n\n\x08_FormulaB\x08\n\x06_NAtomB\x0f\n\r_MultiplicityB\t\n\x07_ChargeB\t\n\x07_OrbSymB\n\n\x08_ElecSym\"\xad\x02\n\tCalcField\x12\x16\n\tJobStatus\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x42\x61sis\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03NMO\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x15\n\x08Keywords\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x13\n\x06NBasis\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x16\n\nMoEnergies\x18\x06 \x03(\x01\x42\x02\x10\x01\x12\x14\n\x07Package\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x15\n\x08\x43\x61lcType\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\x14\n\x07Methods\x18\t \x01(\tH\x07\x88\x01\x01\x42\x0c\n\n_JobStatusB\x08\n\x06_BasisB\x06\n\x04_NMOB\x0b\n\t_KeywordsB\t\n\x07_NBasisB\n\n\x08_PackageB\x0b\n\t_CalcTypeB\n\n\x08_Methods\"\xa6\x01\n\x10IdentifiersField\x12\x15\n\x08InChiKey\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0f\x43\x61nonicalSMILES\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05InChi\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06SMILES\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x0b\n\t_InChiKeyB\x12\n\x10_CanonicalSMILESB\x08\n\x06_InChiB\t\n\x07_SMILES\"\xb0\x02\n\nFilesField\x12\x17\n\nSMILESFile\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10SDFStructureFile\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\x12GaussianOutputFile\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1e\n\x11GaussianInputFile\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1d\n\x10PDBStructureFile\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x16\n\tInChIFile\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\r\n\x0b_SMILESFileB\x13\n\x11_SDFStructureFileB\x15\n\x13_GaussianOutputFileB\x14\n\x12_GaussianInputFileB\x13\n\x11_PDBStructureFileB\x0c\n\n_InChIFile\"y\n\x1bInputFileConfigurationField\x12\x1a\n\rLink0Commands\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rRouteCommands\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x10\n\x0e_Link0CommandsB\x10\n\x0e_RouteCommands\"\x82\x06\n\x08GridChem\x12\x18\n\x0bProjectName\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0e\x45xperimentName\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08Username\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x0f\n\x02Id\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0bIndexedTime\x18\n \x01(\x05H\x04\x88\x01\x01\x12\x43\n\x14\x45xecutionEnvironment\x18\x05 \x01(\x0b\x32%.com.smiles.server.controller.ExecEnv\x12J\n\x14\x43\x61lculatedProperties\x18\x06 \x01(\x0b\x32,.com.smiles.server.controller.CalcProperties\x12Y\n\x1e\x46inalMoleculeStructuralFormats\x18\x07 \x01(\x0b\x32\x31.com.smiles.server.controller.FMStructuralFormats\x12\x33\n\x08Molecule\x18\x08 \x01(\x0b\x32!.com.smiles.server.controller.Mol\x12<\n\x0b\x43\x61lculation\x18\t \x01(\x0b\x32\'.com.smiles.server.controller.CalcField\x12\x43\n\x0bIdentifiers\x18\x0b \x01(\x0b\x32..com.smiles.server.controller.IdentifiersField\x12\x37\n\x05\x46iles\x18\x0c \x01(\x0b\x32(.com.smiles.server.controller.FilesField\x12Y\n\x16InputFileConfiguration\x18\r \x01(\x0b\x32\x39.com.smiles.server.controller.InputFileConfigurationFieldB\x0e\n\x0c_ProjectNameB\x11\n\x0f_ExperimentNameB\x0b\n\t_UsernameB\x05\n\x03_IdB\x0e\n\x0c_IndexedTime\"\x14\n\x12GetGridChemRequest2i\n\x0fGridChemService\x12V\n\x07GetData\x12\x30.com.smiles.server.controller.GetGridChemRequest\x1a\x17.google.protobuf.Struct\"\x00\x62\x06proto3')



_EXECENV = DESCRIPTOR.message_types_by_name['ExecEnv']
_CALCPROPERTIES = DESCRIPTOR.message_types_by_name['CalcProperties']
_FMSTRUCTURALFORMATS = DESCRIPTOR.message_types_by_name['FMStructuralFormats']
_MOL = DESCRIPTOR.message_types_by_name['Mol']
_CALCFIELD = DESCRIPTOR.message_types_by_name['CalcField']
_IDENTIFIERSFIELD = DESCRIPTOR.message_types_by_name['IdentifiersField']
_FILESFIELD = DESCRIPTOR.message_types_by_name['FilesField']
_INPUTFILECONFIGURATIONFIELD = DESCRIPTOR.message_types_by_name['InputFileConfigurationField']
_GRIDCHEM = DESCRIPTOR.message_types_by_name['GridChem']
_GETGRIDCHEMREQUEST = DESCRIPTOR.message_types_by_name['GetGridChemRequest']
ExecEnv = _reflection.GeneratedProtocolMessageType('ExecEnv', (_message.Message,), {
  'DESCRIPTOR' : _EXECENV,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.ExecEnv)
  })
_sym_db.RegisterMessage(ExecEnv)

CalcProperties = _reflection.GeneratedProtocolMessageType('CalcProperties', (_message.Message,), {
  'DESCRIPTOR' : _CALCPROPERTIES,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.CalcProperties)
  })
_sym_db.RegisterMessage(CalcProperties)

FMStructuralFormats = _reflection.GeneratedProtocolMessageType('FMStructuralFormats', (_message.Message,), {
  'DESCRIPTOR' : _FMSTRUCTURALFORMATS,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.FMStructuralFormats)
  })
_sym_db.RegisterMessage(FMStructuralFormats)

Mol = _reflection.GeneratedProtocolMessageType('Mol', (_message.Message,), {
  'DESCRIPTOR' : _MOL,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.Mol)
  })
_sym_db.RegisterMessage(Mol)

CalcField = _reflection.GeneratedProtocolMessageType('CalcField', (_message.Message,), {
  'DESCRIPTOR' : _CALCFIELD,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.CalcField)
  })
_sym_db.RegisterMessage(CalcField)

IdentifiersField = _reflection.GeneratedProtocolMessageType('IdentifiersField', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIERSFIELD,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.IdentifiersField)
  })
_sym_db.RegisterMessage(IdentifiersField)

FilesField = _reflection.GeneratedProtocolMessageType('FilesField', (_message.Message,), {
  'DESCRIPTOR' : _FILESFIELD,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.FilesField)
  })
_sym_db.RegisterMessage(FilesField)

InputFileConfigurationField = _reflection.GeneratedProtocolMessageType('InputFileConfigurationField', (_message.Message,), {
  'DESCRIPTOR' : _INPUTFILECONFIGURATIONFIELD,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.InputFileConfigurationField)
  })
_sym_db.RegisterMessage(InputFileConfigurationField)

GridChem = _reflection.GeneratedProtocolMessageType('GridChem', (_message.Message,), {
  'DESCRIPTOR' : _GRIDCHEM,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.GridChem)
  })
_sym_db.RegisterMessage(GridChem)

GetGridChemRequest = _reflection.GeneratedProtocolMessageType('GetGridChemRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGRIDCHEMREQUEST,
  '__module__' : 'datacat_pb2'
  # @@protoc_insertion_point(class_scope:com.smiles.server.controller.GetGridChemRequest)
  })
_sym_db.RegisterMessage(GetGridChemRequest)

_GRIDCHEMSERVICE = DESCRIPTOR.services_by_name['GridChemService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CALCPROPERTIES.fields_by_name['Homos']._options = None
  _CALCPROPERTIES.fields_by_name['Homos']._serialized_options = b'\020\001'
  _CALCPROPERTIES.fields_by_name['MaximumGradientDistribution']._options = None
  _CALCPROPERTIES.fields_by_name['MaximumGradientDistribution']._serialized_options = b'\020\001'
  _CALCPROPERTIES.fields_by_name['RMSGradientDistribution']._options = None
  _CALCPROPERTIES.fields_by_name['RMSGradientDistribution']._serialized_options = b'\020\001'
  _CALCPROPERTIES.fields_by_name['Iterations']._options = None
  _CALCPROPERTIES.fields_by_name['Iterations']._serialized_options = b'\020\001'
  _CALCFIELD.fields_by_name['MoEnergies']._options = None
  _CALCFIELD.fields_by_name['MoEnergies']._serialized_options = b'\020\001'
  _EXECENV._serialized_start=78
  _EXECENV._serialized_end=367
  _CALCPROPERTIES._serialized_start=370
  _CALCPROPERTIES._serialized_end=595
  _FMSTRUCTURALFORMATS._serialized_start=597
  _FMSTRUCTURALFORMATS._serialized_end=670
  _MOL._serialized_start=673
  _MOL._serialized_end=884
  _CALCFIELD._serialized_start=887
  _CALCFIELD._serialized_end=1188
  _IDENTIFIERSFIELD._serialized_start=1191
  _IDENTIFIERSFIELD._serialized_end=1357
  _FILESFIELD._serialized_start=1360
  _FILESFIELD._serialized_end=1664
  _INPUTFILECONFIGURATIONFIELD._serialized_start=1666
  _INPUTFILECONFIGURATIONFIELD._serialized_end=1787
  _GRIDCHEM._serialized_start=1790
  _GRIDCHEM._serialized_end=2560
  _GETGRIDCHEMREQUEST._serialized_start=2562
  _GETGRIDCHEMREQUEST._serialized_end=2582
  _GRIDCHEMSERVICE._serialized_start=2584
  _GRIDCHEMSERVICE._serialized_end=2689
# @@protoc_insertion_point(module_scope)
