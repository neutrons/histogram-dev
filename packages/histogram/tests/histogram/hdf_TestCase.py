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
import os


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


    def testdump1(self):
        """ histogram.hdf: dump with fs specified"""
        filename = 'test1.h5'
        import os
        if os.path.exists( filename): os.remove( filename )

        from hdf5fs.h5fs import H5fs
        fs = H5fs( filename, 'c' )
        
        from histogram import histogram, arange
        h = histogram('h',
                      [('x', arange(0,100, 1.) ),
                       ('y', arange(100, 180, 1.) ),],
                      unit = 'meter',
                      )
        #fs will take over
        dump( h, 'abc', '/', mode = 'r', fs = fs )
        self.assert_( os.path.exists( filename ))
        return


    def testdump2(self):
        'dump two histograms to one hdf'
        filename = 'testdump1.h5'
        import os
        if os.path.exists( filename): os.remove( filename )

        from hdf5fs.h5fs import H5fs
        fs = H5fs( filename, 'c' )
        
        from histogram import histogram, arange
        h = histogram('h',
                      [('x', arange(0,100, 1.) ),
                       ('y', arange(100, 180, 1.) ),],
                      unit = 'meter',
                      )
        dump( h, None, '/', fs = fs )
        
        h2 = histogram('h2',
                      [('x', arange(0,100, 1.) ),
                       ('y', arange(100, 180, 1.) ),],
                      unit = 'meter',
                      )
        dump( h2, None, '/', fs = fs )

        #load histogram
        h2c = load( filename, '/h2', fs = fs )
        print h2c

        self.assert_( os.path.exists( filename ))
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

    def testdump_and_load2(self):
        'dump and load in the same process'
        tmpfile = 'test_dump_load2.h5'
        if os.path.exists( tmpfile ): os.remove( tmpfile )

        from hdf5fs.h5fs import H5fs
        fs = H5fs( tmpfile, mode = 'c' )
        
        from histogram import histogram
        x = y = range(10)
        h = histogram( 
            'h',
            [ ('x', x) ],
            data = y, errors = y )
        import histogram.hdf as hh
        hh.dump( h, tmpfile, '/',  fs = fs )

        h = load( tmpfile, 'h', fs = fs )
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

    def testload5(self):
        'load with fs specified'
        filename = 'testload.h5'
        from hdf5fs.h5fs import H5fs
        fs = H5fs( filename, 'r' )
        
        h = load( filename, '/h', fs = fs )
        return

    def testload6(self):
        'load with fs specified'
        orig = 'testload.h5'
        filename = 'testload6.h5'
        import shutil
        shutil.copyfile( orig, filename )
        from hdf5fs.h5fs import H5fs
        fs = H5fs( filename, 'c' )

        self.assertRaises( IOError, load, filename, '/h', fs )
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
