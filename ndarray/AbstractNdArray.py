#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \namespace ndarray::NdArray
## base class for NdArray
##
## NdArray serves as the interface between histogram python classes
## and arrays. A histogram object always need storage, which can
## be implemented as c arrays or c++ vectors or others.
## The NdArray class in this module specifies the interface needed
## by the histogram class. It is abstract base class.
##
## Currently following methods are supported:
##  - numeric operators like + - * / += -= *= /=
##  - simple numeric functions like sum, square, sqrt
##  - slicing
##  - other utilities: copy, cast copy
##
## NdArray is a multidimensional array, so following methods are also
## essential:
##  - shape
##  - setShape
##
## Also included in this module is the unit test suite for this
## interface: NdArray_TestCase. It can be subclassed to test
## subclasses of this base class, as is done in StdVectorNdArray
## and NumpyNdArray.
##




#this class should be called NdArray, a concept similar to numpy.ndarray
#std::vector could contribute to an implementation of this NdArray
#and numpy.ndarray could contribute to another one
#this NdArray will be used by Histogram classes
class NdArray(object):


    def as(self, NdArrayTypeName):
        return converters.convert( self, NdArrayTypeName )


    def __neg__(self): self._nie("__neg__")


    def __mul__(self, other):
        "v1*v2"
        #default implementation to use __imul__
        res = self.copy()
        res *= other
        return res


    __rmul__ = __mul__
    
            
    def __add__(self, other):
        "v1+v2"
        #default implementation to use __iadd__
        r = self.copy()
        r += other
        return r


    __radd__ = __add__


    def __sub__(self, other):
        "v1-v2"
        #default implementation to use __isub__
        if self == other: return self.__class__( self.datatype(), self.size(), 0 )
        r = self.copy()
        r -= other
        return r


    def __rsub__(self, other): self._nie( "__rsub__" )


    def __rdiv__(self, other): self._nie("__rdiv__")


    def __div__(self, other):
        "v1/v2"
        #default implementation to use __idiv__
        r = self.copy()
        r /= other
        return r
    
        
    def __iadd__(self, other): self._nie("__iadd__")


    def __isub__(self, other): self._nie("__isub__")


    def __imul__(self, other): self._nie("__imul__")


    def __idiv__(self, other): self._nie("__idiv__")


    def __getitem__(self, s): self._nie( "__getitem__" )
        

    def __setitem__(self, s, rhs): self._nie( "__setitem__" )


    def transpose(self, *args):
        '''Returns a view of ndarray with axes transposed.
        If no axes are given,
        or None is passed, switches the order of the axes. For a 2-d
        histogram, this is the usual matrix transpose. If axes are given,
        they describe how the axes are permuted.
        '''
        self._nie( "transpose" )


    def reverse(self):
        "array --> 1./array"
        self._nie( "reverse" )



    # ufuncs
    def integrate( self, start, end, dx):
        """integrate(  start, end, dx) -> dx*\sum_{i in [start, end)}vec_i
        Add from start to (but not including) end, multiply by dx.
        Inputs:
            start: index at which to begin (integer)
            end: index one past the last (integer)
            dx: \"measure\"
        Output:
            dx*\sum_{i in [start, end)}
        Exceptions: ValueError, IndexError
        Notes: end must be <= size of vector; start must be <= end."""
        self._nie("integrate")


    def square( self):
        """square() -> None
        Square each element of this vector.
        Inputs: None
        Output: None
        Exceptions: ValueError
        """
        self._nie("square")
    
        
    def sqrt( self):
        """sqrt() -> None
        Take the square root of each element of this vector.
        Inputs: None
        Output: None
        Exceptions: ValueError
        """
        self._nie( "sqrt" )


    def sum( self, axis = None ):
        self._nie( "sum" )
    
        
    # utilities
    def assign( self, count, val):
        """assign( count, value) -> None
        Erases all elements of this vector, then inserts <count> elements each
        with <value> into this vector.
        inputs:
            count (number of copies of value to insert)
            value ...(float)
        output: PyCObject w/ void pointer to &c_array[offset]
        Exceptions: ValueError
        """
        self._nie( "assign" )


    def asList( self):
        """asList() -> [This vector's contents in a Python list].
        """
        self._nie( "asList" )


    def asNumarray( self, dims=[]):
        """asNumarray() -> numpy array
        Create a numpy array object that looks at this vector's memory.
        Input:
            dims: list of dimensions for array shape. Default shape is 1d
                  with length of vector. Product of all dimensions must be
                  <= length of vector.
        Output:
            numpy.array object.
        Exceptions: TypeError, IndexError, RuntimeError
        Notes: numpy must be installed.
        """
        self._nie( "asNumarray" )


    def compare( self, other, epsilon = 0.000001):
        """compare( other, epsilon = 0.000001) -> Boolean
        Compare this vector elementwise with another vector. Returns True
        if the vectors have the same templateType, are both Vector's,
        and are element-by-element equal to within epsilon.
        """
        self._nie( "compare" )


    def shape(self):
        self._nie( "shape" )


    def setShape(self):
        self._nie( "setShape" )


    def copy(self):
        self._nie( "copy" )


    def castCopy(self, typename):
        """typeName:
        double
        int
        unsigned"""
        self._nie( "castCopy" )


    def size( self):
        """size() -> number of elements.
        """
        self._nie( "size" )


    def datatype(self):
        """
        float.......5
        double......6
        int........24
        unsigned...25
        """
        self._nie( "datatype" )


    def __init__( self, datatype, arg2, initVal=0):
        """(1) Vector( datatype, numList, **kwds)
        (2) Vector( datatype, length, initVal=0, **kwds).
        Inputs (1):
            1. datatype (integer) recognized datatypes are
                float.......5
                double......6
                int........24
                unsigned...25
            2. list of numbers
        Inputs (2):
            1. datatype (integer) recognized datatypes are
                float.......5
                double......6
                int........24
                unsigned...25
            2. length (integer > 0) length of vector to construct
            3. initial value to assign to all elements
        """
        self._nie( "__init__" )


    def _nie(self, method):
        raise NotImplementedError , "%s must provide method '%s'" % (
            self.__class__.__name__, method )


    pass # end of NdArray



#test of interface
import unittest
from unittest import TestCase

class NdArray_TestCase(TestCase):


    def setUp(self):
        # overload this to test a special subclass of NdArray
        self.NdArray = None
        return


    def testCtor(self):
        """ NdArray: ctor """
        v = self.NdArray( "double", [1,2,3] )
        self.assertEqual( v.asNumarray()[0] , 1 )
        self.assertEqual( v.asNumarray()[1] , 2 )
        self.assertEqual( v.datatype(), 6 )
        
        v = self.NdArray( "float", 3, 2 )
        self.assertEqual( v.asNumarray()[0] , 2 )
        self.assertEqual( v.size() , 3 )
        self.assertEqual( v.datatype(), 5 )
        
        v = self.NdArray( "int", 3, 2 )
        self.assertEqual( v.asNumarray()[0] , 2 )
        self.assertEqual( v.size() , 3 )
        self.assertEqual( v.datatype(), 24 )
        
        v = self.NdArray( "uint", 3, 2 )
        self.assertEqual( v.asNumarray()[0] , 2 )
        self.assertEqual( v.size() , 3 )
        self.assertEqual( v.datatype(), 25 )
        
        return


    def test__neg__(self):
        "NdArray: operator '-a'"
        v = self.NdArray( 'double', [1,2,3] )
        v2 = -v
        self.assert_( v2.compare( self.NdArray('double', [-1,-2,-3] ) ) )
        return
        

    def test__add__(self):
        "NdArray: operator 'a+b'"
        v = self.NdArray( 'double', [1,2,3] )
        v2 = v + 1
        self.assert_( v2.compare( self.NdArray('double', [2,3,4] ) ) )

        v2 = 1 + v
        self.assert_( v2.compare( self.NdArray('double', [2,3,4] ) ) )
        
        v3 = v + self.NdArray( "double", [2,3,4] )
        self.assert_( v3.compare( self.NdArray('double', [3,5,7])) )

        self.assertRaises( NotImplementedError , v.__add__, "a" )
        return


    def test__mul__(self):
        "NdArray: operator 'a*b'"
        v = self.NdArray( 'double', [1,2,3] )
        v2 = v * 2
        self.assert_( v2.compare( self.NdArray('double', [2,4,6] ) ) )

        v2 = 2 * v
        self.assert_( v2.compare( self.NdArray('double', [2,4,6] ) ) )
        
        v2 = v * v
        self.assert_( v2.compare( self.NdArray('double', [1,4,9] ) ) )
        
        return


    def test__sub__(self):
        "NdArray: operator 'a-b'"
        v = self.NdArray( 'double', [1,2,3] )
        v2 = v - 2
        self.assert_( v2.compare( self.NdArray('double', [-1,0,1] ) ) )
        
        v2 = v - v
        self.assert_( v2.compare( self.NdArray('double', [0,0,0] ) ) )
        return


    def test__div__(self):
        "NdArray: operator 'a/b'"
        v = self.NdArray( 'double', [1,2,3] )
        v2 = v / 2
        self.assert_( v2.compare( self.NdArray('double', [0.5,1,1.5] ) ) )
        
        v2 = 1 / v
        self.assert_( v2.compare( self.NdArray('double', [1,0.5,1./3] ) ) )

        v2 = v / v
        self.assert_( v2.compare( self.NdArray('double', [1,1,1] ) ) )
        
        v2 = v / v.copy()
        self.assert_( v2.compare( self.NdArray('double', [1,1,1] ) ) )

        v = self.NdArray( 'double', range(12) )
        v.setShape( (3,4) )
        
        v2 = v / v.copy()
        v2.setShape( (12,) )
        self.assert_( v2.compare( self.NdArray('double', [1]*12 ) ) )

        return


    def test__iadd__(self):
        "NdArray: operator 'a+=b'"
        v = self.NdArray( 'double', [1,2,3] )
        v += 1
        self.assert_( v.compare( self.NdArray('double', [2,3,4] ) ) )
        
        v += self.NdArray( "double", [2,3,4] )
        self.assert_( v.compare( self.NdArray('double', [4,6,8])) )

        print "__iadd__ big array"
        v = self.NdArray( "double", 1024000, 2 )
        v += self.NdArray( "double", 1024000, 1 )
        self.assert_( v.compare( self.NdArray('double', 1024000, 3)) )

        self.assertRaises( NotImplementedError , v.__iadd__, "a" )
        return


    def test__isub__(self):
        "NdArray: operator 'a-=b'"
        v = self.NdArray( 'double', [1,2,3] )
        v -= 1
        self.assert_( v.compare( self.NdArray('double', [0,1,2] ) ) )
        
        v -= self.NdArray( "double", [2,3,4] )
        self.assert_( v.compare( self.NdArray('double', [-2,-2,-2])) )

        self.assertRaises( NotImplementedError , v.__isub__, "a" )
        return


    def test__imul__(self):
        "NdArray: operator 'a*=b'"
        v = self.NdArray( 'double', [1,2,3] )
        v *= 2
        self.assert_( v.compare( self.NdArray('double', [2,4,6] ) ) )
        
        v *= self.NdArray( "double", [2,3,4] )
        self.assert_( v.compare( self.NdArray('double', [4,12,24])) )

        self.assertRaises( NotImplementedError , v.__imul__, "a" )
        return


    def test__idiv__(self):
        "NdArray: operator 'a/=b'"
        v = self.NdArray( 'double', [1,2,3] )
        v /= 2
        self.assert_( v.compare( self.NdArray('double', [0.5, 1, 1.5] ) ) )
        
        v /= self.NdArray( "double", [0.5,1,1.5] )
        self.assert_( v.compare( self.NdArray('double', [1,1,1])) )

        self.assertRaises( NotImplementedError , v.__idiv__, "a" )
        return


    def testReverse(self):
        "NdArray: array  -> 1./array"
        v = self.NdArray( 'double', [1,2,3] )
        v.reverse()
        self.assert_( v.compare( self.NdArray('double', [1, 1./2, 1./3] ) ) )
        return


    def testTranspose(self):
        "NdArray: transpose"
        v = self.NdArray( 'double', range(6) )
        v.setShape( (2,3) )
        vt = v.transpose()
        self.assertEqual( vt.shape(), (3,2) )
        self.assertEqual( vt[0,0],0 )
        self.assertEqual( vt[0,1],3 )
        self.assertEqual( vt[1,0],1 )
        self.assertEqual( vt[1,1],4 )
        self.assertEqual( vt[2,0],2 )
        self.assertEqual( vt[2,1],5 )
        return
    

    def test__getitem__(self):
        "NdArray: operator 'a[3:5], a[3]'"
        v = self.NdArray( 'double', range(12) )
        self.assert_( v[3:5].compare( self.NdArray('double', [3,4] ) ) )
        self.assertAlmostEqual( v[3], 3 )
        
        v.setShape( (3,4) )
        subarr = v[1:2, 1:2]
        expected = self.NdArray('double', [5] ) ; expected.setShape( (1,1) )
        self.assert_( subarr.compare( expected ) )
        return


    def test__setitem__(self):
        "NdArray: operator 'a[3]=4'"
        v = self.NdArray( 'double', range(12) )
        v[3:5] = [1,2]
        self.assert_( v[3:5].compare( self.NdArray('double', [1,2] ) ) )

        v[10] = 11
        self.assertAlmostEqual( v[10], 11 )

        v[3:5] = 0
        self.assert_( v[3:5].compare( self.NdArray('double', [0,0] ) ) )
        return


    def testCopy(self):
        "NdArray: method 'copy'"
        v = self.NdArray( 'double', range(12) )
        self.assert_( v.compare( v.copy() ) )
        return


    def testCastCopy(self):
        "NdArray: method 'castCopy'"
        v = self.NdArray( 'double', range(12) )
        v2 = self.NdArray( 'int', range(12) )
        self.assert_( v2.compare( v.castCopy( "int" ) ) )
        return
    

    def testIntegrate(self):
        "NdArray: integrate"
        v = self.NdArray("double", range(3) )
        r = v.integrate( 0, 2, 0.1)
        self.assertAlmostEqual( r, 0.1 )
        return
        
        
    def testSquare(self):
        "NdArray: square"
        v = self.NdArray("double", range(3) )
        r = v.square( )
        self.assert_( v.compare( self.NdArray('double', [0,1,4] ) ) )
        return
        
        
    def testSqrt(self):
        "NdArray: sqrt"
        v = self.NdArray("double", [1,4,9] )
        v.sqrt( )
        self.assert_( v.compare( self.NdArray('double', [1,2,3] ) ) )
        return        
        
        
    def testSum(self):
        "NdArray: sum"
        v = self.NdArray("double", range(3) )
        r = v.sum( )
        self.assertAlmostEqual( r, 3 )

        v = self.NdArray("double", range(9) )
        v.setShape( (3,3) )
        r = v.sum( )
        self.assertAlmostEqual( r, 36 )
        r1 = v.sum(axis = 0)
        expected_r1 = self.NdArray( 'double', [9,12,15])
        self.assert_( r1.compare( expected_r1 ) )
        return


    def testAssign(self):
        "NdArray: assign"
        v = self.NdArray("double", range(3) )
        v.assign( 5, 1.0 )
        self.assert_( v.compare( self.NdArray('double', [1,1,1,1,1] ) ) )
        return


    def testAsList(self):
        "NdArray: asList"
        v = self.NdArray("double", range(3) )
        l = v.asList()
        self.assert_( v.compare( self.NdArray( "double", l )) )
        return

    
    def testAsNumarray(self):
        "NdArray: asNumarray"
        v = self.NdArray("double", range(3))
        na = v.asNumarray()
        import numpy
        self.assert_( isinstance( na, numpy.ndarray ) )
        self.assert_( v.compare( self.NdArray( "double", list(na) ) ) )
        return


    def test_dump(self):
        "NdArray: pickle.dump"
        import pickle
        v = self.NdArray( "double", [1,2,3,4] )
        v.setShape( (2,2) )
        pickle.dump( v, open( "tmp.pkl", 'w' ) )
        return


    def test_load(self):
        "NdArray: pickle.load"
        import pickle
        v = self.NdArray( "double", [1,2,3,4] )
        v.setShape( (2,2) )
        pickle.dump( v, open( "tmp.pkl", 'w' ) )
        v1 = pickle.load( open( "tmp.pkl" ) )
        print v1.asNumarray()
        assert v1.compare(v)
        return
    

    def test_setShape(self):
        "NdArray: setShape"
        v = self.NdArray( 'double', range(12) )
        v.setShape( (3,4) )

        self.assertRaises( ValueError, v.setShape, (4,4) )
        return
    
    pass # end of NdArray_TestCase


import converters



# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Thu Jun 29 09:32:21 2006

# End of file 
