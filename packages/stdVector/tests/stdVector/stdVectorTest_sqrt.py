#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "with single precision floats",
    "with double precision floats",
    "using sqrt function in package init",
    "using sqrt function in package init, different output",
    ]

from stdVector import vector


def test_0( **kwds):

    v = vector( 5, 10, 4.0)
    v.sqrt()

    expected = [2.0 for i in range(10)]
    passed = utilities.compareFPLists( expected, v.asList(), 1e-20, log)
    return passed

    
def test_1( **kwds):

    v = vector( 6, 10, 4.0)
    v.sqrt()

    expected = [2.0 for i in range(10)]
    passed = utilities.compareFPLists( expected, v.asList(), 1e-20, log)
    return passed

    
def test_2( **kwds):

    import stdVector

    v = vector( 6, 10, 4.0)
    stdVector.sqrt( v)

    expected = [2.0 for i in range(10)]
    passed = utilities.compareFPLists( expected, v.asList(), 1e-20, log)
    return passed

    
def test_3( **kwds):

    import stdVector

    v = vector( 6, 10, 4.0)
    vout = vector( 6, 10, 0.0)
    stdVector.sqrt( v, vout)

    expectedOut = [2.0 for i in range(10)]
    expectedIn  = [4.0 for i in range(10)]
    passedOut = utilities.compareFPLists( expectedOut, vout.asList(),
                                          1e-20, log)
    passedIn = utilities.compareFPLists( expectedIn, v.asList(), 1e-20, log)

    log("output correct: %s" % passedOut)
    log("input unchanged: %s" % passedIn)
    return passedOut and passedIn

    
# ------------- do not modify below this line ---------------


def run( **kwds):
    
    allPassed = True
    
    for i, aspect in enumerate( aspects):
        run = eval( 'test_' + str(i))
        utilities.preReport( log, target, aspect)
        passed = run( **kwds)
        utilities.postReport( log, target, aspect, passed)
        allPassed = allPassed and passed

    return allPassed


import  utilities

target = "sqrt"

log = utilities.picklog()

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id: stdVectorTest_sqrt.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file

