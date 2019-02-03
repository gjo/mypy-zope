"""Support type inference after providedBy checks

Interface.providedBy is translated to isinstance;
Interface.implementedBy is tranlated to issubclass
"""
import zope.interface
from typing import Optional

class IBookmark(zope.interface.Interface):
    def create(url: str) -> None:
        pass

@zope.interface.implementer(IBookmark)
class Bookmark(object):
    x = ""
    def create(self, url: str) -> None:
        pass

def main(obj: Optional[IBookmark]) -> None:
    if not IBookmark.providedBy(obj):
        reveal_type(obj)
    else:
        reveal_type(obj)
    reveal_type(obj)

    cls = obj.__class__
    if IBookmark.implementedBy(cls):
        reveal_type(cls)
    else:
        reveal_type(cls)
    reveal_type(cls)

if __name__ == '__main__':
    main(Bookmark())

"""
<output>
interface_implications.py:21: error: Revealed type is 'None'
interface_implications.py:23: error: Revealed type is '__main__.IBookmark'
interface_implications.py:24: error: Revealed type is 'Union[__main__.IBookmark, None]'
interface_implications.py:28: error: Revealed type is 'Type[__main__.IBookmark]'
interface_implications.py:30: error: Revealed type is 'Union[Type[__main__.IBookmark], Type[None]]'
interface_implications.py:31: error: Revealed type is 'Union[Type[__main__.IBookmark], Type[None]]'
</output>
"""
