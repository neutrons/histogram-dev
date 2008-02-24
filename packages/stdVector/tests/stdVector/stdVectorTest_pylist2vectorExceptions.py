#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import stdVector as sv
from utilities import picklog, preReport, postReport
log = picklog()

aspects = [
    "exception: pass arg 1 not list",
    "exception: pass arg 2 unsupported datatype",
    ]


target = "test_stdVector"

def run():

    trgt = "pylist2vector"
    
    allPassed = True    
    allPassed = allPassed and test_p2vE1( trgt)
    allPassed = allPassed and test_p2vE2( trgt)
    
    return allPassed


def test_0( ):
    aspect = "exception: pass arg 1 not list"
    preReport( log, target, aspect)
    try:
        sv.pylist2vector( 3.14159, 3)
        passed = False
    except TypeError, msg:
        log("Caught TypeError with this message:\n" + str(msg))
        passed = True
    postReport( log, target, aspect, passed)
    return passed


def test_1( ):
    aspect = "exception: pass arg 2 unsupported datatype"
    preReport( log, target, aspect)
    try:
        sv.pylist2vector( [1,2,3], 3)
        passed = False
    except ValueError, msg:
        log("Caught ValueError with this message:\n" + str(msg))
        passed = True
    postReport( log, target, aspect, passed)
    return passed




# version
__id__ = "$Id: stdVectorTest_pylist2vectorExceptions.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
