#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

from stdVector import vector
import stdVector

aspects = [
    "simple test, template type float",
    "simple test, template type unsigned"
    ]


def test_0():
    v1 = vector( 5, [3.14]*3)
    v2 = vector( 5, [2.0]*3)
    stdVector.multiply( v1, v2, v1)
    v3 = vector( 5, [6.28]*3)
    return v1.compare( v3)
    

def test_1():
    v1 = vector( 24, [42]*3)
    v2 = vector( 24, [2]*3)
    stdVector.multiply( v1, v2, v1)
    v3 = vector( 24, [84]*3)
    return v1.compare(v3)

    
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

target = "multiply"

log = utilities.picklog()

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id: stdVectorTest_multiply.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file

