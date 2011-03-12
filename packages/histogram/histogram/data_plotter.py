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


import numpy as N



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
        from pylab_extensions import pylab
        _engine = pylab
    except ImportError:
        import traceback
        traceback.print_exc()
        _engine = None
        pass

    #_image is the current image kept for pylab
    _image = None
    
    def __init__(self, mpl_figure = None):
        #passing mpl figure to this does not seem to work very well
        #directly use pylab seems to be the best solution.
        mpl_figure = None 
        
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
            MplPlotter._image = self.errorbar( x, y, yerr = kwds["yerr"], fmt = fmtstr)
        else:
            MplPlotter._image = self._plot(x,y, fmtstr)
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


    def plot(self, x, y, z, min = None, max = None, **kwds):
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
        MplPlotter._image = self.plot_(x,y,z, min = min, max = max, **kwds)
        if self._usePylab and not self._interactive: self._engine.show()
        return

        
    def plot_(self,x, y, z, min = None, max = None, **kwds): 
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

        #zcopy = _restrictedZ( z, min, max)

        #please read notes in docstring of method "plot"
        zt = z.transpose()

        print "plot z in (%s, %s)" % (min, max)
        X,Y = self._engine.meshgrid(x,y)

        if self._usePylab: engine = self._engine
        else: engine = figure.gca()

        #rt = MplPlotter._image = engine.pcolormesh( X,Y, zt, shading="flat")
        # need to reverse order on y direction
        zt1 = zt[::-1, :]
        #
        extent = x[0],x[-1], y[0],y[-1]
        # targetaspect = 3./4
        # adjustedaspect = targetaspect * (x[-1]-x[0]) / (y[-1]-y[0])
        # rt = MplPlotter._image = engine.imshow(zt1, extent=extent, aspect=adjustedaspect, **kwds)
        if not kwds.has_key('aspect'): kwds['aspect'] = 'auto'
        if not kwds.has_key('extent'): kwds['extent'] = extent
        rt = MplPlotter._image = engine.imshow(zt1, **kwds)
        engine.clim( min, max )
        engine.colorbar()
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
    return N.clip( z, min, max )


def _guessMinMax(z):
    """to create a nice plot, one has to choose the right region for z.
    otherwise, many details would be missed. This function provides
    a guess for the plotting region.
    """
    # copy to make sure we can change the shape
    # this will cause problem if the data is huge.
    z = z.copy()
    return _guessMin(z), _guessMax(z)


_scaler = 10
def _guessMax(z):
    """make a guess of the max z value that should be used in plot.
    This max value should usually be smaller than the real max value of z matrix
    because otherwise many details could be missing from the plot
    """
    save = z.shape
    z.shape = -1,
    max = N.max(z)
    if max <= 0:
        ret = max
    else:
        positive_median = N.median( z[ z>0 ] )
        ret = min( positive_median*_scaler, max )
    z.shape = save
    return ret


def _guessMin(z):
    """ return minimum of z """
    save = z.shape
    try:
        z.shape = -1,
    except Exception, err:
        msg = "%s. z is a %s, z.shape = %s" % (err, type(z), z.shape)
        raise err.__class__, msg
    min = N.min(z)
    if min >= 0: 
        ret = min
    else:
        negative_median = N.median( z[ z<0 ] )
        ret = max( negative_median*_scaler, min )
    z.shape = save
    return ret


def _clear(figure):
    figure.clf()
    try: figure.gca()
    except: pass
    return


pylabPlotter2D = defaultPlotter2D = MplPlotter2D()



def test_guessMin( ):
    assert( _guessMin( N.arange(100) ) == 0 )
    assert( _guessMin( N.arange(-10, 10) ) == -10 )
    a = N.arange( -10, 10 )
    a[0] = -1000000
    assert( _guessMin( N.arange(-10, 10) ) > -100 )
    assert( _guessMin( N.arange(-10, 10) ) <= -10 )
    a[-1] = 10000000
    assert( _guessMin( N.arange(-10, 10) ) > -100 )
    assert( _guessMin( N.arange(-10, 10) ) <= -10 )
    return


def test_guessMax( ):
    assert( _guessMax( N.arange(100) ) == 100 )
    assert( _guessMax( -N.arange(100) ) == 0 )
    assert( _guessMax( N.arange(-10, 10) ) == 10 )
    a = N.arange( -10, 10 )
    a[-1] = 1000000
    assert( _guessMax( N.arange(-10, 10) ) < 100 )
    assert( _guessMax( N.arange(-10, 10) ) >= 10 )
    a[0] = -10000000
    assert( _guessMax( N.arange(-10, 10) ) < 100 )
    assert( _guessMax( N.arange(-10, 10) ) >= 10 )
    return



if __name__ == '__main__':
    test_guessMin()



# version
__id__ = "$Id: Plot2dHist.py,v 1.4 2005/11/07 23:03:44 linjiao Exp $"

# End of file 
