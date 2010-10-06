#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004


## \namespace stdVector::StdVector
##
## provides python class wrapping a stl vector
##
## This class is a subclass of TemplateCObject.TemplateCObject.
## It wraps python bindings of methods of stl vector class
## as its methods.
##


from TemplateCObject import TemplateCObject as Template
import stdVector
import journal
debug = journal.debug("stdVector.StdVector")



class StdVector( Template ):
    """Class that wraps a C++ STL vector. 
    """

    def getSlice( self, start, size, stride, output = None, copy = False):
        if not copy: raise NotImplementedError , "getSlice( copy = False )"
        from Slice import Slice
        slce = Slice( start, size, stride )
        if not output: output = vector( self.datatype(), slce.size())
        from stdVector import extractSlice
        extractSlice( self._handle, self._templateType, output._handle, slce._handle)
        return output
    

    # vector-scalar arithmetic
    def addScalar( self, scalar, outputVector = None, rangeStart = None,
                   rangeEnd = None):
        """stdVec.addScalar( scalar, [outputVec]) -> None
        Add scalar to each element of input vector. If an optional output
        vector is given, the output will be stored there, otherwise,
        this vector will change.
        In future, user can specify a subrange of the vector to add the
        scalar to; presently range args ignored.
        """
        if not outputVector:
            stdVector.add_scalar_vec( self._handle, self._handle,
                                      self._templateType, scalar)
        else:
            stdVector.add_scalar_vec( self._handle, outputVector._handle,
                                      self._templateType, scalar)
        return


    def multScalar( self, scalar, outputVector = None):
        """stdVec.multScalar( scalar, [outputVec]) -> None
        multiply each element of this vector by a scalar. If an optional
        output vector is given, the output will be stored there,
        otherwise, this vector will change.
        In future, user can specify a subrange of the vector to add the
        scalar to; presently range args ignored.
        """
        if not outputVector:
            stdVector.mult_scalar_vec( self._handle, self._handle,
                                       self._templateType, scalar)
        else:
            stdVector.mult_scalar_vec( self._handle, outputVector._handle,
                                       self._templateType, scalar)
        return
    

    # vector-vector arithmetic
    def plusEquals( self, rhs, startRHS = None, endRHS = None,
                    startLHS = None):
        """plusEquals( rhs, startRHS = None, endLHS = None, startLHS = None) -> None
        Add rhsVector elementwise to this vector. rhsVector must be same
        type. Can optionally specify a subrange of RHS, and the range of
        LHS to which it should be added. RHS range will default to
        [rhs.begin(), rhs.end() ); LHS start will default to self.begin()
        Inputs:
            rhs: Another StdVector object with same template type
            startRHS: offset of RHS vector start at.
            endRHS: one past the end of where to stop in RHS vector
            startLHS: where to start in LHS
        Output: None (results are added in place to self).
        Exceptions:
            ValueError, IndexError, TypeError
        """
        # check inputs, set defaults
        self._isCompatible( rhs)
        sRHS, eRHS, sLHS = \
            self._setVecVecDefaults( rhs, startRHS, endRHS, startLHS)

        stdVector.vectorPlusEquals( rhs.handle(), self.templateType(),
                                    self.handle(), sRHS, eRHS, sLHS)
        return


    def minusEquals( self, rhs, startRHS = None, endRHS = None,
                     startLHS = None):
        """minusEquals( rhs, startRHS = None, endLHS = None, startLHS = None) -> None
        Subtract rhsVector elementwise from this vector. rhsVector must be same
        type. Can optionally specify a subrange of RHS, and the range of
        LHS to which it should be added. RHS range will default to
        [rhs.begin(), rhs.end() ); LHS start will default to self.begin()
        Inputs:
            rhs: Another StdVector object with same template type
            startRHS: offset of RHS vector start at.
            endRHS: one past the end of where to stop in RHS vector
            startLHS: where to start in LHS
        Output: None (results are added in place to self).
        Exceptions:
            ValueError, IndexError, TypeError
        """
        # check inputs, set defaults
        self._isCompatible( rhs)
        sRHS, eRHS, sLHS = \
            self._setVecVecDefaults( rhs, startRHS, endRHS, startLHS)

        stdVector.vectorMinusEquals( rhs.handle(), self.templateType(),
                                    self.handle(), sRHS, eRHS, sLHS)
        return


    def timesEquals( self, rhs, startRHS = None, endRHS = None,
                     startLHS = None):
        """timesEquals( rhs, startRHS = None, endLHS = None, startLHS = None) -> None
        Multiply this vector elementwise by rhsVector. rhsVector must be 
        same type. Can optionally specify a subrange of RHS, and the
        range of LHS to which it should be added. RHS range will 
        default to [rhs.begin(), rhs.end() ); LHS start will
        default to self.begin().
        Inputs:
            rhs: Another StdVector object with same template type
            startRHS: offset of RHS vector start at.
            endRHS: one past the end of where to stop in RHS vector
            startLHS: where to start in LHS
        Output: None (results are added in place to self).
        Exceptions:
            ValueError, IndexError, TypeError
        """
        # check inputs, set defaults
        self._isCompatible( rhs)
        sRHS, eRHS, sLHS = \
            self._setVecVecDefaults( rhs, startRHS, endRHS, startLHS)

        stdVector.vectorTimesEquals( rhs.handle(), self.templateType(),
                                     self.handle(), sRHS, eRHS, sLHS)
        return
        
    
    def divideEquals( self, rhs, startRHS = None, endRHS = None,
                     startLHS = None):
        """timesEquals( rhs, startRHS = None, endLHS = None, startLHS = None) -> None
        Multiply this vector elementwise by rhsVector. rhsVector must be 
        same type. Can optionally specify a subrange of RHS, and the
        range of LHS to which it should be added. RHS range will 
        default to [rhs.begin(), rhs.end() ); LHS start will
        default to self.begin().
        Inputs:
            rhs: Another StdVector object with same template type
            startRHS: offset of RHS vector start at.
            endRHS: one past the end of where to stop in RHS vector
            startLHS: where to start in LHS
        Output: None (results are added in place to self).
        Exceptions:
            ValueError, IndexError, TypeError
        """
        # check inputs, set defaults
        self._isCompatible( rhs)
        sRHS, eRHS, sLHS = \
            self._setVecVecDefaults( rhs, startRHS, endRHS, startLHS)

        stdVector.vectorDivideEquals( rhs.handle(), self.templateType(),
                                      self.handle(), sRHS, eRHS, sLHS)
        return


    # Iterators
    def begin( self):
        """begin() -> TemplateCObject that wraps PyCObject that wraps
        std::vector<T>::iterator set to the beginning of this vector."""
        from StdVectorIterator import StdVectorIterator as svi
        hndl = stdVector.begin( self.handle(), self.datatype())
        debug.log( "handle = "+str( hndl))
        return svi( self, handle=hndl)

    
    def end( self):
        """end() -> TemplateCObject that wraps PyCObject that wraps
        std::vector<T>::iterator set to the end of this vector (one-past-the-
        last-element, as usual with STL)."""
        from StdVectorIterator import StdVectorIterator as svi
        hndl = stdVector.end( self.handle(), self.datatype())

        debug.log( "handle = "+str( hndl))

        return svi( self, handle=hndl)

    
    def iterator( self, offset):
        """iterator( offset) -> TemplateCObject that wraps PyCObject that wraps
        std::vector<T>::iterator set to the offset requested by user."""        
        from StdVectorIterator import StdVectorIterator as svi
        hndl = stdVector.iterator( self.handle(), self.datatype(), offset)

        debug.log( "handle = "+str( hndl))

        return svi( self, handle=hndl)


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
        i = stdVector.accumPlus( self._handle, self._templateType, start, end)
        return dx*i


    def square( self):
        """square() -> None
        Square each element of this vector.
        Inputs: None
        Output: None
        Exceptions: ValueError
        Notes: (1) To take the square of this vector and store the output
               in another vector (leaving this vector unchanged), please use
               square() function in stdVector module"""
        stdVector.square(  self._handle, self._handle, self._templateType)
        return
    
        
    def sqrt( self):
        """sqrt() -> None
        Take the square root of each element of this vector.
        Inputs: None
        Output: None
        Exceptions: ValueError
        Notes: (1) To take the sqrt of this vector and store the output
               in another vector (leaving this vector unchanged), please use
               sqrt() function in stdVector.__init__.py"""
        stdVector.sqrt(  self._handle, self._handle, self._templateType)
        return


    def sum( self, start, end):
        """sum(  start, end) -> \sum_{i in [start, end)}vec_i
        Add from start to (but not including) end.
        Inputs:
            start: index at which to begin (integer)
            end: index one past the last (integer)
        Output:
            \sum_{i in [start, end)}
        Exceptions: ValueError, IndexError
        Notes: end must be <= size of vector; start must be <= end."""
        return stdVector.accumPlus( self._handle, self._templateType,
                                    start, end)
    
        
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
        return stdVector.assign( self.handle(), self.templateType(), count,
                                 val)

    def asList( self):
        """asList() -> [This vector's contents in a Python list].
        """
        return stdVector.vector2pylist( self._handle, self._templateType)


    def asNumarray( self, dims=[]):
        """asNumarray() -> numarray
        Create a numarray object that looks at this vector's memory.
        Input:
            dims: list of dimensions for numarray shape. Default shape is 1d
                  with length of vector. Product of all dimensions must be
                  <= length of vector.
        Output:
            numarray.array object.
        Exceptions: TypeError, IndexError, RuntimeError
        Notes: Numarray must be installed.
        """

        dims = self.__numarrayDims( dims)

        debug.log( dims)
        
        numarray = stdVector.asNumarray( self._handle, self._templateType,
                                         dims)
        # give numarray a reference to this vector so this vector will live
        # at least as long as the user's view of it
        #numarray.__vector = self
        # for numpy array instance, the above line does not work

        _remember( numarray, self )
        return numarray


    def compare( self, other, epsilon = 0.000001):
        """compare( other, epsilon = 0.000001) -> Boolean
        Compare this vector elementwise with another vector. Returns True
        if the vectors have the same templateType, are both StdVector's,
        and are element-by-element equal to within epsilon.
        """
        import journal
        info = journal.info("ARCSStdVectorTest")
        
        if self.type() != other.type():
            info.log('CObject types don\'t agree')
            return False
        if self.templateType() != other.templateType():
            info.log('TemplateCObject types don\'t agree')
            return False
        ls =  self.asList()
        lo = other.asList()

        passed = True
        for i, num in enumerate(ls):
            if num + epsilon < lo[i] or num - epsilon > lo[i]:
                info.log("index " + str(i)+ ": self = " + str(num) \
                         + "; other = " + str( lo[i]))
                passed = False
        return passed


    def size( self):
        """size() -> number of elements.
        Invokes std::vector::size() on this instance's vector.
        """
        return stdVector.size( self.handle(), self.templateType())


    def voidPtr( self, offset = 0):
        """voidPtr( offset = 0) -> TemplateCObject with pointer to this
        StdVector's C array at specified offset. The template object type
        will be this vector's templateType, and the CObject type (class)
        will be "CArray".
        Inputs:
            offset (index into the array, integer)
        Output:
            TemplateCObject instance.
        Exceptions: ValueError, IndexError
        Notes: To pass the array pointer to an extension function expecting
        a C array, use tempCObj.handle().
        """
        arrayHandle = stdVector.voidPtr( self.handle(),
                                         self.templateType(), offset)
        return Template( self.templateType(), arrayHandle, "CArray")
    

    def __init__( self, typename_or_typecode, arg2, initVal=0, **kwds):
        """(1) StdVector( datatype, numList, **kwds)
        (2) StdVector( datatype, length, initVal=0, **kwds).
        
        Inputs (1):
            1. datatype (integer or string) recognized datatypes are
                float.......5
                double......6
                int........24
                unsigned...25
            2. list of numbers
            Possible keyword: 'handle': use this to construct a Python object
            that wraps an already existing vector
            
        Inputs (2):
            1. datatype (integer or string) recognized datatypes are
                float.......5
                double......6
                int........24
                unsigned...25
            2. length (integer > 0) length of vector to construct
            3. initial value to assign to all elements
        """

        # determine data type
        if isinstance(typename_or_typecode, str):
            typename = typename_or_typecode
            from array_kluge import types as aktypes
            try: typecode = aktypes[typename]
            except KeyError: raise ValueError , "unknown data type name: %s" % typename
            
        elif isinstance(typename_or_typecode, int):
            typecode = typename_or_typecode
            
        else:
            raise ValueError, "unknown data type" % typename_or_typecode
        
        # create handle
        if 'handle' in kwds.keys():
            # this is an unusual case. it is only used when developer
            # want to use an existing handle to the stdVector c++ instance
            # only use this if you really know what is going on
            debug.log("using handle keyword")
            handle = kwds['handle']
            
        elif '__iter__' in dir( arg2):
            # arg2 is a list-like thing
            arg2 = list(arg2)
            if initVal != 0 or kwds != {}: raise ValueError , \
               "vector( datatype, list ) is good enough, vector( %s, %s, initVal = %s, kwds = %s ) is overwhelming" % (typecode, arg2, initVal, kwds )
            debug.log("calling pylist2vector 1")
            handle = stdVector.pylist2vector( arg2, typecode)
            
        elif isinstance(arg2, str):
            # arg2 is a string
            if initVal != 0 or kwds != {}: raise ValueError , \
               "vector( 'char', string ) is good enough, vector( %s, %s, initVal = %s, kwds = %s ) is overwhelming" % (typecode, arg2, initVal, kwds )
            debug.log("calling pylist2vector 2")
            handle = stdVector.pylist2vector( arg2, typecode)
            
        elif isInteger( arg2 ):
            # arg2 must be an integer. arg2 is number of elements in the new vector
            # initVal is value for every new element
            debug.log("calling vector ctor")
            handle = stdVector.stdVector_ctor( typecode, arg2, initVal)

        else:
            raise ValueError , "don't know how to create vector from %s" % \
                  { "typecode": typecode,
                    "arg2": arg2,
                    "initVal" : initVal,
                    "other keywords" : kwds }
        
        Template.__init__( self, typecode, handle, "StdVector")

        self._shape = self.size(),
        return


    def _journal(self):
        if '_debug' not in dir(self):
            import journal
            self._debug = journal.debug("StdVectorPy")
        return
            

##     def _isCompatible( self, other):
##         if self.templateType() != other.templateType():
##             msg = "template (data) types do not agree, this obj's type ="
##             msg += str( self.templateType()) + ", other's type = "
##             msg += str( other.templateType())
##             raise TypeError, msg
##         if self.type() != other.type():
##             msg = "C++ class types do not agree, this object's type ="
##             msg += str( self.templateType()) + ", other's type = "
##             msg += str( other.templateType())
##             raise TypeError, msg
##         return


    def _setVecVecDefaults( self, rhs, startRHS, endRHS, startLHS):
        if not startRHS:
            startRHS = 0; endRHS = rhs.size(); startLHS = 0
        elif not endRHS:
            endRHS = rhs.size(); startLHS = 0
        elif not startLHS:
            startLHS = 0
        return startRHS, endRHS, startLHS
        

    def __numarrayDims( self, dims):
        """Check user-specified dimensions, supply default dimension"""
        #default
        if not dims:
            dims = [ self.size() ]
            pass 

        dims1 = [ int(dim) for dim in dims ]

        for dim, dim1 in zip(dims, dims1):
            if (dim/dim1) == 1 : continue
            msg = 'Cannot convert given dimensions to sth acceptable by numpy: %s' % (
                dims, )
            raise ValueError, msg
        
        return dims1


    #pickle interface    
    def __getstate__(self):
        data = self.asNumarray().copy()
        return self.datatype(), data

    def __setstate__(self, inputs):
        datatype, data = inputs
        size = len(data)
        initVal = 0
        handle = stdVector.stdVector_ctor( datatype, size, initVal)
        Template.__init__( self, datatype, handle, "StdVector")
        self.asNumarray()[:] = data
        return

    # End class StdVector


def isInteger( n ):
    return isinstance(n, int ) or isinstance( n, long )


#before, we can attach a stdVector instance to a numpy array instance
#when asNumarray is called. But now numpy array instance does not allow
#attachments any more. so we use weakref to keep references to vectors
#for which "asNumarray" has been called.
#We should have used numpy array as key, but numpy array is not hashable,
#so we have to use numpy array as value, and use WeakValueDictionary
import weakref
_weakmap = weakref.WeakValueDictionary()
def _remember( arr, vector ):
    _weakmap[ vector, id(arr) ] = arr
    return

# version
__id__ = "$Id: StdVector.py 144 2007-12-11 16:51:23Z linjiao $"

# End of file
