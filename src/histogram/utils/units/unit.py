from __future__ import division

#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from functools import total_ordering
import operator


@total_ordering
class unit(object):
    _labels = ("m", "kg", "s", "A", "K", "mol", "cd")
    _zero = (0,) * len(_labels)
    _negativeOne = (-1,) * len(_labels)

    def __init__(self, value, derivation):
        self.value = value
        self.derivation = derivation
        return

    def __add__(self, other):
        if not self.derivation == other.derivation:
            raise IncompatibleUnits("add", self, other)

        return unit(self.value + other.value, self.derivation)

    def __sub__(self, other):
        if not self.derivation == other.derivation:
            raise IncompatibleUnits("subtract", self, other)

        return unit(self.value - other.value, self.derivation)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return unit(other * self.value, self.derivation)

        value = self.value * other.value
        derivation = tuple(map(operator.add, self.derivation, other.derivation))

        if derivation == self._zero:
            return value

        return unit(value, derivation)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return unit(self.value / other, self.derivation)
        value = self.value / other.value
        derivation = tuple(map(operator.sub, self.derivation, other.derivation))

        if derivation == self._zero:
            return value

        return unit(value, derivation)

    __div__ = __truediv__  # py2

    def __pow__(self, other):
        if (not isinstance(other, int)) and (not isinstance(other, float)):
            raise InvalidOperation("**", self, other)

        value = self.value**other
        derivation = tuple(map(operator.mul, [other] * 7, self.derivation))

        return unit(value, derivation)

    def __pos__(self):
        return self

    def __neg__(self):
        return unit(-self.value, self.derivation)

    def __abs__(self):
        return unit(abs(self.value), self.derivation)

    def __invert__(self):
        value = 1.0 / self.value
        derivation = tuple(map(operator.mul, self._negativeOne, self.derivation))
        return unit(value, derivation)

    def __rmul__(self, other):
        if (not isinstance(other, int)) and (not isinstance(other, float)):
            raise InvalidOperation("*", other, self)

        return unit(other * self.value, self.derivation)

    def __rtruediv__(self, other):
        if (not isinstance(other, int)) and (not isinstance(other, float)):
            raise InvalidOperation("/", other, self)

        value = other / self.value
        derivation = tuple(map(operator.mul, self._negativeOne, self.derivation))
        return unit(value, derivation)

    __rdiv__ = __rtruediv__  # py2

    def __float__(self):
        if self.derivation == self._zero:
            return self.value
        raise InvalidConversion(self)

    """def __cmp__(self, other):
        return cmp(self.value, other.value)"""

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        str = "{0:g}".format(self.value)
        derivation = self._strDerivation()
        if not derivation:
            return str

        return str + "*" + derivation

    def __repr__(self):
        str = "{0:g}".format(self.value)
        derivation = self._strDerivation()
        if not derivation:
            return str

        return str + "*" + derivation

    def _strDerivation(self):
        return _strDerivation(self._labels, self.derivation)


# instances

one = dimensionless = unit(1, unit._zero)


# helpers


def _strDerivation(labels, exponents):
    dimensions = filter(None, map(_strUnit, labels, exponents))
    return "*".join(dimensions)


def _strUnit(label, exponent):
    if exponent == 0:
        return None
    if exponent == 1:
        return label
    return label + "**{0:g}".format(exponent)


# exceptions


class InvalidConversion(Exception):
    def __init__(self, operand):
        self._op = operand
        return

    def __str__(self):
        str = "dimensional quantities ('{0!s}') ".format(self._op._strDerivation())
        str = str + "cannot be converted to scalars"
        return str


class InvalidOperation(Exception):
    def __init__(self, op, operand1, operand2):
        self._op = op
        self._op1 = operand1
        self._op2 = operand2
        return

    def __str__(self):
        str = "Invalid expression: {0!s} {1!s} {2!s}".format(
            self._op1, self._op, self._op2
        )
        return str


class IncompatibleUnits(Exception):
    def __init__(self, op, operand1, operand2):
        self._op = op
        self._op1 = operand1
        self._op2 = operand2
        return

    def __str__(self):
        str = "Cannot {0!s} quanitites with units of '{1!s}' and '{2!s}'".format(
            self._op, self._op1._strDerivation(), self._op2._strDerivation()
        )
        return str


# version
__id__ = "$Id: unit.py,v 1.1.1.1 2006-11-27 00:10:08 aivazis Exp $"

#
# End of file
