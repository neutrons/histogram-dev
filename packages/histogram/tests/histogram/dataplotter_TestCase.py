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

interactive = False

from numpy  import array, arange

import unittest

from unittestX import TestCase
class dataplotter_TestCase(TestCase):


    def test_defaultPloter2D_plot(self):
        'plot: 2d'
        import pylab
        a, b = 3,10
        x, y, z = array(arange(a)), array(arange(b)), array( arange((a-1)*(b-1)) )
        z.shape = a-1, b-1

        self.plotter2.plot( x, y, z )
        if interactive:
            raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return

    def test_defaultPloter2D_contourplot(self):
        'contour plot: 2d'
        a, b = 3,10
        x, y, z = array(arange(a)), array(arange(b)), array( arange((a)*(b)) )
        z.shape = a, b
        
        self.plotter2.contourPlot( x, y, z )
        if interactive:
            raw_input('Press ENTER to continue')
        import pylab
        pylab.clf()
        pylab.close()
        return

    def test1D(self):
        "pylab plotter: 1D"
        self.plotter1.plot( [1,2,3], [1,2,3] )
        self.plotter1.plot( [1,2,3], [1,2,3], yerr = [0.1,0.1,0.1] )
        if interactive:
            raw_input('Press ENTER to continue')
        import pylab
        pylab.clf()
        pylab.close()
        return
    
    def test2D(self):
        "pylab plotter: 2D"
        import numpy
        I = numpy.arange( 0, 12, 1.)
        I.shape = 3,4
        self.plotter2.plot( [1,2,3], [1,2,3,4], I )
        if interactive:
            raw_input('Press ENTER to continue')
        import pylab
        pylab.clf()
        pylab.close()
        return
    
    def _test_sortxy_x(self):
        "histogram.data_plotter: sortxy_x"
        x = [3,1,2]
        y = [4,5,6]
        x1, y1 = sortxy_x( x, y )
        self.assertVectorEqual(x1, [1,2,3] )
        self.assertVectorEqual(y1, [5,6,4] )
        return


    def _test_sortxys_x(self):
        "histogram.data_plotter: sortxys_x"
        x = [3,1,2]
        ys = [4,5,6], [7,8,9]
        x1, y1s = sortxys_x( x, ys )
        self.assertVectorEqual(x1, [1,2,3] )
        self.assertVectorEqual(y1s[0], [5,6,4] )
        self.assertVectorEqual(y1s[1], [8,9,7] )
        return


    def __init__(self, *args, **kwds):
        super(dataplotter_TestCase, self).__init__(*args, **kwds)
        if not interactive:
            import matplotlib
            matplotlib.use('PS')
        from histogram.data_plotter import defaultPlotter1D, defaultPlotter2D
        if not interactive:
            defaultPlotter1D.interactive(0)
            defaultPlotter2D.interactive(0)
        self.plotter1 = defaultPlotter1D
        self.plotter2 = defaultPlotter2D
        return

    pass # end of dataplotter_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(dataplotter_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    global interactive
    interactive = True
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id: dataplotter_TestCase.py 1279 2007-07-19 16:02:10Z linjiao $"

# End of file 
