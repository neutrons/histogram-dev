#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from histogram.hdf import *


import unittest
from unittest import TestCase


class hdf_TestCase(TestCase):


    def testdump(self):
        """ histogram.hdf: dump """
        from histogram import histogram, arange
        h = histogram('h',
                      [('x', arange(0,100, 1.) ),
                       ('y', arange(100, 180, 1.) ),]
                      )
        import os
        os.remove( 'test.h5' )
        dump( h, 'test.h5', '/', mode = 'c' )
        return


    def testload(self):
        h = load( 'testload.h5', '/h' )
        print h
        return

    pass # end of Dataset_TestCase



def pysuite():
    suite1 = unittest.makeSuite(hdf_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()




# version
__id__ = "$Id: hdf_TestCase.py 1209 2006-11-16 18:51:55Z linjiao $"

# End of file 
