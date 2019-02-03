"""Something.hello has a signature, incompatible with interface
"""

import zope.interface


class ISomething(zope.interface.Interface):
    def hello(x: int, y: str) -> None:
        pass


@zope.interface.implementer(ISomething)
class Something(object):
    def hello(self, x: int, y: int) -> None:
        print(f"X: {x}, Y: {y}")


"""
<output>
incompatible_signature.py:12: error: __main__.Something is not a valid implementation of __main__.ISomething
incompatible_signature.py:12: note: Following member(s) of "Something" have conflicts:
incompatible_signature.py:12: note:     Expected:
incompatible_signature.py:12: note:         def hello(self, x: int, y: str) -> None
incompatible_signature.py:12: note:     Got:
incompatible_signature.py:12: note:         def hello(self, x: int, y: int) -> None
</output>
"""
