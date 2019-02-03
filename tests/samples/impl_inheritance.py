"""Interface implementations can be inherited
"""
import zope.interface

class IBookmark(zope.interface.Interface):
    def remember(url: str) -> None:
        pass

@zope.interface.implementer(IBookmark)
class Bookmark(object):
    pass

class SuperBookmark(Bookmark):
    def remember(self, url: str) -> None:
        pass


def main() -> None:
    bm: IBookmark = SuperBookmark()

    # We can assign anything to abstract attributes
    bm.remember(None)  # Error, string is expected

if __name__ == '__main__':
    main()

"""
<output>
impl_inheritance.py:9: error: __main__.Bookmark is not a valid implementation of __main__.IBookmark
impl_inheritance.py:9: note: 'Bookmark' is missing following 'IBookmark' protocol member:
impl_inheritance.py:9: note:     remember
impl_inheritance.py:22: error: Argument 1 to "remember" of "IBookmark" has incompatible type "None"; expected "str"
</output>
"""
