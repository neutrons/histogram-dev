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

    def __init__(self, value, error2 = None, errorPropagator = None ):
        if error2 is not None:
            assert error2 >= 0.0, \
                   "error bar square must be larger than zero: %s" % error2
        
        self._value = float(value)
        self._error2 = error2
        if errorPropagator is None:
            from ErrorPropagator import ErrorPropagator
            errorPropagator  = ErrorPropagator()
        self._errorPropagator = errorPropagator
        return


    def asTuple(self): return self._value, self._error2 or 0.


    def copy(self):
        return ValueWithError( self._value, self._error2)


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
        '__add__',
        '__sub__',
        '__mul__',
        '__div__',
        '__radd__',
        '__rsub__',
        '__rmul__',
        '__rdiv__',
        ],
        }


    # implementation details

    def unaryProxyCodeFactory( operator ):
        return '''
def f(self):
    return getattr(self._errorPropagator, %r)( self )

%s = f
''' % (operator, operator)

    def binaryProxyCodeFactory( operator ):
        return '''
def f(self, other):
    from histogram.ValueWithError import toVE
    other = toVE( other )
    return getattr(self._errorPropagator, %r)( self, other )

%s = f
''' % (operator, operator)


    operatorProxyCodeFactory = {
        'unary': unaryProxyCodeFactory,
        'binary': binaryProxyCodeFactory,
        }
        
    for operatorType, operators in ErrorPropagatorInterface.iteritems():

        codeFactory = operatorProxyCodeFactory[ operatorType ]
        
        for operator in operators:
            code = codeFactory( operator )
            exec code in locals()
            continue
        continue

    pass # end of ValueWithError


def toVE( candidate ):
    if isinstance( candidate, ValueWithError): return candidate
    if isIterable( candidate ):
        if len(candidate) < 4 and len(candidate) > 0 :
            #try create VE instance from input
            return ValueWithError( *candidate )
    if isNumber( candidate ): return ValueWithError( candidate )
    raise  NotImplementedError, \
          "Don't know how to convert %s" % (
        candidate, )


import types
def isIterable( candidate ):
    if isinstance( candidate, types.ListType): return True
    if isinstance( candidate, types.TupleType): return True
    if '__iter__' in dir(candidate):  return True
    return False


def isNumber( candidate ):
    numbertypes = [
        types.LongType,
        types.FloatType,
        types.IntType,]

    for t in numbertypes:
        if isinstance( candidate, t ): return True
        continue
    return False
    

# version
__id__ = "$Id$"

# End of file
