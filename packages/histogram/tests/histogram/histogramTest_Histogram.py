#!/usr/bin/env python
# Copyright (c) 2004 Timothy M. Kelley all rights reserved

aspects = [
    "instantiate/initialize",
    "axisFromId()",
    "axisFromName()",
    "data()",
    "error()",
    ]



from ndarray.StdVectorNdArray import NdArray



def test_0( **kwds):

    from histogram.Axis import Axis
    from histogram.NdArrayDataset import Dataset
    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    lengths = [2,3,4]
    dtype = 6  # double

    stor1 = NdArray( dtype, lengths[0]+1, 1.0)
    ax1 = Axis( name+'ax1', unit, attributes, lengths[0],  stor1)
    
    stor2 = NdArray( dtype, lengths[1]+1, 1.0)
    ax2 = Axis( name+'ax2', unit, attributes, lengths[1],  stor2)

    stor3 = NdArray( dtype, lengths[2]+1, 1.0)
    ax3 = Axis( name+'ax3', unit, attributes, lengths[2],  stor3) 

    size = lengths[0]*lengths[1]*lengths[2]
    
    dataStore = NdArray( dtype, size, 1.0); dataStore.setShape( (2, 3,4) )
    data = Dataset( name+'data', unit, attributes, lengths, dataStore)

    errorStore = NdArray( dtype, size, 1.0); errorStore.setShape( (2, 3,4) )
    error = Dataset( name+'error', unit, attributes, lengths, errorStore)

    from histogram.Histogram import Histogram

    histogram = Histogram( 'testHist', data, error, [ax1, ax2, ax3],
                           attributes)

    return True

    
def test_1( **kwds):

    from histogram.Axis import Axis
    from histogram.NdArrayDataset import Dataset
    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    lengths = [2,3,4]
    dtype = 6  # double

    stor1 = NdArray( dtype, lengths[0]+1, 1.0)
    ax1 = Axis( name+'ax1', unit, attributes, lengths[0],  stor1)
    
    stor2 = NdArray( dtype, lengths[1]+1, 1.0)
    ax2 = Axis( name+'ax2', unit, attributes, lengths[1],  stor2)

    stor3 = NdArray( dtype, lengths[2]+1, 1.0)
    ax3 = Axis( name+'ax3', unit, attributes, lengths[2],  stor3) 

    size = lengths[0]*lengths[1]*lengths[2]
    
    dataStore = NdArray( dtype, size, 1.0); dataStore.setShape( (2, 3,4) )
    data = Dataset( name+'data', unit, attributes, lengths, dataStore)

    errorStore = NdArray( dtype, size, 1.0); errorStore.setShape( (2, 3,4) )
    error = Dataset( name+'error', unit, attributes, lengths, errorStore)

    from histogram.Histogram import Histogram

    hist = Histogram( 'testHist', data, error, [ax1, ax2, ax3],
                           attributes)

    passed = True
    hax1 = hist.axisFromId( 1)
    if hax1 is not ax1:
        passed = False
        log("hax1 was %s instead of %s" % (hax1, ax1))
    return passed

    
def test_2( **kwds):

    from histogram.Axis import Axis
    from histogram.NdArrayDataset import Dataset
    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    lengths = [2,3,4]
    dtype = 6  # double

    stor1 = NdArray( dtype, lengths[0]+1, 1.0)
    ax1 = Axis( name+'ax1', unit, attributes, lengths[0],  stor1)
    
    stor2 = NdArray( dtype, lengths[1]+1, 1.0)
    ax2 = Axis( name+'ax2', unit, attributes, lengths[1],  stor2)

    stor3 = NdArray( dtype, lengths[2]+1, 1.0)
    ax3 = Axis( name+'ax3', unit, attributes, lengths[2],  stor3) 

    size = lengths[0]*lengths[1]*lengths[2]
    
    dataStore = NdArray( dtype, size, 1.0); dataStore.setShape( (2, 3,4) )
    data = Dataset( name+'data', unit, attributes, lengths, dataStore)

    errorStore = NdArray( dtype, size, 1.0); errorStore.setShape( (2, 3,4) )
    error = Dataset( name+'error', unit, attributes, lengths, errorStore)

    from histogram.Histogram import Histogram

    hist = Histogram( 'testHist', data, error, [ax1, ax2, ax3],
                           attributes)

    passed = True
    hax1 = hist.axisFromName( 'testax1')
    if hax1 is not ax1:
        passed = False
        log("hax1 was %s instead of %s" % (hax1, ax1))
    return passed

    
def test_3( **kwds):

    from histogram.Axis import Axis
    from histogram.NdArrayDataset import Dataset
    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    lengths = [2,3,4]
    dtype = 6  # double

    stor1 = NdArray( dtype, lengths[0]+1, 1.0)
    ax1 = Axis( name+'ax1', unit, attributes, lengths[0],  stor1)
    
    stor2 = NdArray( dtype, lengths[1]+1, 1.0)
    ax2 = Axis( name+'ax2', unit, attributes, lengths[1],  stor2)

    stor3 = NdArray( dtype, lengths[2]+1, 1.0)
    ax3 = Axis( name+'ax3', unit, attributes, lengths[2],  stor3) 

    size = lengths[0]*lengths[1]*lengths[2]
    
    dataStore = NdArray( dtype, size, 1.0); dataStore.setShape( (2, 3,4) )
    data = Dataset( name+'data', unit, attributes, lengths, dataStore)

    errorStore = NdArray( dtype, size, 1.0); errorStore.setShape( (2, 3,4) )
    error = Dataset( name+'error', unit, attributes, lengths, errorStore)

    from histogram.Histogram import Histogram

    hist = Histogram( 'testHist', data, error, [ax1, ax2, ax3],
                           attributes)

    passed = True
    hdata = hist.data()
    if hdata is not data:
        passed = False
        log("hdata was %s instead of %s" % (hdata, data))
    return passed

    
def test_4( **kwds):

    from histogram.Axis import Axis
    from histogram.NdArrayDataset import Dataset
    name = 'test'
    unit = '1'
    attributes = {'plottable':True, 'nifty':False, 'pi':3.14159, 3.14159:'pi'}
    lengths = [2,3,4]
    dtype = 6  # double

    stor1 = NdArray( dtype, lengths[0]+1, 1.0)
    ax1 = Axis( name+'ax1', unit, attributes, lengths[0],  stor1)
    
    stor2 = NdArray( dtype, lengths[1]+1, 1.0)
    ax2 = Axis( name+'ax2', unit, attributes, lengths[1],  stor2)

    stor3 = NdArray( dtype, lengths[2]+1, 1.0)
    ax3 = Axis( name+'ax3', unit, attributes, lengths[2],  stor3) 

    size = lengths[0]*lengths[1]*lengths[2]
    
    dataStore = NdArray( dtype, size, 1.0); dataStore.setShape( (2, 3,4) )
    data = Dataset( name+'data', unit, attributes, lengths, dataStore)

    errorStore = NdArray( dtype, size, 1.0); errorStore.setShape( (2, 3,4) )
    error = Dataset( name+'error', unit, attributes, lengths, errorStore)

    from histogram.Histogram import Histogram

    hist = Histogram( 'testHist', data, error, [ax1, ax2, ax3],
                           attributes)

    passed = True
    herror = hist.errors()
    if herror is not error:
        passed = False
        log("herror was %s instead of %s" % (herror, error))
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



if __name__ == '__main__':
    import ARCSTest.utilities as utilities

    target = "Histogram"

    log = utilities.picklog( target)
    import journal
    info = journal.info( target)
    info.activate()
    
    run()

# version
__id__ = "$Id$"

# End of file

