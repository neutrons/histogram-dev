#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import vector
from utilities import picklog, preReport, postReport
log = picklog()

target = "voidPtr"

aspects = ["simple test, template type double", "testing offset = 1"]
    
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
    sz = 4
    v = vector( 6, [3.14159, 4.14159, 5.14159, 6.14159])
    vptr1 = v.voidPtr()
    from stdVector import stdVector as sv
    sv.printCArray( vptr1.handle(), sz)
    return True
    

def test_1():
    sz = 4
    v = vector( 6, [3.14159, 4.14159, 5.14159, 6.14159])
    vptr1 = v.voidPtr(1)
    from stdVector.stdVector import printCArray
    printCArray( vptr1.handle(), 3)
    return True


if __name__ == '__main__':
    import journal
    info = journal.info("ARCSStdVectorTest")
    info.activate()
    
    run()

    
# version
__id__ = "$Id: stdVectorTest_voidPtr.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
