#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import stdVector as sv
from utilities import picklog, preReport, postReport
log = picklog()


aspects = [
    "exception: pass arg 1 not PyCObject",
    "exception: pass arg 2 unrecognized datatype",
    "exception: pass PyCObject wrapping non std::vector",
    "exception: pass PyCObject wrapping std::vector, wrong datatype",
    ]


target = "test_stdVector"

def run():
    allPassed = True
    trgt = "vector2pylist"
    allPassed = allPassed and test_v2pE1( trgt)
    allPassed = allPassed and test_v2pE2( trgt)
    allPassed = allPassed and test_v2pE3( trgt)
    allPassed = allPassed and test_v2pE4( trgt)
    return allPassed


def test_0( ):
    aspect = "exception: pass arg 1 not PyCObject"
    preReport( log, target, aspect)
    try:
        sv.vector2pylist( 3.14159, 3)
        passed = False
    except TypeError, msg:
        log("Caught TypeError with this message:\n" + str(msg))
        passed = True
    postReport( log, target, aspect, passed)
    return passed


def test_1( ):
    aspect = "exception: pass arg 2 unrecognized datatype"
    preReport( log, target, aspect)
    try:
        a = sv.testcobj()
        sv.vector2pylist( a, 3)
        passed = False
    except ValueError, msg:
        log("Caught ValueError with this message:\n" + str(msg))
        passed = True 
    postReport( log, target, aspect, passed)
    return passed


def test_2( ):
    aspect = "exception: pass PyCObject wrapping non std::vector"
    preReport( log, target, aspect)
    try:
        a = sv.testcobj()
        sv.vector2pylist( a, 5)
        passed = False
    except TypeError, msg:
        log("Caught TypeError with this message:\n" + str(msg))
        passed = True 
    postReport( log, target, aspect, passed)
    return passed


def test_3( ):
    aspect = "exception: pass PyCObject wrapping std::vector, wrong datatype"
    preReport( log, target, aspect)
    try:
        a = sv.pylist2vector( [1,2,3], 6)
        sv.vector2pylist( a, 5)
        passed = False
    except TypeError, msg:
        log("Caught TypeError with this message:\n" + str(msg))
        passed = True 
    postReport( log, target, aspect, passed)
    return passed


# version
__id__ = "$Id: stdVectorTest_vector2pylistExceptions.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
