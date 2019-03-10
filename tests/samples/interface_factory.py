"""Factory Intarface uses __call__
"""
import zope.interface

class IFoo(zope.interface.Interface):
    def bar() -> int:
        pass
    def baz() -> str:
        pass

class IFooFactory(zope.interface.Interface):
    def __call__(bar: int, baz: str) -> IFoo:
        pass

@zope.interface.provider(IFooFactory)
@zope.interface.implementer(IFoo)
class Foo:
    def __init__(self, bar: int, baz: str) -> None:
        self._bar = bar
        self._baz = baz
    def bar(self) -> int:
        return self._bar
    def baz(self) -> str:
        return self._baz

@zope.interface.provider(IFooFactory)
def foo_factory(bar: int, baz: str) -> IFoo:
    return Foo(bar, baz)

@zope.interface.provider(IFooFactory)
def bad_factory() -> IFoo:
    return Foo(10, "Sample")

def make_foo(factory: IFooFactory) -> IFoo:
    return factory(10, "Sample")

def main():
    foo = make_foo(Foo)
    foo = make_foo(foo_factory)
    foo = make_foo(bad_factory)

if __name__ == "__main__":
    main()

"""
<output>
interface_factory.py:40: ***FIXME NOT HAPPENED***
</output>
"""
