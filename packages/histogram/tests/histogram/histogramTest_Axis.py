#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "instantiate/intialize",
    "binCenters()",
    "binBoundaries()",
    "binBoundariesAsList()",
    ]



from histogram import ndArray



def test_0( **kwds):

    from histogram.Axis import Axis

    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    length = 23
    dtype = 6  # double

    storage = ndArray( dtype, length+1, 1.0)

    axis = Axis( name, unit, attributes, length,  storage)

    passed = True
    if axis._shape != [length + 1]:
        passed = False
        log("shape was %s instead of %s" % (axis._shape, [length+1]))
    # everything else tested in histogramTest_StdvectorDataset.py
    
    return passed 


def test_1( **kwds):

    from histogram.Axis import Axis

    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    length = 23
    dtype = 6  # double

    binBounds = [i+1.0 for i in range( length+1)]
    storage = ndArray( dtype, binBounds)


    axis = Axis( name, unit, attributes, length,  storage)

    expected = [i+1.5 for i in range(23)]
    passed = utilities.compareFPLists( expected, axis.binCenters(), 1e-15, log)
    if not passed:
        log( "binCenters(): expected %s, got %s" %
             (expected, axis.binCenters()))

    return passed


def test_2( **kwds):

    from histogram.Axis import Axis

    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    length = 23
    dtype = 6  # double

    binBounds = [i+1.0 for i in range( length+1)]
    storage = ndArray( dtype, binBounds)

    axis = Axis( name, unit, attributes, length,  storage)

    passed = storage == axis.binBoundaries()
    if not passed:
        log( "binBoundaries(): expected %s, got %s" %
             ( storage, axis.binBoundaries()))

    return passed


def test_3( **kwds):

    from histogram.Axis import Axis

    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    length = 23
    dtype = 6  # double

    binBounds = [i+1.0 for i in range( length+1)]
    storage = ndArray( dtype, binBounds)

    axis = Axis( name, unit, attributes, length,  storage)

    passed = storage.asList() == axis.binBoundariesAsList()
    if not passed:
        log( "binBoundariesAsList(): expected %s, got %s" %
             ( storage.asList(), axis.binBoundariesAsList()))

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


#import ARCSTest.utilities as utilities
import utilities

target = "Axis"

log = utilities.picklog( target)

if __name__ == '__main__':
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id$"

# End of file

