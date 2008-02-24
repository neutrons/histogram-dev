#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               T. M. Kelley
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \mainpage stdVector
##
## This package provides bindings to std::vector<T> c++ template
##
## Python is a dynamic typing language while c++ is a static typing language.
## This mismatch causes difficulties in binding c++ templates to python.
## The approach here is to carry a "type code" with the python object
## containing the handle to the underlying c++ object.
##
## Type checking for StdVector instances in the python layer
## happens in two classes: CObject and TemplateCObject.
##
## Class CObject is used to wrap instances of any c++ class, by
## keeping track of class name.
##
## Class TemplateCObject is used to wrap instances of any
## c++ template class. It is a subclass of CObject, and it keeps
## track of both the class name and the template type name.
##
## StdVector.StdVector class is a subclass of TemplateCObject.
##
## The rest of this package is more-or-less routine. Funtions in c++
## layer are exported to python layer and wrapped into class StdVector.StdVector.
##


from StdVector import StdVector
import journal
debug = journal.debug("stdVector.__init__")


vector = StdVector


# vector-vector arithmetic

def add( vector1, vector2, output, startRHS=0, endRHS=0, startLHS=0):
    """add( vector1, vector2, output, startRHS=0, endRHS=0, startLHS=0) -> None
    Add rhs_vector1[start_rhs:end_rhs) to rhs_vector2[start_rhs:end_rhs),
    assigning to lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs)).
    Inputs:
        vector1, vector2, output: StdVector objects
        start_rhs (start of rhs range)
        end_rhs   (one-past the end of the rhs range)
        start_lhs (start of lhs range)
    Output:
        None
    Exceptions: ValueError, IndexError
    Notes: (1) Read myVector[a:b) as first in range is myVector[a], last is
    myVector[b-1]
    (2) All vectors must be same type, otherwise should get TypeError."""
    
    import stdVector
    if endRHS == 0:
        endRHS = vector1.size()
    return stdVector.vectorPlus( vector1._handle, vector2._handle,
                                 output._handle, vector1._templateType,
                                 startRHS, endRHS, startLHS)


def subtract( vector1, vector2, output, startRHS=0, endRHS=0, startLHS=0):
    """subtract( vector1, vector2, output, startRHS=0, endRHS=0, startLHS=0) -> None
    Subtract rhs_vector1[start_rhs:end_rhs) frm rhs_vector2[start_rhs:end_rhs),
    assigning to lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs)).
    Inputs:
        vector1, vector2, output: StdVector objects
        start_rhs (start of rhs range)
        end_rhs   (one-past the end of the rhs range)
        start_lhs (start of lhs range)
    Output:
        None
    Exceptions: ValueError, IndexError
    Notes: (1) Read myVector[a:b) as first in range is myVector[a], last is
    myVector[b-1]
    (2) All vectors must be same type, otherwise should get TypeError."""
    
    import stdVector
    if endRHS == 0:
        endRHS = vector1.size()
    return stdVector.vectorMinus( vector1._handle, vector2._handle,
                                  output._handle, vector1._templateType,
                                  startRHS, endRHS, startLHS)


def multiply( vector1, vector2, output, startRHS=0, endRHS=0, startLHS=0):
    """multiply( vector1, vector2, output, startRHS=0, endRHS=0, startLHS=0) -> None
    Multiply rhs_vector1[start_rhs:end_rhs) by rhs_vector2[start_rhs:end_rhs),
    assigning to lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs)).
    Inputs:
        vector1, vector2, output: StdVector objects
        start_rhs (start of rhs range)
        end_rhs   (one-past the end of the rhs range)
        start_lhs (start of lhs range)
    Output:
        None
    Exceptions: ValueError, IndexError
    Notes: (1) Read myVector[a:b) as first in range is myVector[a], last is
    myVector[b-1]
    (2) All vectors must be same type, otherwise should get TypeError."""
    
    import stdVector
    if endRHS == 0:
        endRHS = vector1.size()
    return stdVector.vectorTimes( vector1._handle, vector2._handle,
                                  output._handle, vector1._templateType,
                                  startRHS, endRHS, startLHS)


def divide( vector1, vector2, output, startRHS=0, endRHS=0, startLHS=0):
    """divide( vector1, vector2, output, startRHS=0, endRHS=0, startLHS=0) -> None
    Divide rhs_vector1[start_rhs:end_rhs) by rhs_vector2[start_rhs:end_rhs),
    assigning to lhs_vector[start_lhs:start_lhs+(end_rhs-start_rhs)).
    Inputs:
        vector1, vector2, output: StdVector objects
        start_rhs (start of rhs range)
        end_rhs   (one-past the end of the rhs range)
        start_lhs (start of lhs range)
    Output:
        None
    Exceptions: ValueError, IndexError
    Notes: (1) Read myVector[a:b) as first in range is myVector[a], last is
    myVector[b-1]
    (2) All vectors must be same type, otherwise should get TypeError."""
    
    import stdVector
    if endRHS == 0:
        endRHS = vector1.size()
    return stdVector.vectorDivide( vector1._handle, vector2._handle,
                                   output._handle, vector1._templateType,
                                   startRHS, endRHS, startLHS)


# other things to do with vectors:

def average( vector, start, end):
    """average( vector, start, end) -> None
    average the vector from index start to but not including index end.
    """
    import stdVector
    cumm = stdVector.accumPlus( vector._handle, vector._templateType, start, end)
    return cumm/(end-start)
    
    
def castCopy( vec1, vec2):
    """castCopy( stdvec1, stdvec2) -> None
    Copy vector 1 to vector 2, casting from the type of vector 1 to the type
    for vector 2. If vector 2 does not have the same size as vector 1,
    then vector 2 will be resized to vector1.size().
    Inputs:
        vec1: StdVector instance
        vec2: StdVector instance
    Output:
        None
    Exceptions: ValueError if either vector's stated type is unrecognized in
    the bindings layer; TypeError if either vector's stated type doesn't match
    the encoded type.
    """
    import stdVector
    stdVector.vectorCast( vec1.handle(), vec1.templateType(),
                          vec2.handle(), vec2.templateType())
    return


def copy( vector):
    """copy( vector) -> new vector
    Create a new (deep) copy of vector.
    Input:
        StdVector instance
    Output:
        new StdVector instance
    Exceptions: ValueError, RuntimeError
    Notes: calls the std::vector copy ctor."""

    debug.log("calling stdVector_copy_ctor1")
    
    handle =  stdVector.stdVector_copy_ctor1( vector._templateType,
                                              vector._handle)
    from StdVector import StdVector
    debug.log("handing off to StdVector ctor")
    return StdVector( vector._templateType, vector.size(), handle=handle)


def extractSlice( slce, invec, outvec = None):
    """extractSlice( slice, inputVector, outputVector=None) -> vector w/ slice
    get a slice from inputVector, put it into a vector and return it.
    Input:
        slice: stdVector.Slice instance
        inputVector: vector to take slice from
        outputVector: vector to load slice into (optional, see below)
    Output:
        vector holding slice. If outputVector was furnished, this is returned
    Exceptions: TypeError, ValueError
    Notes: If no outputVector is provided, one will be allocated. This should
    be avoided for best performance."""
    if not outvec:
        outvec = vector( invec.datatype(), slce.size())
        debug.log("called vector ctor ")
    stdVector.extractSlice( invec._handle, invec._templateType, outvec._handle,
                            slce._handle)
    return outvec


def reduceSum2d( vector2d, sizes, vector1d, whichAxis):
    """reduceSum2d( vector2d, sizes, vector1d, whichAxis) --> None
    Sum the 2dvec over whichAxis into the 1dvec.
    inputs:
        vector2d (source; std::vector<datatype, PyCObject)
        sizes (list of integers, length of each dimension of vector3d)
        vector1d (target; std::vector<datatype, PyCObject)
        whichAxis (which axis is being summed over; int = 1 or 2)
    outputs: None
    Exceptions: ValueError
    Notes: 1) Datatypes must match.
    2) Sizes means the lengths of each axis of your 2-d array;
    the product must equal the total length of the 2d-vector.
    3) Axis numbering: 1 means the slower running index; 2 the faster.
    In the C style of indexing, this means the leftmost index."""
    import stdVector
    if vector2d.datatype() != vector1d.datatype():
        raise TypeError,'vector datatypes do not match'
    stdVector.ReduceSum2d( vector2d.handle(), vector2d.datatype(),
                                 vector1d.handle(), sizes, whichAxis)
    return


def reduceSum3d( vector3d, sizes, vector2d, whichAxis):
    """reduceSum3d( vector3d, sizes, vector2d, whichAxis) --> None
    Sum vector3d with dimensions lengths sizes over whichAxis into the vector3d.
    inputs:
        vector3d (source; StdVector)
        sizes (list of integers, length of each dimension of vector3d)
        vector2d (target; StdVector)
        whichAxis (which axis is being summed over; int = 1-3; 1 runs slowest)
    outputs: None
    Exceptions: ValueError, TypeError
    Notes: 1) Datatypes must match.
    2) Length of vector2d must equal product of the two axes not reduced; the
    product of all three axes must equal the length of the 3d-vector.
    3) Axis numbering: 1 means the slowest running index; 3 the fastest.
    In the C style of indexing, 1 means the leftmost index, 3 the rightmost."""
    import stdVector
    if vector3d.datatype() != vector2d.datatype():
        print vector3d.datatype(), vector2d.datatype()
        raise TypeError,'vector datatypes do not match'
    stdVector.ReduceSum3d( vector3d.handle(), vector3d.datatype(),
                                 vector2d.handle(), sizes, whichAxis)
    return


def square( invec, outvec=None):
    """square( inputVector, outputVector = None) -> None
    assign the square of each element of inputVector to corresponding element
    of outputVector. If no outputVector is given, the result will be placed
    in inputVector.
    Inputs:
        inputVector: StdVector instance
        outputVector: StdVector instance (defaults to None)
    Output:
        outputVector
    Exceptions: ValueError, IndexError
    Notes: """
    if not outvec:
        outvec = invec
    import stdVector
    stdVector.square( invec.handle(), outvec.handle(), invec.datatype())
    return outvec


def sqrt( invec, outvec = None):
    """sqrt( invec, outvec = invec) -> None
    Take square root of each element of invec, and load it into the
    corresponding position of outvec. Will resize outvec to match invec, note
    this destroys/invalidates all iterators, pointers, etc on outvec.
    """
    if not outvec:
        outvec = invec
    import stdVector
    stdVector.sqrt( invec.handle(), outvec.handle(), invec.datatype())
    return


# etc.
def copyright():
    return "stdVector pyre module: Copyright (c) 2004-2005 T. M. Kelley";
    

# version
__id__ = "$Id: __init__.py 134 2006-10-09 15:21:57Z linjiao $"

#  End of file 
