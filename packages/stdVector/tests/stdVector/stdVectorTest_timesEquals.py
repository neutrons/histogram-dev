#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import vector
from utilities import picklog, preReport, postReport
log = picklog()

target = "timesEquals"
aspects = ["simple test, template type float",
           "simple test, template type unsigned"]


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
    v = vector( 5, [3.14]*3)
    v2 = vector( 5, [2.0]*3)
    v.timesEquals( v2)
    v3 = vector( 5, [6.28]*3)
    return v.compare( v3)
    

def test_1():
    v = vector( 24, [42]*3)
    v2 = vector( 24, [2]*3)
    v.timesEquals( v2)
    v3 = vector( 24, [84]*3)
    return v.compare(v3)
    

if __name__ == '__main__':
    import journal
    info = journal.info("ARCSStdVectorTest")
    info.activate()
    
    run()

    
# version
__id__ = "$Id: stdVectorTest_timesEquals.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
