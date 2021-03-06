import zope.interface
import zope.schema


class IBookmark(zope.interface.Interface):
    textline = zope.schema.TextLine(
        title='Title',
        description='Optional text line',
        required=False)
    reqtextline = zope.schema.TextLine(
        title='Title',
        description='Implicitly required text line',)
    expreqtextline = zope.schema.TextLine(
        title='Title',
        description='Explicitly required text line',
        required=True)
    asciiline = zope.schema.ASCIILine(
        title='Title',
        description='ASCII-only text line',
        required=False)


@zope.interface.implementer(IBookmark)
class Bookmark(object):
    pass

def main() -> None:
    bm = Bookmark()
    bm.textline = 343  # Error, expected to be string
    bm.reqtextline = None  # Error, it is required
    bm.expreqtextline = None  # Error, it is required
    bm.asciiline = True  # Error, it is a string

if __name__ == '__main__':
    main()

"""
<output>
schema_text.py:29: error: Incompatible types in assignment (expression has type "int", variable has type "Optional[str]")
schema_text.py:30: error: Incompatible types in assignment (expression has type "None", variable has type "str")
schema_text.py:31: error: Incompatible types in assignment (expression has type "None", variable has type "str")
schema_text.py:32: error: Incompatible types in assignment (expression has type "bool", variable has type "Optional[str]")
</output>
"""
