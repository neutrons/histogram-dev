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
from unittestX import TestCase


class hdf_TestCase(TestCase):


    def testdump(self):
        """ histogram.hdf: dump """
        from histogram import histogram, arange
        h = histogram('h',
                      [('x', arange(0,100, 1.) ),
                       ('y', arange(100, 180, 1.) ),],
                      unit = 'meter',
                      )

        filename = 'test.h5'
        import os
        if os.path.exists( filename): os.remove( filename )
        dump( h, filename, '/', mode = 'c' )
        return


    def testload(self):
        'load simplest histogram'
        h = load( 'testload.h5', '/h' )
        return

    def testload1(self):
        'load histogram with unit'
        h = load( 'testload.h5', '/h1' )
        return

    def testdump_and_load(self):
        'dump and load'
        tmpfile = 'test_dump_load_hdf5.h5'
        cmd = '''
from histogram import histogram
x = y = range(10)
h = histogram( 
    'h',
    [ ('x', x) ],
    data = y, errors = y )
import histogram.hdf as hh
hh.dump( h, '%s', '/', 'c' )
''' % tmpfile
        import os
        if os.path.exists(tmpfile): os.remove( tmpfile )
        
        cmd =  'python -c "%s"' % cmd 
        if os.system( cmd ): raise "%s failed" % cmd

        h = load( tmpfile, 'h' )
        self.assertVectorAlmostEqual( h[1], (1,1) )
        return

    def testload2(self):
        'load histogram with one path string'
        h = load( 'testload.h5/h' )
        return

    def testload3(self):
        'load a slice of a histogram '
        tmpfile = "tmp.h5"
        import os
        if os.path.exists( tmpfile): os.remove(tmpfile)

        cmd = "from histogram.hdf import dump; from histogram import histogram, arange; h = histogram( 'h', [ ('xID', range(10)), ('y', arange(0, 1,0.1)) ] ); from numpy import array; d = array(range(100)); d.shape = 10,10; h[{}] = d, 0; dump(h, %r, '/', 'c') " % tmpfile
        os.system( 'python -c %r' % cmd )
        if not os.path.exists( tmpfile ): raise "failed to create tmp h5 file of historam"

        h1 = load( tmpfile, 'h', xID=(3,6) )
        assert h1.shape() == (4,10)
        d = h1.data().storage().asNumarray().copy()
        d.shape = 40,
        self.assertVectorAlmostEqual( d, range(30,70) )

        self.assertVectorEqual(
            h1.axisFromId(1).binCenters(), (3,4,5,6) )

        from numpy import arange
        self.assertVectorAlmostEqual(
            h1.axisFromId(2).binCenters(), arange(0,1,0.1) )

        
        h2 = load( tmpfile, 'h', xID=(3,6), y=(0.4,0.5) )
        assert h2.shape() == (4,2)
        d = h2.data().storage().asNumarray().copy()
        d.shape = 8,
        self.assertVectorAlmostEqual(
            d, (34,35,44,45,54,55,64,65) )

        self.assertVectorEqual(
            h2.axisFromId(1).binCenters(), (3,4,5,6) )

        from numpy import arange
        self.assertVectorAlmostEqual(
            h2.axisFromId(2).binCenters(), (0.4,0.5) )
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
