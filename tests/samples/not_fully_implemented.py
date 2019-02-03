"""A simple valid interface declaration
"""
import zope.interface


class ISomething(zope.interface.Interface):
    def hello(x: int, y: str) -> None:
        pass


@zope.interface.implementer(ISomething)
class Something(object):
    pass


def run(smth: ISomething):
    smth.hello(1, "test")


def main() -> None:
    smth = Something()
    run(smth)


if __name__ == '__main__':
    main()

"""
<output>
not_fully_implemented.py:11: error: __main__.Something is not a valid implementation of __main__.ISomething
not_fully_implemented.py:11: note: 'Something' is missing following 'ISomething' protocol member:
not_fully_implemented.py:11: note:     hello
not_fully_implemented.py:22: error: Argument 1 to "run" has incompatible type "Something"; expected "ISomething"
not_fully_implemented.py:22: note: 'Something' is missing following 'ISomething' protocol member:
not_fully_implemented.py:22: note:     hello
</output>
"""
