#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "instantiate/initialize",
    "attribute()", # relies on correct initialization
    "setAttribute()", # relies on correct attribute()
    "listAttribute()", # relies on correct initialization
    "name()",
    "shape()",
    "storage()",
    "typecode()",
    "typecodeAsC()",
    "typecodeAsNA()",
    "typecodeAsStdVector()",
    "unit()",
    "two datasets",
    ]


def test_0( **kwds):

    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    if ds._shape is not shape:
        passed = False
        log("dataset._shape not identical to shape")
    if ds._storage is not storage:
        passed = False
        log("dataset._storage not identical to storage")
    if ds._typecode != dtype:
        passed = False
        log("dataset._typecode was %s, not %s" % (ds._typecode, dtype))
    attList = [3.14159, 'name', 'nifty', 'pi', 'plottable', 'unit']
    acList = ds._attributeCont._attributes.keys()
    acList.sort()
    if acList != attList:
        passed = False
        log("attribute keys were %s, should have been %s" % ( acList, attList))
    return passed

    
def test_1( **kwds):
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    dsNifty = ds.attribute('nifty')
    if dsNifty is not False:
        passed = False
        log("ds attribute 'nifty' was not False, instead was %s" % dsNifty)
    dspi = ds.attribute('pi')
    if dspi != 3.14159:
        passed = False
        log("ds attribute 'pi' was %s instead of 3.14159" % dspi)
    ds42 = ds.attribute( 42)
    if ds42 != 'answer':
        passed = False
        log("ds attribute 42 was %s instead of 'answer'" % ds42)
    
    return passed
    

def test_2( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    ds.setAttribute( 42, "answer")

    passed = True
    ds42 = ds.attribute( 42)
    if ds42 != "answer":
        passed = False
        log("ds attr 42 was %s instead of 'answer'" % ds42)
        
    return passed 


def test_3( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    acAtts = ds.listAttributes()
    acAtts.sort()
    attList = [42, 'name', 'nifty', 'pi', 'plottable', 'unit']
    passed = True
    if acAtts != attList:
        passed = False
        log("ds attributes list was %s instead of %s" % (acAtts, attList))
    return passed


def test_4( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    if ds.name() != name:
        passed = False
        log("ds name was %s instead of 'test'" % ds.name())
    return passed


def test_5( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    dsShape = ds.shape()
    passed = True
    if dsShape != shape:
        passed = False
        log("ds.shape() was %s instead of %s" % ( dsShape, shape))

    return passed


def test_6( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    dsStorage = ds.storage()
    if dsStorage != storage:
        passed = False
        log("ds.storage was %s instead of %s" % (dsStorage, storage))

    return passed


def test_7( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    typecode = 6  # double
    
    from stdVector import vector
    storage = vector( typecode, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    dsTypecode = ds.typecode()
    if dsTypecode != typecode:
        passed = False
        log("ds.typecode was %s instead of %s" % (dsTypecode, typecode))

    return passed


def test_8( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    typecode = 6  # double
    
    from stdVector import vector
    storage = vector( typecode, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    dsTypecodeAsC = ds.typecodeAsC()
    if dsTypecodeAsC != 'double':
        passed = False
        log("ds.typecodeAsC was %s instead of 'double'" % dsTypecodeAsC)

    return passed


def test_9( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    typecode = 6  # double
    
    from stdVector import vector
    storage = vector( typecode, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    dsTypecodeAsNA = ds.typecodeAsNA()
    if dsTypecodeAsNA != 'Float64':
        passed = False
        log("ds.typecodeAsNA was %s instead of 'Float64'" % dsTypecodeAsNA)

    return passed


def test_10( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    typecode = 6  # double
    
    from stdVector import vector
    storage = vector( typecode, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    dsTypecodeAsStdVector = ds.typecodeAsStdVector()
    if dsTypecodeAsStdVector != 6:
        passed = False
        log( "ds.typecodeAsStdVector was %s instead of 6" %
             dsTypecodeAsStdVector)

    return passed


def test_11( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds = Dataset( name, unit, attributes, shape, storage)

    passed = True
    if ds.unit() != unit:
        passed = False
        log("ds unit was %s instead of 'many'" % ds.unit())
    return passed


def test_12( **kwds):
    
    from histogram.StdvectorDataset import Dataset
    name = 'test'
    unit = 'many'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 42:'answer'}
    shape = [2,3,4]
    dtype = 6  # double
    
    from stdVector import vector
    storage = vector( dtype, 24, 1.0)

    ds1 = Dataset( name, unit, attributes, shape, storage)
    ds2 = Dataset( 'test2', unit, attributes, shape, storage)

    print ds1.name(), ds2.name()
    
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

target = "StdvectorDataset"

log = utilities.picklog( target)

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id$"

# End of file

