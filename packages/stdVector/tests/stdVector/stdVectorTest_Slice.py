#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "instantiate/initialize",
    "extractSlice"
    ]


from stdVector.Slice import Slice
import stdVector


def test_0( **kwds):

    slc = Slice( 2,3,3)

    return True


def test_1( **kwds):

    slc = Slice( 3,3,3)
    v1 = stdVector.vector( 6, [1.0*i for i in range(10)])
    v2 = stdVector.vector( 6, 3)

    stdVector.extractSlice( slc, v1, v2)

    expected = stdVector.vector( 6, [3.0, 6.0, 9.0])
    return utilities.compareFPLists( expected.asList(), v2.asList(),
                                     1.0e-20, log)

    
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

target = "Slice"

log = utilities.picklog( )

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()

    journal.debug("stdVector").activate()
    run()

# version
__id__ = "$Id: stdVectorTest_Slice.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file

