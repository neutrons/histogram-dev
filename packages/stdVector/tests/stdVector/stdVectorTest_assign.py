#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import vector
from utilities import picklog, preReport, postReport
log = picklog()
from stdVector import stdVector as sv

target = "assign"

aspects = ["rewrite same size", "rewrite none", "rewrite more"]


def run():
    
    allPassed = True
    
    for i, aspect in enumerate( aspects):
        run = eval( 'test_' + str(i))
        preReport( log, target, aspect)
        passed = run()
        postReport( log, target, aspect, passed)
        allPassed = allPassed and passed

    return allPassed


def test_0():
    s = vector( 6, [1., 2.,3.])
    s.assign( s.size(), 2.3)
    s2 = vector( 6, [2.3]*3)
    return s.compare( s2)
    

def test_1():
    s = vector( 6, [1., 2., 3.])
    s.assign( 0, 2.3)
    s2 = vector( 6, [])
    return s.compare( s2)


def test_2():
    s = vector( 6, [1., 2., 3.])
    s.assign( 10, 2.3)
    s2 = vector( 6, [2.3]*10)
    return s.compare( s2)


if __name__ == '__main__':
    import journal
    info = journal.info("ARCSStdVectorTest")
    info.activate()
    
    run()

    
# version
__id__ = "$Id: stdVectorTest_assign.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
