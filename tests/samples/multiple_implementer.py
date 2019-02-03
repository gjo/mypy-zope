"""zope.interface.implementer accepts multiple interfaces
"""
import zope.interface

class IBookmark(zope.interface.Interface):
    def remember(url: str) -> None:
        pass

class IActionalble(zope.interface.Interface):
    def follow(times: int):
        pass

@zope.interface.implementer(IBookmark, IActionalble)
class Bookmark(object):
    pass


"""
<output>
multiple_implementer.py:13: error: __main__.Bookmark is not a valid implementation of __main__.IBookmark
multiple_implementer.py:13: note: 'Bookmark' is missing following 'IBookmark' protocol member:
multiple_implementer.py:13: note:     remember
multiple_implementer.py:13: error: __main__.Bookmark is not a valid implementation of __main__.IActionalble
multiple_implementer.py:13: note: 'Bookmark' is missing following 'IActionalble' protocol member:
multiple_implementer.py:13: note:     follow
</output>
"""
