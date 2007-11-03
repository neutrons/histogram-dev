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


from histogram.plotter import defaultPlotter
from histogram import *
import pylab


import unittest


from unittestX import TestCase
class plotter_TestCase(TestCase):

    def test1D(self):
        "pylab plotter: 1D"
        h = histogram('h', [('x', arange(10))], fromfunction=lambda x: x*x)
        defaultPlotter.plot(h)
        raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return
        
    def test2D(self):
        "pylab plotter: 2D"
        h = histogram(
            'h',
            [('x', arange(10)),
             ('y', arange( 5 )),
             ],
            fromfunction=lambda x,y: x*x + y*y)
        defaultPlotter.plot(h)
        raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return
    
    pass # end of plotter_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(plotter_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
##     journal.debug('instrument').activate()
##     journal.debug('instrument.elements').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id: plotter_TestCase.py 834 2006-03-03 14:39:02Z linjiao $"

# End of file 
