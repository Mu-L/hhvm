

#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import abc as _abc
import typing as _typing

_fbthrift_property = property

import enum as _enum


import folly.iobuf as _fbthrift_iobuf
import thrift.python.abstract_types as _fbthrift_python_abstract_types

class SerializedStruct(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def s(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def i(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def os(self) -> _typing.Optional[str]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def rs(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int, str, str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_types.SerializedStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.serialized_dep.types.SerializedStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "serialized_dep.ttypes.SerializedStruct": ...  # type: ignore
_fbthrift_SerializedStruct = SerializedStruct
class SerializedUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def s(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def i(self) -> int: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_types.SerializedUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.serialized_dep.types.SerializedUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "serialized_dep.ttypes.SerializedUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        s = 1
        i = 2

    FbThriftUnionFieldEnum.__name__ = "SerializedUnion"
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_value(self) -> _typing.Union[None, str, int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_field(self) -> FbThriftUnionFieldEnum: ...

_fbthrift_SerializedUnion = SerializedUnion
class SerializedError(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def msg(self) -> str: ...
    @_fbthrift_property
    def os(self) -> _typing.Optional[str]: ...
    @_fbthrift_property
    def rs(self) -> str: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str, str]]]: ...
    def _to_mutable_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedError": ...  # type: ignore
    def _to_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_types.SerializedError": ...  # type: ignore
    def _to_py3(self) -> "test.fixtures.python_capi.serialized_dep.types.SerializedError": ...  # type: ignore
    def _to_py_deprecated(self) -> "serialized_dep.ttypes.SerializedError": ...  # type: ignore
_fbthrift_SerializedError = SerializedError
class MarshalStruct(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def s(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def i(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def os(self) -> _typing.Optional[str]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def rs(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int, str, str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_mutable_types.MarshalStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_types.MarshalStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.serialized_dep.types.MarshalStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "serialized_dep.ttypes.MarshalStruct": ...  # type: ignore
_fbthrift_MarshalStruct = MarshalStruct
class MarshalUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def s(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def i(self) -> int: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_mutable_types.MarshalUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_types.MarshalUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "test.fixtures.python_capi.serialized_dep.types.MarshalUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "serialized_dep.ttypes.MarshalUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        s = 1
        i = 2

    FbThriftUnionFieldEnum.__name__ = "MarshalUnion"
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_value(self) -> _typing.Union[None, str, int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_field(self) -> FbThriftUnionFieldEnum: ...

_fbthrift_MarshalUnion = MarshalUnion
class MarshalError(_fbthrift_python_abstract_types.AbstractGeneratedError):
    @_fbthrift_property
    def msg(self) -> str: ...
    @_fbthrift_property
    def os(self) -> _typing.Optional[str]: ...
    @_fbthrift_property
    def rs(self) -> str: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str, str]]]: ...
    def _to_mutable_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_mutable_types.MarshalError": ...  # type: ignore
    def _to_python(self) -> "test.fixtures.python_capi.serialized_dep.thrift_types.MarshalError": ...  # type: ignore
    def _to_py3(self) -> "test.fixtures.python_capi.serialized_dep.types.MarshalError": ...  # type: ignore
    def _to_py_deprecated(self) -> "serialized_dep.ttypes.MarshalError": ...  # type: ignore
_fbthrift_MarshalError = MarshalError
