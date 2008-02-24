#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import vector
from utilities import picklog, preReport, postReport
log = picklog()

target = "Iterator"

import journal
info = journal.info("ARCSStdVectorTest")
info.activate()
debug = journal.debug("ARCSStdVectorTest")
#debug.activate()
debugasv = journal.debug("ARCSStdVector") #C++ journals
#debugasv.activate()
debugasvp = journal.debug("StdVectorPy") # Python classes
#debugasvp.activate()

aspects = [
    "direct test of begin(), simple call",
    "StdVector.begin() simple call",
    "direct test of end(), simple call",
    "StdVector.end() simple call",
    "direct test of iterator(), simple call",
    "StdVector.iterator(), simple call",
    "direct test of iteratorsEqual()",
    "StdVectorIterator.equal() simple call",
    "direct test of increment()",
    "StdVectorIterator.increment() simple call",
    "combining begin, end, equal, increment"
    ]

def run():

    allPassed = True
    
    for i, aspect in enumerate( aspects):
        run = eval( 'test_' + str(i))
        preReport( log, target, aspect)
        passed = run()
        postReport( log, target, aspect, passed)
        allPassed = allPassed and passed

##     preReport( log, target, aspects[0])
##     passed = test_3()
##     postReport( log, target, aspects[0], passed)

    return allPassed


def test_0():
    sz = 4; dtype = 6
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( dtype, inlist)

    from stdVector import stdVector as sv
    vit = sv.begin( v.handle(), v.datatype())

    debug.log( "Result:" + str( vit))

    info.log("Contents of first "+str(sz) +" places pointed to by iter:")
    sv.printIterator( vit, dtype, sz)
    info.log( "Should be " + str(inlist))

    return True


def test_1():
    # Can run StrdVector.begin()?
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)
    vit = v.begin()

    debug.log( str(vit.handle())+" " + str( vit.datatype()) + " " +
               str(sz))

    from stdVector import stdVector as sv
    info.log("Contents of first "+str(sz) +" places pointed to by iter:")
    sv.printIterator( vit.handle(), vit.datatype(), sz)
    info.log( "Should be " + str(inlist))

    return True


def test_2():
    #Can run stdVector.end()?
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)

    from stdVector import stdVector as sv
    vit = sv.end( v.handle(), v.datatype())

    debug.log( "StdVectorIterator handle: " + str( vit))

    return True


def test_3():
    #Can run StdVector.end()?
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)
    vit = v.end()

    debug.log( "StdVectorIterator handle: " + str( vit.handle() ))
    debug.log( "datatype: " + str( vit.datatype() ))

    return True


def test_4():
    #Can run stdVector.iterator()
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)

    from stdVector import stdVector as sv
    vit = sv.iterator( v.handle(), v.datatype(), 0)
    return True


def test_5():
    #Can run StdVector.iterator()
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)

    from stdVector import stdVector as sv
    vit = v.iterator( 0)
    return True


def test_6():
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)
    vit = v.end()
    from stdVector import stdVector as sv
    passed = sv.iteratorsEqual( vit.handle(), vit.handle(), vit.datatype())
    
    debug.log( "Iterator equals itself? " + str( passed))
    return passed

def test_7():
    #Can run StdVectorIterator.equal()
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)

    from stdVector import stdVector as sv
    vit1 = v.iterator( 0)
    vit2 = v.iterator( 0)
    
    return vit1.equal( vit2)


def test_8():
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)
    vitb = v.begin()

    from stdVector import stdVector as sv
    for i in range( sz):
        sv.printIterator( vitb.handle(), vitb.datatype(), 1)
        sv.increment( vitb.handle(), vitb.datatype())
    return True


def test_9():
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)
    vitb = v.begin()

    from stdVector import stdVector as sv
    for i in range( sz):
        sv.printIterator( vitb.handle(), vitb.datatype(), 1)
        vitb.incr()
    return True


def test_10():
    sz = 4
    inlist = [3.14159, 4.14159, 5.14159, 6.14159]
    v = vector( 6, inlist)
    vitb = v.begin()
    vite = v.end()
    from stdVector import stdVector as sv
    while not vitb.equal( vite):
        sv.printIterator( vitb.handle(), vitb.datatype(), 1)
        vitb.incr()
    return True


if __name__ == '__main__':
    passed = run()
    if passed:
        print "All tests of stdVectorIterator PASSED"
    else:
        print "Some/all tests of stdVectorIterator FAILED"
    #end
    
# version
__id__ = "$Id: stdVectorTest_iterators.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file
