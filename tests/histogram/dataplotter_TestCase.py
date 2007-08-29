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

from histogram.data_plotter import *


import unittest

from unittestX import TestCase
class dataplotter_TestCase(TestCase):


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
