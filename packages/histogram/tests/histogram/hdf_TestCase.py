#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

#import histogram
#histogram.use('numpy')
#from histogram.h5py import *
import os
from histogram.hdf import load, dump

import unittest
from unittestX import TestCase


class hdf_TestCase(TestCase):

    def testdump0(self):
        """ histogram.hdf: dump """
        from histogram import histogram, arange
        h = histogram('h',
                      [('x', arange(0,100, 1.) ),
                       ('y', arange(100, 180, 1.) ),],
                      unit = 'meter',
                      )

        filename = 'test0.h5'
        import os
        if os.path.exists( filename): os.remove( filename )
        dump( h, filename, '/', mode = 'c' )
        return


    def testdump0a(self):
        """ histogram.hdf: dump with compression"""
        from histogram import histogram, arange
        h = histogram('h',
                      [('x', arange(0,100, 1.) ),
                       ('y', arange(100, 180, 1.) ),],
                      unit = 'meter',
                      )

        filename = 'test0-compressed.h5'
        import os
        if os.path.exists( filename): os.remove( filename )
        dump( h, filename, '/', mode = 'c', compression=6 )
        return

    def testdump1(self):
        """ histogram.hdf: dump with fs specified"""
        filename = 'test1.h5'
        if os.path.exists( filename): os.remove( filename )

        from h5py import File
        fs = File( filename, 'w' )
        
        from histogram import histogram, arange
        h = histogram('h',
                      [('x', arange(0, 100, 1.) ),
                       ('y', arange(100, 180, 1.) ),],
                      unit = 'meter',
                      )
        #fs will take over
        dump( h, 'abc', '/', mode = 'w', fs = fs )
        self.assert_( os.path.exists( filename ))
        return

    def testdump2(self):
        'dump two histograms to one hdf'
        filename = 'testdump1.h5'
        import os
        if os.path.exists( filename): 
            os.remove( filename )

        from h5py import File
        fs = File( filename, 'w' )
        
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
        if os.path.exists(tmpfile): 
            os.remove( tmpfile )
        cmd =  'python -c "%s"' % cmd 
        if os.system( cmd ): 
            raise "%s failed" % cmd
        h = load( tmpfile, 'h' )
        for i in range(10):
            self.assertVectorAlmostEqual( h[i], (i,i) )
            continue
        return
    

    def testdump_and_load1a(self):
        'dump and load: continuous axis'
        tmpfile = 'test_dump_load_1a.h5'
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
        if os.path.exists(tmpfile): 
            os.remove( tmpfile )
        cmd =  'python -c "%s"' % cmd 
        if os.system( cmd ): 
            raise "%s failed" % cmd
        h = load( tmpfile, 'h' )
        assert not h.axes()[0].isDiscrete()
        return
    

    def testdump_and_load1b(self):
        'dump and load: discrete axis'
        tmpfile = 'test_dump_load_1b.h5'
        cmd = '''
from histogram import histogram
x = y = range(10)
h = histogram( 
    'h',
    [ ('tID', x) ],
    data = y, errors = y )
import histogram.hdf as hh
hh.dump( h, '%s', '/', 'c' )
''' % tmpfile
        import os
        if os.path.exists(tmpfile): 
            os.remove( tmpfile )
        cmd =  'python -c "%s"' % cmd 
        if os.system( cmd ): 
            raise "%s failed" % cmd
        h = load( tmpfile, 'h' )
        axis = h.axes()[0]
        self.assert_(axis.isDiscrete())
        self.assertEqual(axis.name(), 'tID')
        return
    

    def testdump_and_load1c(self):
        'dump and load: meta data'
        tmpfile = 'test_dump_load_1c.h5'
        cmd = '''
from histogram import histogram
x = y = range(10)
h = histogram( 
    'h',
    [ ('tID', x) ],
    data = y, errors = y )
h.setAttribute('instrument', 'ARCS')
axis = h.axes()[0]
axis.setAttribute('pi', 3.14)
import histogram.hdf as hh
hh.dump( h, '%s', '/', 'c' )
''' % tmpfile
        import os
        if os.path.exists(tmpfile): 
            os.remove( tmpfile )
        cmd =  'python -c "%s"' % cmd 
        if os.system( cmd ): 
            raise "%s failed" % cmd
        h = load( tmpfile, 'h' )
        axis = h.axes()[0]
        self.assert_(axis.isDiscrete())
        self.assertEqual(axis.name(), 'tID')
        self.assertEqual(h.getAttribute('instrument'), 'ARCS')
        data = h.data()
        self.assertEqual(axis.attribute('pi'), 3.14)
        return
    

    def testdump_and_load2(self):
        'dump and load in the same process'
        tmpfile = 'test_dump_load2.h5'
        if os.path.exists( tmpfile ):
            os.remove( tmpfile )

        from h5py import File
        fs = File( tmpfile, 'w' )
        
        from histogram import histogram
        x = y = range(10)
        h = histogram( 
            'h',
            [ ('x', x) ],
            data = y, errors = y )
        import histogram.hdf as hh
        hh.dump( h, tmpfile, '/',  fs = fs )
        h = load( tmpfile, 'h')
        #print h[1]
        self.assertVectorAlmostEqual( h[1], (1,1) )
        return

    
    def test_slice_and_dump(self):
        'slice a histogram and dump the slice'
        tmpfile = 'test_slice_and_dump.h5'
        if os.path.exists( tmpfile ):
            os.remove( tmpfile )

        from histogram import histogram
        x = y = range(100)
        h = histogram( 
            'h',
            [ ('x', x) ],
            data = y, errors = y )
        s = h[(3,10)]
        import histogram.hdf as hh
        hh.dump(s, tmpfile, '/',  'c')
        return
    

    def test_load_slice_and_dump(self):
        'load a histogram and dump a slice of it'
        tmpfile = 'test_load_slice_and_dump.h5'
        if os.path.exists( tmpfile ):
            os.remove( tmpfile )

        import histogram.hdf as hh
        h = hh.load('testload.h5', '/h')
        s = h[(10, 30), ()]
        hh.dump(s, tmpfile, '/',  'c')
        return
    

    def testload(self):
        'load simplest histogram'
        h = load( 'testload.h5', '/h' )
        return

    def testload1(self):
        'load histogram with unit'
        h = load( 'testload.h5', '/h1' )
        return

    def testload2(self):
        'load histogram with one path string'
        #h = load( 'testload.h5/h' )
        h = load( 'sqe.h5/S(Q,E)' )
        return

    def testload3(self):
        'load a slice of a histogram '
        tmpfile = "tmp.h5"
        if os.path.exists( tmpfile): os.remove(tmpfile)

        cmd = "from histogram.hdf import dump; from histogram import histogram, arange; h = histogram( 'h', [ ('xID', range(10)), ('y', arange(0, 1,0.1)) ] ); from numpy import array; d = array(range(100)); d.shape = 10,10; h[{}] = d, 0; dump(h, %r, '/', 'c') " % tmpfile
        os.system( 'python -c %r' % cmd )
        if not os.path.exists( tmpfile ): raise "failed to create tmp h5 file of historam"

        h1 = load( tmpfile, 'h', xID=(3,6) )
        assert h1.shape() == (4,10)
        d = h1.data().storage().asNumarray().copy()
        d.shape = 40,
        print d
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

    def testload5(self):
        'load with fs specified'
        filename = 'tmp.h5'
        filename = 'test_dump_load2.h5'
        from h5py import File
        fs = File(filename)
        h = load( filename, '/h', fs = fs )
        return
    

    def testload6(self):
        '''load with fs specified: catch error when there is mismatch in the 
        mode of fs and the load method
        '''
        orig = 'testload.h5'
        filename = 'testload6.h5'
        import shutil
        shutil.copyfile( orig, filename )
        from h5py import File
        fs = File( filename, 'w' )

        # self.assertRaises( IOError, load, filename, '/h', fs )
        self.assertRaises( KeyError, load, filename, '/h', fs )
        return


    def testload7(self):
        'load histogram that is only one entry with just the filename'
        h = load( 'sqe.h5' )
        return



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
