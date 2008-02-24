#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "simple test of integrate"
    ]


def test_0( **kwds):

    from stdVector import vector
    vec = vector( 6, [i+1.0 for i in range(10)])

    result = vec.integrate( 0, 10, 0.5)
    answer = 27.5
    passed = True
    epsilon = 1e-20
    if result + epsilon < answer or result - epsilon > answer:
        passed = False
        log("result was %s instead of %s" % (result, answer))
    return passed

    
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

target = "integrate"

log = utilities.picklog()

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id: stdVectorTest_integrate.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file

