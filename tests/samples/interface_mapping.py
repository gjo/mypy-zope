import zope.interface
from zope.interface.common import mapping

class IBookmarkContainer(mapping.IMapping):
    pass

@zope.interface.implementer(IBookmarkContainer)
class BookmarkContainer(object):
    def values(self):
        pass

    def __getitem__(self, key: str) -> int: pass
    def __setitem__(self, key: str, value: int) -> None: pass

def main() -> None:
    bc = BookmarkContainer()
    bc['one'] = 1

if __name__ == '__main__':
    main()

"""
<output>
interface_mapping.py:7: error: __main__.BookmarkContainer is not a valid implementation of __main__.IBookmarkContainer
</output>
"""
