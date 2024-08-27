#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                         (C) 2007 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



class ValueWithError(object):

    def __init__(self, value, error2=None, errorPropagator=None):
        if error2 is not None:
            assert error2 >= 0.0, \
                   "error bar square must be larger than zero: {0!s}".format(error2)
        
        self._value = float(value)
        self._error2 = error2
        if errorPropagator is None:
            from .ErrorPropagator import ErrorPropagator
            errorPropagator = ErrorPropagator()
        self._errorPropagator = errorPropagator
        return


    def asTuple(self): return self._value, self._error2 or 0.


    def copy(self):
        return ValueWithError(self._value, self._error2)


    def __str__(self): return str(self.asTuple())

    __repr__ = __str__


    ErrorPropagatorInterface = {
        'unary': [
            'inverse',
            '__neg__',
        ],
        'binary': [
            '__iadd__',
            '__isub__',
            '__imul__',
            '__idiv__',
            '__itruediv__',
            '__add__',
            '__sub__',
            '__mul__',
            '__div__',
            '__truediv__',
            '__radd__',
            '__rsub__',
            '__rmul__',
            '__rdiv__',
            '__rtruediv__',
        ],
        }


    # implementation details

    def unaryProxyCodeFactory(operator):
        return '''
def f(self):
    return getattr(self._errorPropagator, {0!r})( self )

{1!s} = f
'''.format(operator, operator)

    def binaryProxyCodeFactory(operator):
        return '''
def f(self, other):
    from histogram.ValueWithError import toVE
    other = toVE( other )
    return getattr(self._errorPropagator, {0!r})( self, other )

{1!s} = f
'''.format(operator, operator)


    operatorProxyCodeFactory = {
        'unary': unaryProxyCodeFactory,
        'binary': binaryProxyCodeFactory,
        }
        
    for operatorType, operators in ErrorPropagatorInterface.items():

        codeFactory = operatorProxyCodeFactory[operatorType]
        
        for operator in operators:
            code = codeFactory( operator)
            exec(code, locals())
            continue
        continue

    pass # end of ValueWithError


def toVE(candidate):
    if isinstance(candidate, ValueWithError): return candidate
    if isIterable(candidate):
        if len(candidate) < 4 and len(candidate) > 0:
            #try create VE instance from input
            return ValueWithError(*candidate)
    if isNumber(candidate): return ValueWithError(candidate)
    raise  NotImplementedError(\
        "Don't know how to convert {0!s}".format(
        candidate))


import types
ListType = type(list())
TupleType = type(tuple())
def isIterable(candidate):
    if isinstance(candidate, ListType): return True
    if isinstance(candidate, TupleType): return True
    if '__iter__' in dir(candidate): return True
    return False

LongType = IntType = type(0)
FloatType = type(0.0)
def isNumber(candidate):
    numbertypes = [
        LongType,
        FloatType,
        IntType]

    for t in numbertypes:
        if isinstance(candidate, t): return True
        continue
    return False
    

# version
__id__ = "$Id$"

# End of file
