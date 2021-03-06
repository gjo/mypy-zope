# Stubs for zope.schema._bootstrapfields (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import threading
from typing import Any, Optional
from zope.interface import Attribute
from zope.schema._bootstrapinterfaces import ValidationError

__docformat__: str

class _NotGiven: ...

class ValidatedProperty:
    def __init__(self, name: Any, check: Optional[Any] = ..., allow_none: bool = ...) -> None: ...
    def __set__(self, inst: Any, value: Any) -> None: ...
    def __get__(self, inst: Any, owner: Any): ...

class DefaultProperty(ValidatedProperty):
    def __get__(self, inst: Any, owner: Any): ...

def getFields(schema: Any): ...

class _DocStringHelpers:
    @staticmethod
    def docstring_to_lines(docstring: Any): ...
    @staticmethod
    def make_class_directive(kind: Any): ...
    @classmethod
    def make_field(cls, name: Any, value: Any): ...
    @classmethod
    def make_class_field(cls, name: Any, kind: Any): ...

class Field(Attribute):
    context: Any = ...
    missing_value: Any = ...
    order: int = ...
    default: Any = ...
    __name__: Any = ...
    interface: Any = ...
    title: Any = ...
    description: Any = ...
    required: Any = ...
    readonly: Any = ...
    constraint: Any = ...
    defaultFactory: Any = ...
    def __init__(self, title: str = ..., description: str = ..., __name__: str = ..., required: bool = ..., readonly: bool = ..., constraint: Optional[Any] = ..., default: Optional[Any] = ..., defaultFactory: Optional[Any] = ..., missing_value: Any = ...) -> None: ...
    def constraint(self, value: Any): ...
    def bind(self, context: Any): ...
    def validate(self, value: Any) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def get(self, object: Any): ...
    def query(self, object: Any, default: Optional[Any] = ...): ...
    def set(self, object: Any, value: Any) -> None: ...
    def getExtraDocLines(self): ...
    def getDoc(self): ...

class Container(Field): ...
class Iterable(Container): ...

class Orderable:
    min: Any = ...
    max: Any = ...
    default: Any = ...
    def __init__(self, min: Optional[Any] = ..., max: Optional[Any] = ..., default: Optional[Any] = ..., **kw: Any) -> None: ...

class MinMaxLen:
    min_length: int = ...
    max_length: Any = ...
    def __init__(self, min_length: int = ..., max_length: Optional[Any] = ..., **kw: Any) -> None: ...

class Text(MinMaxLen, Field):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def fromUnicode(self, str: Any): ...

class TextLine(Text):
    def constraint(self, value: Any): ...

class Password(TextLine):
    UNCHANGED_PASSWORD: Any = ...
    def set(self, context: Any, value: Any): ...
    def validate(self, value: Any): ...

class Bool(Field):
    def set(self, object: Any, value: Any) -> None: ...
    def fromUnicode(self, value: Any): ...
    def fromBytes(self, value: Any): ...

class InvalidNumberLiteral(ValueError, ValidationError): ...

class Number(Orderable, Field):
    def fromUnicode(self, value: Any): ...
    fromBytes: Any = ...
    def fromBytes(self, value: Any): ...

class Complex(Number): ...
class Real(Complex): ...
class Rational(Real): ...
class InvalidIntLiteral(ValueError, ValidationError): ...
class Integral(Rational): ...
class Int(Integral): ...

class _ObjectsBeingValidated(threading.local):
    ids_being_validated: Any = ...
    def __init__(self) -> None: ...

def get_schema_validation_errors(schema: Any, value: Any, _validating_objects: Any = ...): ...
def get_validation_errors(schema: Any, value: Any, validate_invariants: bool = ...): ...

class Object(Field):
    schema: Any = ...
    validate_invariants: Any = ...
    def __init__(self, schema: Any = ..., **kw: Any) -> None: ...
    def getExtraDocLines(self): ...
    def set(self, object: Any, value: Any) -> None: ...

class BeforeObjectAssignedEvent:
    object: Any = ...
    name: Any = ...
    context: Any = ...
    def __init__(self, object: Any, name: Any, context: Any) -> None: ...
