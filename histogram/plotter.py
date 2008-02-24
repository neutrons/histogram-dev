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


## \namespace histogram.plotter
## This histogram plotter plot a histogram
##
## Currently only 1d and 2d plots are suppported
##


import journal
warning = journal.warning( "histogram.plotter" )

class HistogramPlotter:

    def interactive(self, b):
        """if b is True, control will go back to python prompt after plotting
        """
        raise NotImplementedError , "%s must override interactive" % (
            self.__class__.__name__)
    

    def plot(self, hist, **kwds):
        dim = hist.dimension()

        if dim > 2:
            raise NotImplementedError , "dim=%s" % (dim,)
            warning.log( "NotImplementedError: dim = %s" % dim )
            return
        plot = getattr( self, "plot%dd" % dim )
        plot(hist, **kwds)
        return


    def clear(self):
        raise NotImplementedError, "clear"

    
    def plot1d(self, hist, **kwds):
        raise NotImplementedError , "plot 1d curve"

    def plot2d(self, hist, **kwds):
        raise NotImplementedError , "plot 2d image"

    pass # end of HistogramPlotter



from data_plotter import MplPlotter1D, MplPlotter2D


def axis_label( axis ):
    label = axis.name()
    if len( str(axis.unit()) )>0: label = label + "(%s)" % axis.unit()
    return label

    
class HistogramMplPlotter(HistogramPlotter):

    def __init__(self, figure = None):
        self.dp1 = MplPlotter1D( figure )
        self.dp2 = MplPlotter2D( figure )
        return


    def interactive(self, b):
        self.dp1.interactive(b)
        self.dp2.interactive(b)
        return

    
    def clear(self):
        self.dp1.clear()
        return


    def plot1d(self, hist, **kwds ):
        figure = self.dp1.get_figure()
        assert hist.dimension() == 1, "dimension error: %s" % hist.dimension()

        size = hist.shape()[0]
        if size > (display_size*10) : hist = resample( hist, display_size )
        
        xaxis = hist.axisFromId(1)
        x = xaxis.binCenters()
        y = hist.data().storage().asNumarray()
        from numpy import sqrt
        eb = sqrt(hist.errors().storage().asNumarray())
        self.dp1.plot(x,y, yerr = eb, **kwds)
        f = figure
        axes = f.gca()
        axes.set_title( hist.name() )
        axes.set_xlabel( axis_label(xaxis) )
        axes.set_ylabel( "Intensity (unit: %s)" % hist.unit() )
        self._image = self.dp1.get_image()
        return


    def plot2d(self, hist, **kwds):
        assert hist.dimension() == 2, "dimension error: %s" % hist.dimension()
        xaxis = hist.axisFromId(1)
        x = xaxis.binCenters()
        yaxis = hist.axisFromId(2)
        y = yaxis.binCenters()

        from histogram import boundariesFromCenters
        x = boundariesFromCenters( x )
        y = boundariesFromCenters( y )
        
        z = hist.data().storage().asNumarray()
##         ly, lx = z.shape
##         if len(x) == ly and len(y) == lx:
##             from numpy import transpose
##             z = transpose(z)
##             pass
##         elif len(x) == lx and len(y) == ly:
##             pass
##         else: raise "Shape mismatch: len(x) = %s, len(y) = %s, z.shape = %s" % (
##             len(x), len(y), z.shape )
        
        self.dp2.plot(x,y,z, **kwds)
        
        f = self.dp2.get_figure()
        axes = f.gca()
        axes.set_title( hist.name() )
        axes.set_xlabel( axis_label(xaxis) )
        axes.set_ylabel( axis_label(yaxis) )
        self._image = self.dp2.get_image()
        return


    def image(self): return self._image

    pass # end of HistogramMplPlotter


defaultPlotter = HistogramMplPlotter()

def plot1d( histogram, *args ):
    defaultPlotter.plot1d( histogram, *args )
    return

def plot2d( histogram, *args, **kwds ):
    defaultPlotter.plot2d( histogram, *args, **kwds )
    return




display_size = 1000
def resample( hist1, size ):

    import histogram as H
    
    assert hist1.dimension() == 1
    assert hist1.shape()[0] > display_size*10
    xaxis = hist1.axes()[0]
    xbb = xaxis.binBoundaries().asNumarray()
    front, back = xbb[0], xbb[-1]
    step = (back-front)/size
    newxbb = H.arange( front, back+step/2, step)
    newxaxis = H.axis( xaxis.name(), boundaries = newxbb, unit = xaxis.unit() )

    newhist = H.histogram(
        hist1.name(),
        [ newxaxis ] )

    newxc = newxaxis.binCenters()
    for x in newxc[1:-1] :
        newhist[ x ] = hist1[ (x-step/2, x+step/2) ].sum()
        continue

    newhist[ newxc[0] ]= hist1[ (newxbb[0], newxc[0] + step/2) ].sum()
    newhist[ newxc[-1] ]= hist1[ (newxc[-1]-step/2, newxbb[-1]-step*1.e-10) ].sum()

    return newhist
        

# version
__id__ = "$Id: Plot2dHist.py,v 1.4 2005/11/07 23:03:44 linjiao Exp $"

# End of file 
