#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import vector
from utilities import picklog, preReport, postReport
log = picklog()

target = "multScalar"

aspects = ["simple test, template type double",
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
    v2 = vector( 5, [6.28]*3)
    v.multScalar( 2.0)
    return v.compare(v2)
    

def test_1():
    v = vector( 24, [42]*3)
    v2 = vector( 24, [84]*3)
    v.multScalar( 2)
    return v.compare(v2)
    

if __name__ == '__main__':
    import journal
    info = journal.info("ARCSStdVectorTest")
    info.activate()
    
    run()

    
# version
__id__ = "$Id: stdVectorTest_multScalar.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
