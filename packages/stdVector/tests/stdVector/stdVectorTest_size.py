#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import vector
from utilities import picklog, preReport, postReport
log = picklog()

target = "size"

aspects = ["simple test, template type double"]

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
    v = vector( 5, [3.14159]*sz)
    sz2 = v.size()
    return sz == sz2
    

if __name__ == '__main__':
    import journal
    info = journal.info("ARCSStdVectorTest")
    info.activate()
    
    run()

    
# version
__id__ = "$Id: stdVectorTest_size.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
