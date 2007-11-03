#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
this module provides plotting facility to reduction packages.
Currently it only has one implementation based on Matplotlib that
can plot 2D image or contour, and one implementation for plot
1D curve.

Later this module should be reimplemented once the Graphics API
is fixed.
"""


class Plotter1D(object):

    def interactive( self, b ):
        """if b is True, control will go back to python prompt after plotting
        """
        raise NotImplementedError , "%s must override plot" % (
            self.__class__.__name__)
    

    def plot(self, x, y):
        """create plot of y vs x"""
        raise NotImplementedError , "%s must override plot" % (
            self.__class__.__name__)

    pass #end of Plotter1D



class MplPlotter:

    try:
        import pylab
        _engine = pylab
    except ImportError:
        _engine = None
        pass
    
    def __init__(self, mpl_figure = None):
        mpl_figure = None # a hack
        
        #self.interactive(True)
        self.interactive(False)
        self._figure = mpl_figure
        if self._figure: self._usePylab = False
        else: self._usePylab = True
        return


    def interactive(self, b):
        self._interactive = b
        import matplotlib
        matplotlib.interactive(b)
        return


    def clear(self):
        figure = self.get_figure()
        figure.clf()
        try: figure.gca()
        except: pass
        return
    

    def get_figure(self):
        if self._figure: return self._figure
        return self._engine


    def get_image(self):
        return self._image

    pass # end of MplPlotter



class MplPlotter1D(MplPlotter, Plotter1D):

    def __init__(self, mpl_figure = None):
        """MplPlotter1D( mpl_figure=None ) --> create a new 1D plotter
        implemented by using matplotlib
        
         - mpl_figure: matplotlib.figure.Figure instance
        """
        MplPlotter.__init__(self, mpl_figure)
        return
    
    
    def plot(self, x, y, **kwds):
        color = kwds.get('color') or ''
        symbol = kwds.get('symbol') or ''
        
        fmtstr = color+symbol
        
        if kwds.has_key( "yerr" ):
            self._image = self.errorbar( x, y, yerr = kwds["yerr"], fmt = fmtstr)
        else:
            self._image = self._plot(x,y, fmtstr)
            pass
        return


    def errorbar(self, x,y, yerr = None, **kwds):
        figure = self.get_figure()
        _clear( figure )

        if self._usePylab: plot = self._engine.errorbar
        else:
            if figure is None: print "missing matplotlib! "; return
            else: plot = figure.gca().errorbar
            pass
        rt = plot(x,y, yerr = yerr, **kwds)
        if self._usePylab and not self._interactive: self._engine.show()
        return rt


    def _plot(self, x,y, *args, **kwds):
        figure = self.get_figure()
        _clear( figure )

        if self._usePylab: plot = self._engine.plot
        else:
            if figure is None: print "missing matplotlib! "; return
            else: plot = figure.gca().plot
            pass
        rt = plot(x,y, *args, **kwds)
        if self._usePylab and not self._interactive: self._engine.show()
        return rt

    pass # end of MplPlotter1D



pylabPlotter1D = defaultPlotter1D = MplPlotter1D()



class Plotter2D(object):

    def interactive( self, b ):
        """if b is True, control will go back to python prompt after plotting
        """
        raise NotImplementedError , "%s must override plot" % (
            self.__class__.__name__)
    

    def plot(self, x, y, z, min = None, max = None):
        """create 2D intensity plot
        param x:  1D array of x values
        param y:  1D array of y values
        param z:  2D matrix of z values
        """
        raise NotImplementedError , "%s must override plot" % (
            self.__class__.__name__)


    def contourPlot(self, x, y, z, min = None, max = None, nsteps = 20):
        """create 2D contour plot
        param x:  1D array of x values
        param y:  1D array of y values
        param z:  2D matrix of z values
        """
        raise NotImplementedError , "%s must override contourPlot" % (
            self.__class__.__name__)

    pass



class MplPlotter2D(MplPlotter, Plotter2D):

    def __init__(self, mpl_figure = None):
        """MplPlotter2D(mpl_figure = None) -> create a 2d plotter
         - mpl_figure: matplotlib.figure.Figure instance
        """
        MplPlotter.__init__(self, mpl_figure)
        return


    def plot(self, x, y, z, min = None, max = None):
        '''plot z(x,y)

        Notes:
          * x, y are arrays of bin boundaries! This make more sense for
            histograms.
          * z is a 2D array. The convention is that the y index runs faster
            than the x index. This convention is just opposite to the
            matplotlib convention in function pcolor. So we need to
            do a transpose.
        '''
        figure = self.get_figure()
        _clear( figure )
        self._image = self.plot_(x,y,z, min = min, max = max)
        if self._usePylab and not self._interactive: self._engine.show()
        return

        
    def plot_(self,x, y, z, min = None, max = None): 
        figure = self.get_figure()
        if figure is None: print "missing matplotlib! "; return

        #convert everything to numpy array, otherwise matplotlib
        #may complain
        from numpy import array
        z = array(z); x = array(x); y = array(y)
        #

        if len(x) <= 1 or len(y) <= 1: raise ValueError, "The data you want to plot is really 1-D. Please make a create a 1D histogram by slicing and make a 1D plot"
        
        _min, _max = _guessMinMax( z )
        if min is None: min = _min
        if max is None: max = _max

        zcopy = _restrictedZ( z, min, max)

        #please read notes in docstring of method "plot"
        zcopy = zcopy.transpose()

        print "plot z in (%s, %s)" % (min, max)
        X,Y = self._engine.meshgrid(x,y)
        if self._usePylab: rt = self._engine.pcolor( X,Y, zcopy, shading="flat")
        else: rt = figure.gca().pcolor( X,Y, zcopy, shading="flat")
        return rt


    def contourPlot( self, x, y, z, min = None, max = None, nsteps = 20):
        '''contour plot of z(x,y)

        Notes:
          * x, y are arrays of bin centers! This is totally differnt
            from method 'plot'
          * z is a 2D array. The convention is that the y index runs faster
            than the x index. This convention is just opposite to the
            matplotlib convention in function pcolor. So we need to
            do a transpose.
        '''
        figure = self.get_figure()
        _clear( figure )
        self.contourPlot_(x, y, z, min = min, max = max, nsteps = 20)
        if self._usePylab and not self._interactive: self._engine.show()
        return
    

    def contourPlot_( self, x, y, z, min = None, max = None, nsteps = 20):
        figure = self.get_figure()
        if figure is None: print "missing matplotlib! "; return
        from numpy import array
        z = array(z)
        z = z.transpose()
        _min, _max = _guessMinMax( z )
        if min is None: min = _min
        if max is None: max = _max

        #color steps
        import numpy as N
        c = N.arange( min, max, (max-min)/nsteps)

        print "plot z in (%s, %s)" % (min, max)
        _clear( figure )
        if self._usePylab:  self._engine.contourf( x,y,z,c )
        else:   figure.gca().contourf( x,y,z,c )
        #self._engine.show()
        return



# detailed implementations
def _restrictedZ( z, min, max):
    """go through all data and restrict z to be within min,max"""
    lx, ly = z.shape
    import numpy as N
    copy = N.array( z, copy=1) 
    for i in range(lx):
        for j in range(ly):
            v = z[i,j]
            if v>max: copy[i,j] = max
            if v<min: copy[i,j] = min
            continue
        continue
    return copy


def _guessMinMax(z):
    """to create a nice plot, one has to choose the right region for z.
    otherwise, many details would be missed. This function provides
    a guess for the plotting region.
    """
    z = z.copy()
    return _min(z), _guessMax(z)


def _guessMax(z):
    """make a guess of the max z value that should be used in plot.
    This max value should usually be samller than the real max value of z matrix
    because otherwise many details could be missing from the plot
    """
    #calculate average of z
    ave = _average( z )
    #set maximum of z. 3.0 is a reasonable? number
    max = ave * 3.0
    return max


def _average( z ):
    """return average of z"""
    import numpy as N
    ave = N.average( N.average( z ) )
    return ave


def volume(shape):
    from operator import mul
    return reduce(mul, shape)


def _min(z):
    """ return minimum of z """
    save = z.shape
    try:
        z.shape = volume( save ),
    except Exception, err:
        msg = "%s. z is a %s, z.shape = %s" % (err, type(z), z.shape)
        raise err.__class__, msg
    res = min(z)
    z.shape = save
    return res


def _clear(figure):
    return
    figure.clf()
    try: figure.gca()
    except: pass
    return


pylabPlotter2D = defaultPlotter2D = MplPlotter2D()




#the following code is not necessary anymore.
#Patrick pointed out the following numpy trick:
# import pylab, numpy
# x = numpy.random.rand(100)*10
# y = numpy.sin(x)
# o = x.argsort()
# pylab.plot(x[o],y[o])
# pylab.show()



## def sortxy_x_numpy( x, y ):
##     '''sort x, y according to x

##     when we want to plot y(x) curve, we want array x and y to be
##     sorted. An unsorted array will cause plotter to
##     plot draw lines back-and-forth, if the plotting is in any
##     kind of "line" mode.

##     This function sort the input x array and y array, and make
##     sure x array is incremental (y array is adjusted to make
##     sure any (xi,yi) pair-relationship is maintained.

##     sortxy_x( [2,3,1], [4,5,6] ) ---> [1,2,3], [6,4,5]
##     '''
##     import numpy as n
##     try: yx = n.array( (x, y) )
##     except: yx = n.array( (x,y), object )
##     import operator
##     yx_sorted = n.array( sorted(
##         yx.transpose(), key=operator.itemgetter(0) ) ).transpose()
##     return yx_sorted
    
## sortxy_x = sortxy_x_numpy

## def sortxy_x_slow( x, y ):
##     '''sort x, y according to x

##     same as sortxy_x_numpy. but do not use numpy.
##     it is slower but more general.
##     '''
##     yx =x, y
##     yxt = _transpose( yx )
##     import operator
##     yx_sorted =  _transpose( sorted(
##         yxt, key=operator.itemgetter(0) ) )
##     return yx_sorted



## def _transpose_numpy(m):
##     import numpy as n
##     try:
##         m1 = n.array( m )
##     except:
##         m1 = n.array( m, object )
##         pass
##     return m1.transpose()


## _transpose = _transpose_numpy


## def _transpose_slow( m ):
##     "transpose a 2D matrix"
##     try: m[0]
##     except:
##         raise ValueError , "%s is not even a list" % (m, )
##     try: m[0][0]
##     except:
##         raise ValueError , "%s is not a matrix" % (m, )
##     ncols = len(m[0])
##     for row in m:
##         assert len(row) == ncols, "%s is not a matrix" % (m,)
                
##     ret = [ [] for i in  m[0] ]

##     for i, row in enumerate(ret):
##         for a in m: row.append( a[i] )
##         continue

##     return ret
    


## def sortxys_x( x, ys ):
##     '''similar to sortxy_x, but instead of a y array, here
##     we have a list of y arrays
    
##     sortxys_x( [2,3,1], [ [4,5,6], [7,8,9] ] )
##        ---> [1,2,3], [[6,4,5], [9,7,8] ]
##     '''
##     Y1 = _transpose(ys)
##     sx, sY = sortxy_x( x, Y1 )
##     return sx, _transpose_slow(sY)



# version
__id__ = "$Id: Plot2dHist.py,v 1.4 2005/11/07 23:03:44 linjiao Exp $"

# End of file 
