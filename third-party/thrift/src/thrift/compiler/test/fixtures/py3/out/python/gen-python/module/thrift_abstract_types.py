

#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import __static__

import abc as _abc
import typing as _typing

_fbthrift_property = property

import enum as _enum


import folly.iobuf as _fbthrift_iobuf
import fbcode.thrift.python.abstract_types as _fbthrift_python_abstract_types

from module.thrift_enums import (
    AnEnum,
    AnEnum as _fbthrift_AnEnum,
    _fbthrift_compatible_with_AnEnum,
    AnEnumRenamed,
    AnEnumRenamed as _fbthrift_AnEnumRenamed,
    _fbthrift_compatible_with_AnEnumRenamed,
    Flags,
    Flags as _fbthrift_Flags,
    _fbthrift_compatible_with_Flags,
)

class SimpleException(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def err_code(self) -> int: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int]]]: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.SimpleException": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.SimpleException": ...  # type: ignore
    def _to_py3(self) -> "module.types.SimpleException": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.SimpleException": ...  # type: ignore
_fbthrift_SimpleException = SimpleException
class OptionalRefStruct(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def optional_blob(self) -> _typing.Optional[_fbthrift_iobuf.IOBuf]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_fbthrift_iobuf.IOBuf]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.OptionalRefStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.OptionalRefStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.OptionalRefStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.OptionalRefStruct": ...  # type: ignore
_fbthrift_OptionalRefStruct = OptionalRefStruct
class SimpleStruct(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def is_on(self) -> bool: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def tiny_int(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def small_int(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def nice_sized_int(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def big_int(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def real(self) -> float: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def smaller_real(self) -> float: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def hidden_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def something(self) -> _typing.Mapping[int, int]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, int, int, int, float, float, int, _typing.Mapping[int, int]]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.SimpleStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.SimpleStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.SimpleStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.SimpleStruct": ...  # type: ignore
_fbthrift_SimpleStruct = SimpleStruct
class HiddenTypeFieldsStruct(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def field1(self) -> _fbthrift_SimpleStruct: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def field2(self) -> _typing.Sequence[_fbthrift_SimpleStruct]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def field3(self) -> _typing.Mapping[int, _fbthrift_SimpleStruct]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_fbthrift_SimpleStruct, _typing.Sequence[_fbthrift_SimpleStruct], _typing.Mapping[int, _fbthrift_SimpleStruct]]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.HiddenTypeFieldsStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.HiddenTypeFieldsStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.HiddenTypeFieldsStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.HiddenTypeFieldsStruct": ...  # type: ignore
_fbthrift_HiddenTypeFieldsStruct = HiddenTypeFieldsStruct
class AdaptedUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def best(self) -> int: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.AdaptedUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.AdaptedUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.AdaptedUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.AdaptedUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        best = 1

    FbThriftUnionFieldEnum.__name__ = "AdaptedUnion"
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_value(self) -> _typing.Union[None, int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_field(self) -> FbThriftUnionFieldEnum: ...

_fbthrift_AdaptedUnion = AdaptedUnion
class HiddenException(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def test(self) -> int: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int]]]: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.HiddenException": ...  # type: ignore
    def _to_python(self) -> "module.thrift_types.HiddenException": ...  # type: ignore
    def _to_py3(self) -> "module.types.HiddenException": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.HiddenException": ...  # type: ignore
_fbthrift_HiddenException = HiddenException
class ComplexStruct(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def structOne(self) -> _fbthrift_SimpleStruct: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def structTwo(self) -> _fbthrift_SimpleStruct: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def an_integer(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def name(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def an_enum(self) -> _fbthrift_AnEnum: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def some_bytes(self) -> bytes: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def sender(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def cdef_(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def bytes_with_cpp_type(self) -> bytes: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_fbthrift_SimpleStruct, _fbthrift_SimpleStruct, int, str, _fbthrift_AnEnum, bytes, str, str, bytes]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.ComplexStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.ComplexStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.ComplexStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.ComplexStruct": ...  # type: ignore
_fbthrift_ComplexStruct = ComplexStruct
class BinaryUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def iobuf_val(self) -> _fbthrift_iobuf.IOBuf: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.BinaryUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.BinaryUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.BinaryUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.BinaryUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        iobuf_val = 1

    FbThriftUnionFieldEnum.__name__ = "BinaryUnion"
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_value(self) -> _typing.Union[None, _fbthrift_iobuf.IOBuf]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_field(self) -> FbThriftUnionFieldEnum: ...

_fbthrift_BinaryUnion = BinaryUnion
class BinaryUnionStruct(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def u(self) -> _fbthrift_BinaryUnion: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_fbthrift_BinaryUnion]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.BinaryUnionStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.BinaryUnionStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.BinaryUnionStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.BinaryUnionStruct": ...  # type: ignore
_fbthrift_BinaryUnionStruct = BinaryUnionStruct
class CustomFields(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def bool_field(self) -> bool: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def integer_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def double_field(self) -> float: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def string_field(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def binary_field(self) -> bytes: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def list_field(self) -> _typing.Sequence[int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def set_field(self) -> _typing.AbstractSet[int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def map_field(self) -> _typing.Mapping[int, int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def struct_field(self) -> _fbthrift_SimpleStruct: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, float, str, bytes, _typing.Sequence[int], _typing.AbstractSet[int], _typing.Mapping[int, int], _fbthrift_SimpleStruct]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.CustomFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.CustomFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.CustomFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.CustomFields": ...  # type: ignore
_fbthrift_CustomFields = CustomFields
class CustomTypedefFields(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def bool_field(self) -> bool: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def integer_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def double_field(self) -> float: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def string_field(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def binary_field(self) -> bytes: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def list_field(self) -> _typing.Sequence[int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def set_field(self) -> _typing.AbstractSet[int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def map_field(self) -> _typing.Mapping[int, int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def struct_field(self) -> _fbthrift_SimpleStruct: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, float, str, bytes, _typing.Sequence[int], _typing.AbstractSet[int], _typing.Mapping[int, int], _fbthrift_SimpleStruct]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.CustomTypedefFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.CustomTypedefFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.CustomTypedefFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.CustomTypedefFields": ...  # type: ignore
_fbthrift_CustomTypedefFields = CustomTypedefFields
class AdaptedTypedefFields(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def bool_field(self) -> bool: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def integer_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def double_field(self) -> float: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def string_field(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def binary_field(self) -> bytes: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def list_field(self) -> _typing.Sequence[int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def set_field(self) -> _typing.AbstractSet[int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def map_field(self) -> _typing.Mapping[int, int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def struct_field(self) -> _fbthrift_SimpleStruct: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, float, str, bytes, _typing.Sequence[int], _typing.AbstractSet[int], _typing.Mapping[int, int], _fbthrift_SimpleStruct]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.AdaptedTypedefFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.AdaptedTypedefFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.AdaptedTypedefFields": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.AdaptedTypedefFields": ...  # type: ignore
_fbthrift_AdaptedTypedefFields = AdaptedTypedefFields

IOBufPtr = _fbthrift_iobuf.IOBuf
IOBuf = _fbthrift_iobuf.IOBuf
AdaptedTypeDef = _fbthrift_SimpleStruct
HiddenTypeDef = _fbthrift_SimpleStruct
ImplicitlyHiddenTypeDef = _fbthrift_AdaptedUnion
foo_bar = bytes
CustomBool = bool
CustomInteger = int
CustomDouble = float
CustomString = str
CustomBinary = bytes
CustomList = _typing.Sequence[int]
CustomSet = _typing.AbstractSet[int]
CustomMap = _typing.Mapping[int, int]
CustomStruct = _fbthrift_SimpleStruct
AdaptedBool = bool
AdaptedInteger = int
AdaptedDouble = float
AdaptedString = str
AdaptedBinary = bytes
AdaptedList = _typing.Sequence[int]
AdaptedSet = _typing.AbstractSet[int]
AdaptedMap = _typing.Mapping[int, int]
AdaptedStruct = _fbthrift_SimpleStruct
