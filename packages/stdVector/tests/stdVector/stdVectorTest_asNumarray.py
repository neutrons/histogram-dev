#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "simple test",
    "check numpy array class",
    "type float",
    "type double",
    "type int",
    "type unsigned",
    "delete numpy array: vector okay?",
#    "delete vector: numpy array not okay?", # How should this work??
    ]

import stdVector as sv
import journal
journal.debug("StdVectorPy").activate()


def test_0( **kwds):

    vec = sv.vector( 6, 10, 3.14159)
    log("vector as list: %s" % vec.asList())
        
    na = vec.asNumarray()

    log("vector as numpy array: %s" % na)

    log("dir(numpy array): %s" % dir(na))
    log("type(numpy array): %s" % str(type(na)))

    from numpy import array
    a = array([1])
    log("type of a regular numpy array: %s" % str(type(a)))
    return True


def test_1( **kwds):
    vec = sv.vector( 6, 10, 3.14159)
    na = vec.asNumarray()
    from numpy import array
    a = array([1])

    passed = (type(na) == type(a))
    if not passed:
        log("type from asNumarray: %s" % str( type( na)))
        log("type from numpy array: %s" % str( type( a)))
    return passed
    
    
def test_2( **kwds):
    vec = sv.vector( 5, 10, 3.14159)
    na = vec.asNumarray()

    log("checking type")
    log("numpy array type: %s; numpy array typecode: %s" % \
        (na.dtype.name, na.dtype.kind))
    passed = ( na.dtype.name == 'float32')
    if not passed:
        log("type was not float32")

    log("comparing as lists")
    passed = passed and utilities.compareFPLists( na.tolist(), vec.asList(),
                                                  1.e-15, log)
    return passed


def test_3( **kwds):
    vec = sv.vector( 6, 10, 3.14159)
    na = vec.asNumarray()

    log("checking type")
    log("numpy array type: %s; numpy array typecode: %s" % \
        (na.dtype.name, na.dtype.kind))
    passed = ( na.dtype.name == 'float64')
    if not passed:
        log("type was not float64")

    log("comparing as lists")
    passed = passed and utilities.compareFPLists( na.tolist(), vec.asList(),
                                                  1.e-15, log)
    return passed


def test_4( **kwds):
    vec = sv.vector( 24, 10, 3.14159)
    na = vec.asNumarray()

    log("checking type")
    log("numpy array type: %s; numpy array typecode: %s" % \
        (na.dtype.name, na.dtype ))
    passed = ( na.dtype.name == 'int32')
    if not passed:
        log("type was not int32")

    log("comparing as lists")
    passed = passed and utilities.compareFPLists( na.tolist(), vec.asList(),
                                                  1.e-15, log)
    return passed


def test_5( **kwds):
    vec = sv.vector( 25, 10, 3.14159)
    na = vec.asNumarray()

    log("checking type")
    log("numpy array type: %s; numpy array typecode: %s" % \
        (na.dtype.name, na.dtype.kind))
    passed = ( na.dtype.name == 'uint32')
    if not passed:
        log("type was not uint32")

    log("comparing as lists")
    passed = passed and utilities.compareFPLists( na.tolist(), vec.asList(),
                                                  1.e-15, log)
    return passed


def test_6( **kwds):
    vec = sv.vector( 25, 10, 3.14159)
    na = vec.asNumarray()

    del na

    log("vector as list after 'del na': %s" % vec.asList())

    del vec
    
    log("deleted vector after 'del na'")

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


import  utilities

target = "asNumarray"

log = utilities.picklog()

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id: stdVectorTest_asNumarray.py 126 2006-08-23 22:55:32Z linjiao $"

# End of file

