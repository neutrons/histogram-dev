#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \namespace ndarray::NumpyNdArray
##
## This module hosts an implementation of ndarray.NdArray.NdArray using
## numpy. numpy.ndarray is a nice multidimensional array implementation
## for python. The NumpyNdArray.NdArray class here simply uses features
## of numpy.ndarray.
##


from AbstractNdArray import NdArray as AbstractNdArray
import numpy


import journal
info = journal.info("NumpyNdArray")
warning = journal.warning("NumpyNdArray")



def arrayFromNumpyArray( arr ):
    "create a NumpyNdArray.NdArray instance from a numpy array"
    rt = NdArray('float', 0)
    #this implementation is a hack!
    rt._numarr = arr
    rt.setShape( arr.shape )
    return rt


class NdArray(AbstractNdArray):


    def __init__( self, datatype, arg2, initVal=0, **kwds):
        """
        (1) NdArray( datatype, numList, **kwds)
        (2) NdArray( datatype, length, initVal=0, **kwds).
        Inputs (1):
            1. datatype (integer) recognized datatypes are
                float.......5
                double......6
                int........24
                unsigned...25
            2. list of numbers
            Possible keyword: 'handle': use this to construct a Python object
            that wraps an already existing vector
        Inputs (2):
            1. datatype (integer) recognized datatypes are
                float.......5
                double......6
                int........24
                unsigned...25
            2. length (integer > 0) length of vector to construct
            3. initial value to assign to all elements
        """
        if isinstance(datatype, int): t = numpytypecode_from_aktypecode( datatype )
        elif datatype in ['bool',"float", "double", "int", "uint"] : t = numpytypecode_from_typename(datatype)
        else:
            # assume it is valid datatype for numpy
            t = datatype
            pass

        try: len(arg2) #test if a list-like object
        except:
            #suppose input is the length of the array
            length = arg2
            self._numarr = numpy.ones( length, t ) * initVal
            return
        #if we reach here, then arg2 is a list 
        self._numarr = numpy.array( arg2, t )
        return


    def __neg__(self):
        r = self.copy()
        r._numarr *= -1
        return r


    def __rsub__(self, other):
        r = self.copy()
        r._numarr *= -1
        r += other
        return r


    def __rdiv__(self, other):
        r = self.__class__( self.datatype(), [] )
        if isNdArray( other ): other = other.asNumarray()
        elif isNumber(other): pass
        else: raise NotImplementedError , "%s / %s" % (
            other.__class__.__name__, self.__class__.__name__ )
        
        r._numarr = other/self._numarr
        return r
        

    def __iadd__(self, other):
        if isNdArray( other ): self._numarr += other.asNumarray()
        elif isNumber(other): self._numarr += other
        else: raise NotImplementedError , "%s + %s" % (
            self.__class__.__name__, other.__class__.__name__)
        return self


    def __isub__(self, other): 
        if isNdArray( other ): self._numarr -= other.asNumarray()
        elif isNumber(other): self._numarr -= other
        else: raise NotImplementedError , "%s + %s" % (
            self.__class__.__name__, other.__class__.__name__)
        return self


    def __imul__(self, other): 
        if isNdArray( other ): self._numarr *= other.asNumarray()
        elif isNumber(other): self._numarr *= other
        else: raise NotImplementedError , "%s + %s" % (
            self.__class__.__name__, other.__class__.__name__)
        return self


    def __idiv__(self, other):
        if isNdArray( other ): self._numarr /= other.asNumarray()
        elif isNumber(other): self._numarr /= other
        else: raise NotImplementedError , "%s + %s" % (
            self.__class__.__name__, other.__class__.__name__)
        return self


    def reverse(self):
        "array -> 1./array"
        self._numarr = 1./self._numarr
        return


    def transpose(self, *args):
        newna = self._numarr.transpose( *args )
        return arrayFromNumpyArray( newna )


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
        return numpy.sum(self._numarr[start:end])* dx


    def square( self):
        """square() -> None
        Square each element of this vector.
        Inputs: None
        Output: None
        Exceptions: ValueError
        """
        self *= self
        return
    
        
    def sqrt( self):
        """sqrt() -> None
        Take the square root of each element of this vector.
        Inputs: None
        Output: None
        Exceptions: ValueError
        """
        self._numarr = numpy.sqrt( self._numarr )
        return


    def sum( self, axis=None ):
        if axis is None: return _sum( self._numarr )
        else:
            r = self.__class__( self.datatype(), [] )
            try:
                from numpy import sum
                r._numarr = sum( self._numarr, axis = axis )
            except:
                from Numeric import sum
                r._numarr = sum( self._numarr, axis = axis )
            return r
        raise
    
        
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
        code = self.datatype()
        typename = numpytypecode_from_aktypecode( code )
        self._numarr = numpy.ones( count, typename) * val
        return


    def asList( self):
        """asList() -> [This vector's contents in a Python list].
        """
        return list(self._numarr)


    def asNumarray( self, dims=[]):
        #if dims == []: self._numarr.shape = -1
        #else : self._numarr.shape = dims
        return self._numarr


    def compare( self, other, epsilon = 0.000001):
        """compare( other, epsilon = 0.000001) -> Boolean
        Compare this vector elementwise with another vector. Returns True
        if the vectors have the same templateType, are both NdArray's,
        and are element-by-element equal to within epsilon.
        """
        if not isinstance(other, AbstractNdArray):
            info.log("%s is not a vector" % other)
            return False
        if self.datatype() != other.datatype():
            info.log("incompatible data type: %s, %s" % (self.datatype(), other.datatype()) )
            return False
        if self.shape() != other.shape():
            info.log("incompatible array dhape: %s, %s" % (self.shape(), other.shape()) )
            return False
        this = self._numarr
        other = other.asNumarray()
        diff = abs(this-other)
        import numpy
        return not numpy.any( diff>epsilon )


    def size( self):
        """size() -> number of elements.
        """
        #return len(self._numarr)
        import operator
        return reduce(operator.mul, self.shape())


    def datatype(self):
        """
        float.......5
        double......6
        int........24
        unsigned...25
        """
        arr = self._numarr
        return getAKTypecode( arr )

    def shape(self):
        self._shape = self._numarr.shape
        return self._shape


    def setShape(self, shape):
        self._numarr.shape = self._shape = shape
        return


    def copy(self):
        r = self.__class__( self.datatype(), [] )
        r._numarr = self._numarr.copy()
        return r

    
    def castCopy(self, typename):
        r = self.__class__( typename, [] )
        r._numarr = self._numarr.astype( numpytypecode_from_typename( typename) ) 
        return r


    def __getitem__(self, s):
        if isinstance(s, list): s = tuple(s )
        
        subelement = self._numarr[s]
        if isinstance(s, int): return subelement
        elif isinstance(s, tuple):
            s = list(s)
            slicing = False
            for i in s:
                if not isinstance(i, int): slicing = True; break
                continue
        elif isinstance(s, slice):
            slicing = True
        else:
            raise NotImplementedError, "Don't know how to get element indexed by %s" % (s,)
            
        if slicing:
            subarr = subelement
            res = self.__class__( self.datatype(), 1, 0 )
            res._numarr = subarr
            return res
            
        return subelement
    

    def __setitem__(self, s, rhs):
        if isNdArray(rhs): rhs = rhs.asNumarray()
        self._numarr[s] = rhs
        return rhs


    #pickle interface    
    def __getstate__(self):
        data = self._numarr
        shape = self.shape()
        return self.datatype(), data, shape

    def __setstate__(self, inputs):
        datatype, data, shape = inputs
        self.__class__.__init__(self, datatype, 1, 0)
        self._numarr = data
        self.setShape( shape )
        return

    pass # end of NdArray



def isNdArray(a):
    return isinstance(a, AbstractNdArray)


def isNumber(a):
    return isinstance(a, float) or isinstance(a, int)



def typename_from_aktypecode( code ):
    from array_kluge import types as aktypes
    for key, item in aktypes.iteritems():
        if item == code: return key
        continue
    raise ValueError , "Invalid type code %s" % code


def numpytypecode_from_aktypecode( code ):
    name = typename_from_aktypecode( code )
    return numpytypecode_from_typename(name)


def numpytypecode_from_typename( name ):
    table = {
        "double": 'float64',
        "float": "float32",
        "int": 'int32',
        "uint": "uint32",
        'bool': 'bool',
        }
    ret = table.get(name)
    if ret: return ret
    raise NotImplementedError , "unknow type code %s" % name



def getAKTypecode( arr ):
    "get array_kluge type code of a numpy/numarray array"
    try: return getNumpyArray_aktypecode( arr )
    except:
        try:
            return getNumericArray_aktypecode( arr )
        except:
            warning.log("numpy datatype unknown for ndarray: %s" % arr.dtype.name)
            return 10000+arr.dtype.num
    raise "Should not reach here"


def getNumpyArray_aktypecode( arr ):
    dt = arr.dtype
    name = dt.name
    if name == "int32": return 24
    elif name == "int64": return 24 # hack
    elif name == "float64": return 6
    elif name == "float32": return 5
    elif name == "uint32": return 25
    else: raise NotImplementedError , "don't know how to determine type of %s:%s" % (t,arr)
    raise "Should not reach here"


def getNumericArray_aktypecode( arr ):
    c = arr.typecode()
    d = {'l': 24,
         'i': 24,
         'f': 6,
         'd': 6,
         'u': 25}
    return d[c]
    


def _sum( anumarr ):
    if isNumber(anumarr): return anumarr
    from numpy import sum
    a = sum( anumarr )
    return _sum( a )



from AbstractNdArray import NdArray_TestCase as TestBase, unittest

class NdArray_TestCase(TestBase):

    def setUp(self):
        global NdArray
        self.NdArray = NdArray
        return
    
    pass # end of NdArray_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(NdArray_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
##     journal.debug('instrument').activate()
##     journal.debug('instrument.elements').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Thu Jun 29 09:32:21 2006

# End of file 
