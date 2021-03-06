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
    pass


def main() -> None:
    bm = SuperBookmark()

    # We can assign anything to abstract attributes
    bm.remember(None)  # Error, string is expected

if __name__ == '__main__':
    main()

"""
<output>
impl_inheritance.py:19: error: Cannot instantiate abstract class 'SuperBookmark' with abstract attribute 'remember'
impl_inheritance.py:22: error: Argument 1 to "remember" of "IBookmark" has incompatible type "None"; expected "str"
</output>
"""
