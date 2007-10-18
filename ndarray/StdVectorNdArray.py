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


## \namespace ndarray::StdVectorNdArray
##
## This module hosts an implementation of ndarray.NdArray.NdArray using
## std::vector. This package uses the python package
## <a href="../../../stdVector/stdVector/html/">stdVector</a>.
## stdVector c++ implementation is not as fast as numpy arrays when array is big,
## so a StdVectorNdArray.NdArray is casted to an NumpyNdArray.NdArray
## if an array is big.
##


from AbstractNdArray import NdArray as AbstractNdArray

from stdVector.StdVector import StdVector



def arrayFromVector( v ):
    res = NdArray( v.datatype(), v.size(), handle = v.handle() )
    res.__ref_to_original_vector = v
    return res


class NdArray(StdVector, AbstractNdArray):


    def __init__(self, *args, **kwds):
        StdVector.__init__(self, *args, **kwds)
        if self.size() > 1000000: self._big = True
        else: self._big = False
        return


    def __neg__(self):
        return -1. * self


    def __rdiv__(self, other):
        if isNumber(other):
            res = self.copy()
            res.reverse()
            res *= other
            return res
        raise NotImplementedError , "__rdiv_ is not defined for %s and %s" % (
            self.__class__.__name__, other.__class__.__name__ )


    def __iadd__(self, other):
        if self._big: t = self[:]; t+=other; return self
        if isNumber(other): self.addScalar( other ); return self
        if isNdArray(other): self.plusEquals( other.as( thistype ) ); return self
        raise NotImplementedError , "__iadd__ is not defined for %s and %s" % (
            self.__class__.__name__, other.__class__.__name__ )


    def __isub__(self, other):
        if self._big: t = self[:]; t-=other; return self
        if isNumber(other): self.addScalar( -other ); return self
        if isNdArray(other): self.minusEquals( other.as( thistype ) ); return self
        raise NotImplementedError , "__isub__ is not defined for %s and %s" % (
            self.__class__.__name__, other.__class__.__name__ )


    def __imul__(self, other):
        if self._big: t = self[:]; t*=other; return self
        if isNumber(other): self.multScalar( other ); return self
        if isNdArray(other): self.timesEquals( other.as(thistype) ); return self
        raise NotImplementedError , "__imul__ is not defined for %s and %s" % (
            self.__class__.__name__, other.__class__.__name__ )


    def __idiv__(self, other):
        if self._big: t = self[:]; t/=other; return self
        if isNumber(other): self.multScalar( 1./other ); return self
        if isNdArray(other): self.divideEquals( other.as( thistype ) ); return self
        raise NotImplementedError , "__idiv__ is not defined for %s and %s" % (
            self.__class__.__name__, other.__class__.__name__ )



    def sum(self, axis = None):
        if axis is None: return StdVector.sum(self, 0, self.size())
        else:
            r = self.as("NumpyNdArray")
            return r.sum( axis= axis )
        raise
    

    def reverse(self):
        na = self.asNumarray()
        na[:] = 1./na
        return


    def transpose(self, *args):
        rt = self.as( "NumpyNdArray" )
        return rt.transpose( *args )


    def copy(self):
##         res = self.__class__( self.datatype(), self.asList() )
##         res.setShape(self.shape())
##         return res
        from stdVector import copy
        c = copy(self)
        res = arrayFromVector( c )
        res.setShape( self.shape() )
        return res


    def castCopy(self, typename):
        from stdVector import castCopy
        res = self.__class__(typename, self.size(), 0)
        castCopy(self, res)
        res.setShape( self.shape() )
        return res
    

    def shape(self): return self._shape


    def setShape(self, s):
        if volume(s) != self.size():
            msg =  "total size of new shape must be unchanged: "\
                  "new shape = %s, totsize = %s" % (s, self.size() )
            raise ValueError, msg
        self._shape = s
        return


    def asNumarray(self):
        r = StdVector.asNumarray(self)
        try:
            r.shape = self.shape()
        except Exception, e:
            msg = "%s: %s" % ( e.__class__, e)
            msg +=  "shape mismatch: %s, %s" % (r.shape, self.shape())
            raise ValueError , msg
        return r


    def __getitem__(self, s):
        #convert to  NumpyNdArray
        t = self.as( "NumpyNdArray" )
        return t[s]
    

    def __setitem__(self, s, rhs):
        na = self.asNumarray()
        na.shape = self.shape()
        if isNdArray( rhs ): rhs = rhs.asNumarray()
        try:
            na[s] = rhs
        except Exception, msg:
            newmsg = "Cannot set slice %s to %s: %s" % (s, rhs, msg)
            raise msg.__class__, newmsg
        return


    #pickle interface    
    def __getstate__(self):
        data = self.asNumarray().copy()
        shape = self.shape()
        return self.datatype(), data, shape

    def __setstate__(self, inputs):
        datatype, data, shape = inputs
        import operator
        size = reduce( operator.mul, shape )
        initVal = 0
        NdArray.__init__( self, datatype, size, initVal )
        self.setShape( shape )
        self.asNumarray()[:] = data
        return
        

    pass # end of NdArray



thistype = "StdVectorNdArray"



def isNumber(a):
    return isinstance(a, int) or isinstance(a, float)


def isNdArray(a):
    return isinstance(a, AbstractNdArray)


def volume( shape ):
    from operator import mul
    return reduce( mul, shape )



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
    journal.info("ARCSStdVectorTest").activate()
    journal.info("NumpyNdArray").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()



# version
__id__ = "$Id$"

# End of file 
