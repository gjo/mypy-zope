"""Interfaces and implementations may form complicated hierarchies.

By themselves, both interface hierarchy and implementation hierarchies are
consistent and should not cause problems checkin them.

This would not work if interfaces were treated as superclasses of
implementations.
"""
import zope.interface

class ICreature(zope.interface.Interface):
    def bite(): pass
class ISwimmable(zope.interface.Interface): pass
class IReptilia(ICreature): pass
class ICrocodile(ICreature, ISwimmable): pass

@zope.interface.implementer(ISwimmable)
class Swimmable: pass
@zope.interface.implementer(IReptilia)
class Reptilia(Swimmable): pass
@zope.interface.implementer(ICrocodile)
class Crocodile(Reptilia): pass


def main() -> None:
    croc = Crocodile()

if __name__ == '__main__':
    main()

"""
<output>
complex_hierarchy.py:19: error: __main__.Reptilia is not a valid implementation of __main__.IReptilia
complex_hierarchy.py:19: note: 'Reptilia' is missing following 'IReptilia' protocol member:
complex_hierarchy.py:19: note:     bite
complex_hierarchy.py:21: error: __main__.Crocodile is not a valid implementation of __main__.ICrocodile
complex_hierarchy.py:21: note: 'Crocodile' is missing following 'ICrocodile' protocol member:
complex_hierarchy.py:21: note:     bite
</output>
"""
