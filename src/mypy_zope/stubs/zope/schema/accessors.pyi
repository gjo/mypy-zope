# Stubs for zope.schema.accessors (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from zope.interface.interface import Method

class FieldReadAccessor(Method):
    def __provides__(self): ...
    __provides__: Any = ...
    field: Any = ...
    __doc__: Any = ...
    def __init__(self, field: Any) -> None: ...
    def getSignatureString(self): ...
    def getSignatureInfo(self): ...
    def get(self, object: Any): ...
    def query(self, object: Any, default: Optional[Any] = ...): ...
    def set(self, object: Any, value: Any) -> None: ...
    def __getattr__(self, name: Any): ...
    def bind(self, object: Any): ...

class FieldWriteAccessor(Method):
    field: Any = ...
    __doc__: Any = ...
    def __init__(self, field: Any) -> None: ...
    def getSignatureString(self): ...
    def getSignatureInfo(self): ...

def accessors(field: Any) -> None: ...
