import zope.interface

class IFish(zope.interface.Interface):
    def swim() -> None: pass

class IFast(zope.interface.Interface):
    def swim(fast: bool = True) -> None: pass

@zope.interface.implementer(IFish)
class Fish:
    def swim(self) -> None: pass

@zope.interface.implementer(IFast)
class Fast:
    def swim(self, fast: bool = True) -> None: pass

class FastFish(Fast, Fish): pass


"""
<output>
</output>
"""
