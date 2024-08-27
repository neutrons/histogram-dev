import numpy as N
from pyre.units import *
from pyre.units import unit, length, time, pressure, angle
import sys


def unitFromString(s):
    if s is None:
        return 1
    if isinstance(s, unitFromString.unittype):
        return s
    if sys.version_info >= (3, 0) and isinstance(s, bytes):
        s = s.decode()
    if isinstance(s, str):
        return unitFromString.parser.parse(s)
    try:
        return unitFromString.parser.parse(str(s))
    except:
        raise NotImplementedError("Don't know how to convert {0!r} to unit".format(s))
    raise "Should not reach here"


unitFromString.parser = parser()
unitFromString.unittype = unit.unit


def tounit(candidate):
    if sys.version_info >= (3, 0) and isinstance(candidate, bytes):
        candidate = candidate.decode()
    if isinstance(candidate, str):
        _parser = parser()
        return _parser.parse(candidate)
    return candidate


def isunitless(candidate):
    if isinstance(candidate, unit.unit):
        return False
    if isNumber(candidate):
        return True
    return False


def isNumber(a):
    return N.isscalar(a) and N.isreal(a)


def isDimensional(d):
    return isinstance(d, unit.unit)


def isPair(a):
    try:
        len(a)
    except:
        return False
    return len(a) == 2


def isNumberPair(a):
    if not isPair(a):
        return False
    for i in a:
        if not isNumber(i):
            return False
        continue
    return True


def isDimensionalPair(a):
    if not isPair(a):
        return False
    for i in a:
        if not isDimensional(i):
            return False
        continue
    return True
