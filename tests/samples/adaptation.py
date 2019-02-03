"""A simple valid interface declaration
"""
import zope.interface


class ISomething(zope.interface.Interface):
    def hello(x: int, y: str) -> None:
        pass

@zope.interface.implementer(ISomething)
class AbstractSomething(object):
    def thefunc(self) -> None:
        pass

@zope.interface.implementer(ISomething)
class ConcreteSomething(object):
    def hello(self, x: int, y: str) -> None:
        pass

class Context(object):
    pass

def main() -> None:
    ctx = Context()
    smth = ISomething(ctx)
    smth.hello(2, 3)  # Error: second argument is expected to be string

if __name__ == '__main__':
    main()

"""
<output>
adaptation.py:10: error: __main__.AbstractSomething is not a valid implementation of __main__.ISomething
adaptation.py:10: note: 'AbstractSomething' is missing following 'ISomething' protocol member:
adaptation.py:10: note:     hello
adaptation.py:26: error: Argument 2 to "hello" of "ISomething" has incompatible type "int"; expected "str"
</output>
"""
