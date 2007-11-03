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

from histogram.data_plotter import defaultPlotter1D, defaultPlotter2D
import pylab


from numpy  import array, arange

import unittest

from unittestX import TestCase
class dataplotter_TestCase(TestCase):


    def test_defaultPloter2D_plot(self):
        'plot: 2d'
        from histogram.data_plotter import defaultPlotter2D as plotter
        a, b = 3,10
        x, y, z = array(arange(a)), array(arange(b)), array( arange((a-1)*(b-1)) )
        z.shape = a-1, b-1

        plotter.plot( x, y, z )
        raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return

    def test_defaultPloter2D_contourplot(self):
        'contour plot: 2d'
        from histogram.data_plotter import defaultPlotter2D as plotter
        a, b = 3,10
        x, y, z = array(arange(a)), array(arange(b)), array( arange((a)*(b)) )
        z.shape = a, b
        
        plotter.contourPlot( x, y, z )
        raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return

    def test1D(self):
        "pylab plotter: 1D"
        defaultPlotter1D.plot( [1,2,3], [1,2,3] )
        defaultPlotter1D.plot( [1,2,3], [1,2,3], yerr = [0.1,0.1,0.1] )
        raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return
        
    def test2D(self):
        "pylab plotter: 2D"
        import numpy
        I = numpy.arange( 0, 12, 1.)
        I.shape = 3,4
        defaultPlotter2D.plot( [1,2,3], [1,2,3,4], I )
        raw_input('Press ENTER to continue')
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

    pass # end of dataplotter_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(dataplotter_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id: dataplotter_TestCase.py 1279 2007-07-19 16:02:10Z linjiao $"

# End of file 
