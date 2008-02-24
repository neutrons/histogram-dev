#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "convert small vector to numpy array"
    ]


from stdVector import stdVector as sv

dtype = 6


def test_0( **kwds):

    handle = sv.stdVector_ctor( dtype, 10, 3.14159)

    na = sv.asNumarray( handle, dtype, [10])
    log("You should see [ 3.14159  3.14159  3.14159  3.14159  3.14159  3.14159  3.14159  3.14159  3.14159  3.14159]")
    log(na)

    log("type(na): %s" % type(na))

    return True

    
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


import ARCSTest.utilities as utilities

target = "asNumarray"

log = utilities.picklog( target)

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id: stdvecmodTest_asNumarray.py 124 2006-08-06 17:59:20Z linjiao $"

# End of file

