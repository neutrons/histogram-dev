#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                  Jiao  Lin
#                        California Institute of Technology
#                        (C) 2005-2010  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \mainpage histogram
##
## \section reference_sec Public Interface
## Factory methods:
##   - %histogram: histogram::__init__::histogram
##   - %axis: histogram::__init__::axis
##
## Data objects:
##   - %Histogram: histogram::Histogram::Histogram
##   - %Axis: histogram::Axis::Axis
##
## I/O methods:
##   - %histogram.hdf.dump: histogram::hdf::__init__::dump
##   - %histogram.hdf.load: histogram::hdf::__init__::load
## 
## \section intro_sec Introduction
## histogram package provides a fundamental data structure for data reduction
## and data analysis.
##
## Here, let us explain our definition of 
## "histogram". The result of a scientific measurement is usually a histogram(s),
## by which we mean
## we have data in some bins. For example, if we measure a spectrum as a function of
## time-of-flight, we will get an array of counts, while each element in that array represents
## the number of counts measured in a predefined time slot (bin).
## This array of counts can be approximated by
##
##   \f$ \frac{dI}{dx}(x) \Delta x \f$
##
## where \f$\frac{dI}{dx}\f$ is a density function and \f$ \Delta x \f$ is bin size.
##
## From this little discussion, we see that there are two pieces of critical information
## in a histogram: the data, and the axis (or axes), which is about bin sizes. Some time we
## need to know the context that the histogram is in, and that brings us meta-data.
## Following is a bit of definitions:
##
## A histogram consists of axes, datasets, and metadata related to the histogram.
##
## - dataset: a dense array of numbers which may have many dimensions.
## - axis: a one dimensional dataset whose elements are the bin boundaries of one dimension of a histogram.
## - histogram: it contains
##   - (1) a dataset whose elements represent the number of counts in some range of axis
##         or axes values;
##   - (2) a set of associations concerning a histogram in the sense of (1) and
##         potentially everything that can be known about it: error bars, axes, history.
## - metadata: data which provides context for other data: data about data.
##
## \section Design
## The design of this package is not too complex. Basically we need a way to save
## data, and we have an abstract inteface 
## <a href="../../../ndarray/ndarray/html/">ndarray</a> to handle that.
## We also need a way to keep meta-data, and this is done in AttributeContBase.
##
##
## Here is the class diagram of histogram package:
##
## \image html "../../uml/histogram-class-diagram.png"
##

## \package "histogram.__init__"
## Main funtions:
##  - histogram
##  - axis


#factories
def pqvalue( *args ):
    """create an instance that represents a value of a physical quantity,
    probably with an error bar"""
    if len(args) == 1: args = args[0]
    from ValueWithError import toVE
    return toVE( args )


def axis( name, centers = None, unit = None, boundaries = None, attributes=None):
    """axis( name, centers=None, unit = None, boundaries=None): create an axis
    
    name: The name of the axis.
    centers: The bin centers of the axis.
    unit: The unit of the axis.
    boundaries: The bin boundaries of the axis

    If both centers and boundaries are specified, boundaries are ignored.

    Examples:
      axis('tof', boundaries=arange(2000,6000,10), unit='microsecond')
      axis('energy', centers=arange(-50,50,1.), unit='meV')
      axis('detectorID', range(0,1000))
    """
    
    if centers is not None and len(centers) < 1: raise ValueError , "Invalid axis %s" % (centers, )
    if 'ID' in name and centers is not None and _isIntegers(centers) and unit is None:
        return IDaxis( name, centers, attributes=attributes )
    if centers is None: return paxis( name, unit, boundaries = boundaries, attributes=attributes )
    return paxis( name, unit, centers = centers, attributes=attributes )

def use( factory ):
    def useNumpy():
        from ndarray.NumpyNdArray import NdArray
        return NdArray
    table = {
        'default': useNumpy,
        'numpy': useNumpy,
        }
    global _array_factory
    _array_factory = table[ factory ]()
    return
_array_factory = None
use( 'default' )

        
def ndArray( *args, **kwds):
    factory = kwds.get('factory')
    if factory is None:
        global _array_factory
        factory = _array_factory
    else:
        del kwds['factory']
    return factory( *args, **kwds )



def histogram( name, axes, data = None, errors = None, unit="1",
               data_type = "double", fromfunction = None):
    
    """create a histogram out of given inputs

    This is the most important method of the histogram package.
    To use this method, first import it from the histogram package:

      >>> from histogram import histogram

    You may want to import other convenient factory methods too

      >>> from histogram import axis, arange

    The following are explanations of the arguments of this method,
    which is followed by some examples.
    
    axes: a list of axis, each axis could be specified by one of the following
      - a tuple of (name, bin_centers, (optionally)unit)
      - an Axis instance

    data and errors:  multiple dimensional arrays of data and errorbar squares
      - data: m-D arraya of data
      - errors: m-D array of squares of error bars

    fromfunction: create data and errors from user-defined function(s). This
      keyword overrides keywords 'data' and 'errors'.

    If neither the 'data/errors' keywords nor the 'fromfunction' keyword is
    specified, data and error bars are initialized to zeros.

    data_type: type of data array. acceptable types:
      - 'double'
      - 'float'
      - 'int'

    unit: the unit of the data

    Examples:

    Directly create a histogram without pre-creation of axes:
      sqe = histogram( 'SQE',
        [ ('Q', arange(0., 13., 0.1), 'angstrom**-1'),
          ('E', arange(-50,50., 1.), 'meV'), ],
        data = [ ... data matrix (130X100) ... ],
        errors = [ ... square of error bar matrix (130X100) ... ],
        )

    Create axes first, and then create the histogram:
      Qaxis = axis('Q', centers=arange(0, 13., 0.1), unit='angstrom**-1')
      Eaxis = axis('E', centers=arange(-50, 50., 1), unit='meV')
      sqe = histogram( 'SQE',
        (Qaxis, Eaxis),
        data = [ ... data matrix (130X100) ... ],
        errors = [ ... square of error bar matrix (130X100) ... ],
        )

    Create histogram using keyword 'fromfunction':
      1D:
        xaxis = axis('x', arange(10))
        hx = histogram('hx', [xaxis], fromfunction=numpy.sin)
        
      2D:
        xaxis = axis('x', arange(10))
        yaxis = axis('y', arange(10))
        hxy = histogram('hxy', [xaxis, yaxis],
            fromfunction=lambda x,y: numpy.sin(x*y))

      3D:
        xaxis = axis('x', arange(10))
        yaxis = axis('y', arange(10))
        zaxis = axis('z', arange(10))
        hxyz = histogram('hxyz', [xaxis, yaxis, zaxis],
            fromfunction=lambda x,y,z: x**2+numpy.sin(y)+z**3*x*y)

      Specify 2 functions. One for data, another for error bar squares.
        xaxis = axis('x', arange(10))
        hx = histogram('hx', [xaxis],
            fromfunction=(numpy.sin, lambda x:numpy.abs(numpy.sin(x))))
    """
    h = makeHistogram( name, axes, data, errors, unit = unit,
                       data_type = data_type )
    
    if fromfunction is None: return h
    
    axes = h.axes()
    slices = tuple( [ () for axis in axes ] )
    if len(slices) == 1: slices = slices[0] # dim=1 is a special case
    if isinstance(fromfunction, tuple) or isinstance(fromfunction, list):
        assert len(fromfunction) == 2, \
               "histogram( name, axes, fromfunction = (data, errorbars) )"
        for f in fromfunction: assert callable(f), "%s is not callable." %f
        datasets = [datasetFromFunction( f, axes )
                    for f in fromfunction ]
        pass
    
    else:
        f = fromfunction
        assert callable(f), "%s is not callable" % f
        datasets = datasetFromFunction( f, axes ), None
        pass
    
    h[ slices ] = datasets
    return h


def plot( h, min = None, max = None, output='window', interactive=False):
    """plot a histogram

    h: histogram
    min, max: min and max I value
    output:
      - window: plot to a window
      - <filename>: plot to the given filename
    """
    
    if output != 'window':
        import matplotlib
        matplotlib.use('PS')
        
    from plotter import defaultPlotter
    defaultPlotter.interactive(interactive)
    defaultPlotter.plot( h, min = min, max = max)

    if output != 'window':
        import pylab
        import os
        eps = os.path.splitext(output)[0] + '.eps'
        pylab.savefig(eps)

        if eps != output:
            #!!! should check if "convert" exists
            cmd = 'convert %s %s' % (eps, output)
            if os.system(cmd):
                raise RuntimeError
    return





#methods
def getSliceCopyFromHistogram( name, axes, hist ):
    """retrieve a slice (copy) of a histogram

    xaxis = axis('x', [0.1, 0.5,0.6])
    yaxis = axis('y', [3.,4.,5.,100])
    getSliceCopyFromHistogram( Ixyz, [xaxis, yaxis] )
    """
    #get axes that are not touched
    axisnames = [ axis.name() for axis in axes ]
    allaxes = hist.axes()
    remainedaxes = []
    for axis in allaxes:
        if axis.name() in axisnames: continue
        remainedaxes.append( axis )
        continue

    #histogram to return
    ret = histogram( name, axes+remainedaxes, unit = hist.unit() )

    #
    def _( *args ):
        d = {}
        for i, axis in enumerate(axes):
            d[axis.name()] = args[i]
            continue
        ret[ d ] = hist[ d ]
        return
    
    axisBinCenters = [ axis.binCenters() for axis in axes ]

    from _loop import loop
    loop( axisBinCenters, _ )
    
    return ret




#less convenient factories
def datasetFromFunction( func, axes, *args, **kwds):
    shape = [ axis.size() for axis in axes ]

    xs = [ axis.binCenters() for axis in axes ]

    try: return applyFunction_fast( func, xs, *args, **kwds )
    except:
        import traceback
        debug.log(traceback.format_exc())
        return applyFunction_slow( func, xs, *args, **kwds )
    raise "should not reach here"


def applyFunction_fast( func, xs, *args, **kwds ):
    """compute the array [ func(x) ] for each x constructed from xs.

    Example:
      applyFunction_fast( lambda x,y,z: x+y+z, [ arange(0,1,0.1), arange(-2,2,0.5), arange(0,10,1.) ] ) -->   a grid of values of x+y+z for all points (x,y,z) while x in [0,0.1,...,0.9], y in [-2, -1.5, ...,1.5] and z in [0,1.,2.,...,9.]

    xs is a list. Each item, xs[i]. in the list represent one axis and it
    is a list of values on that axis.

    The basic idea is to calculate the function value for each
    grid point. A grid point is
    
      x = [ xs[0][i0], xs[1][i1], xs[2][i2], ... ]
    
    This implementation assumes all operations in 'func' can be applied
    to numpy arrays. Those operations include numpy.sin, numpy.cos,
    operator +-*/, etc.
    
    *args and **kwds are additional parameters for 'func'
    """
    mg = meshgrid( *xs ) 
    targs = mg + list(args)
    debug.log('%s' % (targs,))
    return func( *targs, **kwds )


def applyFunction_slow( func, xs, *args, **kwds):
    """compute the array [ func(x) ] for each x constructed from xs.

    Read applyFunction_fast for more docs.
    
    This implementation assumes all operations in 'func' can be applied
    to numpy arrays. Those operations include numpy.sin, numpy.cos,
    operator +-*/, etc.
    
    *args and **kwds are additional parameters for 'func'
    """
    from numpy import zeros, array
    
    dim = len(xs) # dimension of x space

    #get a list of grid points
    mg = meshgrid( *xs )
    #flatten it so that we can easily transpose
    mg = [item.flatten() for item in mg]
    mg = array(mg)
    #
    Xs = mg.transpose()
    Xs.shape = -1, dim

    # create result array
    ret = zeros( Xs.shape[0] )
    for i,X in enumerate(Xs):
        targs = tuple(X) + args
        ret[i] = func( *targs, **kwds )

    # adjust shape
    ret.shape = [len(x) for x in xs]
    return ret


def histogramContainer( input ):
    """make sure to return a histogram container object

    if input is a histogram, use SimpleHistCollection to
    make it a histogram container object

    otherwise, make sure input is a histogram container object
    and return it.
    """
    from Histogram import Histogram
    if isinstance( input, Histogram ):
        return makeHistogramCollection( input )
    from DetHistCollection import DetHistCollection
    assert isinstance( input, DetHistCollection ), \
           "%s is not a histogram collection" % (input, )
    return input


# interface more for developers

def paxis( *args, **kwds ):
    """create an axis for a physical quantity

    paxis( name, unit, centers = [], boundaries = [] )

      - name: name of the physical quantity
      - unit: unit of the physical quantity
      - centers: centers of bins on the axis
      - boundaries: boundaries of bins on the axis
    """
    return createContinuousAxis( *args, **kwds )


def IDaxis(name, ids, attributes=None):
    """create an 'ID' axis such as detector IDs and pixel IDs

    IDaxis( name, ids )

      name: name of the axis
      ids:  a list of ids
      datatype: should be integer
    """
    return createDiscreteAxis( name, ids, "int", attributes=attributes )




def calcBinBoundaries( min, delta, nBins ):
    """calculate bin boundaries given minumum, step, and number of bins for bin centers

    bin centers should be [min, min+delta, ..., min+delta*(nBins-1)]
    bin boundaries will be [ min-delta/2, min+delta/2, ..., min+delta*(nBins-1/2) ]
    """
    return [min - delta/2.0 + i*delta for i in range(nBins+1)]


def createContinuousAxis( name, unit, centers = None, boundaries = None,
                          centersCreationArgs = None, attributes=None ):
    """create a continuous axis

    a continuos axis represents a continuous physics quantity like energy, time of flight, etc.
    
    datatype is set to 'double' because of the continuity
    
    a mapper is created and attached to the axis.
    """
    if (centers is not None or centersCreationArgs is not None) and boundaries is not None:
        raise ValueError , "both centers and boundaries are specified"
    
    if centers is not None and centersCreationArgs is not None:
        raise ValueError , "both centers and center creation arguments are specified"
    
    if centers is not None:
        boundaries = boundariesFromCenters( centers )
        pass # end if centers
    
    if centersCreationArgs is not None:
        min, delta, nBins = centersCreationArgs
        boundaries = calcBinBoundaries( min, delta, nBins )
        pass # end if centersCreationArgs

    unit = unitFromString( unit )

    from histogram.EvenlyContinuousAxisMapper import \
         EvenlyContinuousAxisMapper as AxisMapper, NotEvenlySpaced
    try:
        axisMapper = AxisMapper( binBoundaries = boundaries )
    except NotEvenlySpaced:
        import traceback
        import journal
        debug = journal.debug('histogram.createContinuousAxis')
        #debug.log( traceback.format_exc() )
        debug.log( 'createContinuousAxis(name = %r, unit = %r, centers= %r, boundaries = %r' % (
            name, unit, centers, boundaries ) )
        from histogram.ContinuousAxisMapper import ContinuousAxisMapper as AxisMapper
        axisMapper = AxisMapper( boundaries )

    nBins = len( boundaries ) - 1
    
    storage = ndArray( "double", boundaries )
    
    from Axis import Axis
    return Axis( name, unit, length = nBins, storage=storage,
                 mapper = axisMapper, centers = centers,
                 attributes = attributes)


def boundariesFromCenters( centers ):
    '''boundariesFromCenters( centers ) --> boundaries

    given bin centers, return bin boundaries
    '''
    if len(centers) < 2:
        raise ValueError , "Cannot create boundaries from centers %s" %(centers, )

    msg =  "centers array must be ascending or descending: %s" % (centers, )
    step = centers[1]-centers[0]
    for i in range(1,len(centers)-1):
        assert step*(centers[i+1]-centers[i])>=0, msg
        continue
    try: return _boundariesFromEvenlySpacedCenters( centers )
    except ArrayNotEvenlySpaced: return _boundariesFromCenters( centers )
    raise RuntimeError, "should not reach here"


def _boundariesFromCenters( centers ):
    '''_boundariesFromCenters( centers ) --> boundaries

    given centers that are not evenly spaced, try to
    make a reasonable guess of bin boundaries.
    
    This is not a good way of doing things because we
    have to make guesses.
    '''
    import numpy
    c = numpy.array(centers)
    c1 = c[1:]
    c2 = c[:-1]
    ret = numpy.zeros( len(centers) + 1, 'd' )
    ret[1:-1] = (c1+c2)/2.
    ret[0] = c[0] - (c[1]-c[0])/2.
    ret[-1] = c[-1] + (c[-1]-c[-2])/2.
    return list(ret)
    

class ArrayNotEvenlySpaced( Exception ): pass
class BinsOverlapped( Exception ): pass


def _boundariesFromEvenlySpacedCenters( centers ):
    d = centers[1] - centers[0]
    if d == 0 or d == 0.0 :
        raise BinsOverlapped , "Cannot create boundaries from centers %s" %(centers, )

    evenlyspaced = True
    for i in range(1, len(centers)-1):
        d1 = centers[i+1] - centers[i]
        if abs( (d1-d)/d  ) > eps:
            raise ArrayNotEvenlySpaced
        continue

    min = centers[0]
    delta = d
    n = len( centers )
    return calcBinBoundaries( min, delta, n )


def createDiscreteAxis( name, items, datatype, attributes=None):
    """create an axis of discrete numbers.

    a mapper is created and attached to the axis

    useful to represent quantities like IDs.
    """
    from histogram.DiscreteAxisMapper import DiscreteAxisMapper as AxisMapper
    itemDict = {}
    for i, value in enumerate(items): itemDict[value] = i
    axisMapper = AxisMapper( itemDict )

    storage = ndArray( datatype, list(items) + [-1] ) # -1 is a patch
    from histogram.Axis import Axis
    axis = Axis( name = name, length = len(items),
                 storage = storage, mapper = axisMapper,
                 attributes=attributes)
    return axis


def volume(shape):
    from operator import mul
    return reduce(mul, shape)


def createDataset( name, unit='1', shape=[], data = None, data_type = "double",
                   storage = None, array_factory = None,
                   ):
    """create a dataset

    if storage and data are left empty (None), a new storage will be created according to
    given data type and shape.

    if either data or storage is not empty, it will be used.
    """
    if storage is None and data is None:
        storage = ndArray( data_type, volume(shape), factory = array_factory )
        storage.setShape( shape )
        pass
    if data is not None and storage is not None:
        raise ValueError , "confused... both data and storage are specified"
    
    if data is not None:
        import numpy
        array = numpy.array( data, data_type )
        if shape: array.shape = shape
        from ndarray.NumpyNdArray import arrayFromNumpyArray as ndarrayFromNumpyArray
        storage = ndarrayFromNumpyArray( array )
        
    from NdArrayDataset import Dataset
    return Dataset(name, unit, shape = shape, storage = storage )


def makeHistogram( name, axes, data, errs, unit="1", data_type = 'double'):
    """create a histogram out of given data
    axes are a list of (axis_name, axis_bins)
    if axis_bins are integers or strings, it is supposed to be a discreted axis
    if axis bins are floats, it is supposed to be a continuous axis
    """
    # convert axis input parameters to axis instances
    _axes = []
    from Axis import Axis
    for axis_params in axes:
        if isinstance( axis_params, Axis ): _axis = axis_params
        else: _axis = axis( *axis_params )
        _axes.append(_axis)
        continue

    # unit
    unit = unitFromString( unit )

    # data
    shape = [ _axis.size() for _axis in _axes ]
    if data is None: data=createDataset(
        'data', unit, shape = shape,
        data_type = data_type )
    from DatasetBase import DatasetBase
    if isinstance( data, DatasetBase ): dataDS = data
    else: dataDS = createDataset( "data", unit, data = data, data_type = data_type )

    if errs is None: errs=createDataset(
        'errors', unit*unit, shape = shape,
        data_type = dataDS.typecode() )
    if isinstance( errs, DatasetBase ): errsDS = errs
    else: errsDS = createDataset( "errors", unit**2, data = errs, data_type = data_type )
    
    from Histogram import Histogram
    h = Histogram( name = name, unit = unit,
                   data = dataDS, errors = errsDS, axes = _axes )
    h._setShape( tuple([ len(_axis.binCenters()) for _axis in h.axes() ]) )
    return h


def makeHistogramCollection( args, factory = None ):
    from Histogram import Histogram
    if factory is None:
        assert isinstance( args, Histogram ), "%s is not a histogram" % (args,)
        from SimpleHistCollection import SimpleHistCollection
        factory = SimpleHistCollection
        args = args,
        pass
    return factory( *args )


eps = 1e-7

from numpy import arange

def unitFromString( s ):
    if s is None: return 1
    if isinstance( s, unitFromString.unittype ): return s
    if isinstance( s, basestring ): return unitFromString.parser.parse( s )
    try: return unitFromString.parser.parse( str(s) )
    except:
        raise NotImplementedError , "Don't know how to convert %r to unit" % s
    raise "Should not reach here"
from pyre.units import parser
unitFromString.parser = parser()
del parser
from pyre.units.unit import unit
unitFromString.unittype = unit
del unit


def _isIntegers( l ):
    from types import IntType
    for i in l:
        if not isinstance( i, IntType ) : return False
        continue
    return True



def meshgrid( *xs ):
    """
    meshgrid( [1,2], [3,4] ) -->
    
       [ [1,1],
         [2,2] ],
       [ [3,4],
         [3,4] ]

         
    meshgrid( [1,2], [3,4], [5,6,7] ) -->
    
       [[[1,1,1],
         [1,1,1]],
        [[1,1,1],
         [1,1,1]]],
       
       [[[3,3,3],
         [4,4,4]],
        [[3,3,3],
         [4,4,4]]],
       
       [[[5,6,7],
         [5,6,7]],
        [[5,6,7],
         [5,6,7]]],
       
    """
    shape = [ len(x) for x in xs ]
    dim = len(shape)
    if dim == 1:
        x, = xs
        import numpy
        x = numpy.array(x)
        return [x]
    return [ _grid( arr, i, shape ) for i, arr in enumerate( xs ) ]


def _grid( arr, i, shape ):
    """
    _grid( [1,2], 0, (2,2) ) --> [ [1,1], [2,2,] ]
    _grid( [1,2], 1, (2,2) ) --> [ [1,2], [1,2,] ]
    """
    arrsize = len(arr)
    assert shape[i] == arrsize, "axis %s does not have the right size: %s" %(
        arr, shape[i] )
    
    from operator  import mul
    size = reduce( mul, shape )

    from numpy import array
    rep = size/arrsize
    rt = array( [ arr for j in range(rep) ] )
    
    pshape = list(shape); del pshape[i]
    rt.shape = pshape + [arrsize] 

    axes = range( len(shape) )
    axes[ -1 ] = i; axes[i] = -1
    
    rt = rt.transpose( axes )
    rt = rt.flatten()
    rt.shape = shape
    return rt



import journal
debug = journal.debug( 'histogram' )


# version
__id__ = "$Id$"

#  End of file 
