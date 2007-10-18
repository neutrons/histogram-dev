
def tounit( candidate ):
    if isinstance( candidate, basestring ):
        from pyre.units import parser
        parser = parser()
        return parser.parse( candidate )
    return candidate


def isunitless( candidate ):
    from pyre.units.unit import unit
    if isinstance( candidate, unit ): return False
    if isNumber( candidate ): return True
    return False


def isNumber(a):
    return isinstance(a, int) or isinstance(a, float)
    

def isDimensional(d):
    from pyre.units.unit import unit
    return isinstance(d, unit)


def isPair(a):
    try: len(a)
    except: return False
    return len(a) == 2


def isNumberPair(a):
    if not isPair(a): return False
    for i in a:
        if not isNumber(i): return False
        continue
    return True


def isDimensionalPair(a):
    if not isPair(a): return False
    for i in a:
        if not isDimensional(i): return False
        continue
    return True

