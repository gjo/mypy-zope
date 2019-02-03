from zope.interface.common .interfaces import IWarning

def main() -> None:
    ob = IWarning(None)
    reveal_type(ob)

"""
<output>
adaptation_minimal.py:5: error: Revealed type is 'zope.interface.common.interfaces.IWarning'
</output>
"""