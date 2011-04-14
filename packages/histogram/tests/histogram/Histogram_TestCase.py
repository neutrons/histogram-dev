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


import histogram, numpy as np

def createHistogram(noerror = False):
    from histogram import createContinuousAxis, arange, createDiscreteAxis
    #create axis E
    axisE = createContinuousAxis( 'E', 'meter', arange(0.5, 3.5, 1.0) )
    
    #create axis "tubeId"
    axisTubeId = createDiscreteAxis( "tubeId", [1, 3, 99], 'int')
    
    #create histogram
    data = errors = np.arange(9)
    data.shape = 3,3
    
    if noerror: errors = None

    return histogram.histogram(
        name = 'I(E, TubeId)', data = data, errors = errors,
        axes = [axisE, axisTubeId])
    


import unittest

from unittestX import TestCase
class Histogram_TestCase(TestCase):


    def __init__(self, *args, **kwds):
        TestCase.__init__(self, *args, **kwds)
        self._histogram = createHistogram()
        self._histogram2 = createHistogram()
        return


    def test__str__(self):
        "Histogram: __str__"
        histogram = self._histogram
        print histogram
        return


    def test_as_floattype(self):
        from histogram import histogram, arange
        h = histogram( 'h', [ ('x',arange(10)) ], data_type = 'int')
        h1 = h.as_floattype()
        self.assertEqual( h1.typeCode(), 6 )
        self.assert_( h1.axisFromName( 'x' ) is not h.axisFromName( 'x' ) )
        return
    

    def testindexes(self):
        "Histogram: indexes"
        histogram = self._histogram
        #test
        self.assertVectorEqual( histogram.indexes( (0.5, 1) ), (0,0) )
        self.assertVectorEqual( histogram.indexes( (0.5, 99) ), (0,2) )
        self.assertVectorEqual( histogram.indexes( (1.1, 3) ), (1,1) )
        return


    def testTranspose(self):
        "Histogram: transpose"
        histogram = self._histogram
        print "before transpose: %s" % histogram
        histogram = histogram.transpose()
        print "after transpose: %s" % histogram
        self.assertVectorEqual( histogram.indexes( (1, 0.5) ), (0,0) )
        self.assertVectorEqual( histogram.indexes( (99, 0.5) ), (2,0) )
        self.assertVectorEqual( histogram.indexes( (3, 1.1) ), (1,1) )
        return


    def testSum(self):
        "Histogram: sum"
        histogram = self._histogram
        I_tubeId = histogram.sum( "E" )
        I_E = histogram.sum( "tubeId" )
        return


    def testSlicing(self):
        "Histogram: slicing"
        histogram = self._histogram
        #get element
        self.assertVectorEqual( histogram[1.5,1], (3,3) )
    
        #get slice
        from histogram.SlicingInfo import SlicingInfo, all, front, back

        slice1 = histogram[SlicingInfo((0.5, 1.5)), SlicingInfo((1,3))]
        self.assertVectorEqual( slice1.shape(), (2,2 ) )
        print slice1.name()

        slice1 = histogram[(0.5, 1.5), (1,3)]
        self.assertVectorEqual( slice1.shape(), (2,2 ) )
        print slice1.name()

        slice2 = histogram[0.5, SlicingInfo((1,3))]
        self.assertVectorEqual(slice2.shape(), (2,) )

        slice2 = histogram[0.5, (1,3)]
        self.assertVectorEqual(slice2.shape(), (2,) )

        slice3 = histogram[all, 99]
        self.assertVectorEqual(slice3.shape(), (3,) )
        
        slice3 = histogram[(), 99]
        self.assertVectorEqual(slice3.shape(), (3,) )

        slice3a = slice3[ SlicingInfo( (1.5, back) ) ]
        self.assertVectorEqual(slice3a.shape(), (2,) )
        
        slice3a = slice3[ (1.5, None) ]
        self.assertVectorEqual(slice3a.shape(), (2,) )        
        
        slice4 = histogram[all, all]
        self.assertVectorEqual(slice4.shape(), (3,3) )

        slice4 = histogram[(), ()]
        self.assertVectorEqual(slice4.shape(), (3,3) )

        slice5 = histogram[SlicingInfo( (1.5,back) ), all]
        self.assertVectorEqual(slice5.shape(), (2,3) )
        
        slice5 = histogram[(1.5, None), ()]
        self.assertVectorEqual(slice5.shape(), (2,3) )
        
        slice6 = histogram[SlicingInfo( (front,1.5) ), all]
        self.assertVectorEqual(slice6.shape(), (2,3) )
        
        slice6 = histogram[(None,1.5), ()]
        self.assertVectorEqual(slice6.shape(), (2,3) )

        #getitem with units
        from histogram._units import length
        meter = length.meter
        slice8 = histogram[ {'E':(0.5*meter, 1.5*meter), 'tubeId':(1,3)} ]
        self.assertVectorEqual(slice8.shape(), (2,2))

        #getitem for 1D histogram
        number7 = histogram[ 1.5, () ][3]

        #getitem using dictionary
        number7 = histogram[ {'E':1.5, 'tubeId':3} ]
        number7 = histogram[ 1.5, () ][ {'tubeId':3} ]
        # special test case: coordinate = 0
        from histogram import histogram, axis
        detIDaxis = axis('detID', range(5))
        h = histogram( 'h', [detIDaxis])
        h[ {'detID':0 } ]

        #get slice. units envolved
        h = histogram( 'distance',
                       [ ('x', [1,2,3] ),
                         ],
                       unit = 'meter', data = [1,2,3] )
        h1 = h[(2,3)]
        self.assertEqual( h1.unit(), h.unit() )
        return


    def testSlicingIsRefering(self):
        #slice is just a reference, not a copy
        from histogram import histogram
        h = histogram( 'h', [('a', [1,2,3]),('b', [4,5])] )
        from numpy import ones
        h[(),()] = ones( (3,2) ), ones((3,2) )
        self.assertVectorAlmostEqual( h[1,4], (1,1) )
        sh = h[1,()]
        sh.clear()
        self.assertVectorAlmostEqual( h[1,4], (0,0) )
        return


    def testReplaceAxis(self):
        'Hisogram: replaceAxis'
        from histogram import histogram, axis, arange
        a = axis('a', arange(1,10,1.0))
        b = axis('b', arange(1,100,10.))
        h = histogram( 'h', [a] )
        self.assert_(a is h.axisFromName('a'))
        h.replaceAxis(name='a', axis=b)
        self.assert_(b is h.axisFromName('a'))
        return
    
        
    def testSetItem(self):
        "Histogram: h[ x,y,z ] = value"
        from histogram import histogram
        h = histogram( 'h', [('a', [1,2,3]),('b', [4,5])] )
        h[ 1,5 ] = 1,1
        self.assertVectorAlmostEqual(
            h.data().storage().asList(), [0,1,0,0,0,0] )
        self.assertVectorAlmostEqual(
            h.errors().storage().asList(), [0,1,0,0,0,0] )

        self.assertVectorAlmostEqual( h[1,5], (1,1) )

        h = histogram( 'h', [('a', [1,2,3])] )
        h[1] = 10,10

        h = histogram( 'h', [('a', [1,2,3])], unit = 'meter')
        from pyre.units.length import meter
        h[1] = 10*meter,10*meter*meter
        return



    def testIadd_and_SetItem(self):
        "Histogram: h[ x,y,z ] += sth"
        from histogram import histogram
        h = histogram( 'h', [('a', [1,2,3]),('b', [4,5])] )
        import numpy as N
        h[ 1,5 ] = N.array( [1,1] )
        return



    def testClear(self):
        "Histogram: h.clear()"
        from histogram import histogram
        h = histogram( 'h', [('a', [1,2,3]),('b', [4,5])] )
        from numpy import ones
        h[(),()] = ones( (3,2) ), ones( (3,2) )
        self.assertVectorAlmostEqual( h[1,4] , (1,1) )
        h.clear()
        self.assertVectorAlmostEqual(
            h.data().storage().asList(), [0,0,0,0,0,0] )
        self.assertVectorAlmostEqual(
            h.errors().storage().asList(), [0,0,0,0,0,0] )
        return


    def testSetSlice(self):
        "Histogram: h[ slices ] = rhs"
        histogram = self._histogram.copy()
        #set element
        histogram[1.5,1] = (2,4)
        self.assertVectorEqual( histogram[1.5,1], (2,4) )

        #set slice
        from histogram.SlicingInfo import SlicingInfo, all, front, back
        from histogram import createDataset
        from numpy import array
        
        data = createDataset( "data", shape = [2,2] )
        data[:,:] = array( [ [1,2],
                             [3,4], ] )
        errs = createDataset( "errs", shape = [2,2] )
        errs[:,:] = array( [ [1,2],
                             [3,4], ] )

        histogram[SlicingInfo((0.5, 1.5)), SlicingInfo((1,3))] = data,errs
        self.assertVectorEqual( histogram[0.5,1], (1,1) )
        self.assertVectorEqual( histogram[0.5,3], (2,2) )
        self.assertVectorEqual( histogram[1,1], (3,3) )
        self.assertVectorEqual( histogram[1,3], (4,4) )

        histogram[(0.5, 1.5),(1,3)] = data,errs
        self.assertVectorEqual( histogram[0.5,1], (1,1) )
        self.assertVectorEqual( histogram[0.5,3], (2,2) )
        self.assertVectorEqual( histogram[1,1], (3,3) )
        self.assertVectorEqual( histogram[1,3], (4,4) )

        
        from histogram import makeHistogram
        name = "h"
        axes = [
            ('x', [1,2]),
            ('y', [1,2]),
            ]
        data = array( [ [1,2], [3,4] ] )
        errs = array( [ [1,2], [3,4] ] )
        h2 = makeHistogram( name, axes, data, errs )
        histogram[SlicingInfo((0.5, 1.5)), SlicingInfo((1,3))] = h2

        #setslice: rhs is a histogram
        histogram[(0.5, 1.5), (1,3)] = h2

        # setslice: rhs is a list of arrays
        histogram[(0.5, 1.5), (1,3)] = data, errs
        
        # setslice: rhs is a list of arrays including None
        histogram[(0.5, 1.5), (1,3)] = data, None

        # setslice: rhs is a lit of arrays. histogram is 1D
        data = array([1,2]); errs = data;
        histogram[ 0.5, () ] [ (1,3) ] = data, errs

        # setslice: rhs is a tuple of two numbers
        histogram[ 0.5, () ] [ (1,3 )]  = 0., 0.
        
        #setitem using dictionary
        histogram[ {'E':1.5, 'tubeId':3} ] = 3, 3
        self.assertVectorAlmostEqual(
            histogram[ {'E':1.5, 'tubeId':3} ], (3, 3) )

        histogram[ {'E':1.5} ][ {'tubeId':3} ] = 3, 3
        self.assertVectorAlmostEqual(
            histogram[ {'E':1.5, 'tubeId':3} ], (3, 3) )

        #
        histogram[ {'E':1.5} ] /= 3,3
        histogram[ {'E':1.5} ] /= 3,3
        return


    def test__iadd__(self):
        "histogram: h+=b"
        h = self._histogram.copy()
        h += (1,0)
        self.assertVectorEqual( h[0.5, 1], (1,0) )

        h = self._histogram.copy()
        h2 = self._histogram2
        h += h2
        self.assertVectorEqual( h[1.5,1], (6,6) )
        return
    
    
    def test__isub__(self):
        "histogram: h-=b"
        h = self._histogram.copy()
        h -= (1,2)
        self.assertVectorEqual( h[0.5, 1], (-1,2) )

        h = self._histogram.copy()
        h2 = self._histogram2
        h -= h2
        self.assertVectorEqual( h[1.5,1], (0,6) )
        return
    
    
    def test__imul__(self):
        "histogram: h*=b"
        h = self._histogram.copy()
        h *= (2,1)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (2,5) )
        return


    def test__imul__2(self):
        "histogram: h*=h2"
        h = self._histogram.copy()
        h2 = self._histogram2
        h *= h2
        self.assertVectorEqual( h[1.5,1], (9,54) )

        import histogram
        h3 = self._histogram.copy()
        h4 = histogram.histogram('h3', h2.axes(), data = h2.I, errors = h2.E2, unit = 'meter' )
        h3 *= h4
        self.assertEqual( h3.unit(), h4.unit() )
        self.assertEqual( h3.unit(), h3.data().unit() )
        self.assertEqual( h3.unit()**2, h3.errors().unit() )
        from histogram._units import length
        meter = length.meter
        self.assertVectorEqual( h3[1.5,1], (9*meter,54*meter**2) )
        return
    
    
    def test__idiv__(self):
        "histogram: h/=b"
        h = self._histogram.copy()
        h /= (2,1)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (0.5,5./16) )

        h = self._histogram.copy()
        h /= (2,0)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (0.5,1./4) )
        return
    

    def test__idiv__2(self):
        "histogram: h/=h1"
        h = self._histogram.copy()
        h2 = self._histogram2
        h /= h2
        self.assertVectorAlmostEqual( h[1.5,1], (1,2.0/3) )

        h = self._histogram.copy()
        h2 = createHistogram( noerror = True )
        h /= h2
        self.assertVectorAlmostEqual( h[1.5,1], (1,1./3) )

        from histogram import histogram, axis, arange, datasetFromFunction
        x = axis('x', arange(1, 2, .2 ) )
        y = axis('y', arange(0, 3, .5 ) )
        def fa(x,y): return x*y + x
        ha = histogram('a', [x,y], datasetFromFunction( fa, (x,y) ) )
        for xi in x.binCenters():
            for yi in y.binCenters():
                self.assertAlmostEqual( fa(xi,yi), ha[xi,yi][0] )
        
        def fb(x,y): return x
        hb = histogram('b', [x,y], datasetFromFunction( fb, (x,y) ) )
        hc = ha/hb
        for xi in x.binCenters():
            for yi in y.binCenters():
                self.assertAlmostEqual( yi+1, hc[xi,yi][0] )

        def fberr(x,y): return 0*x
        hb = histogram('b', [x,y], datasetFromFunction( fb, (x,y) ),
                       datasetFromFunction( fberr, (x,y) ) )
        hc = ha/hb
        for xi in x.binCenters():
            for yi in y.binCenters():
                self.assertAlmostEqual( yi+1, hc[xi,yi][0] )

        #involve units
        h1 = histogram(
            'h1',
            [ ('x', [1,2,3]),
              ],
            unit = 'meter',
            data = [1,2,3],
            errors = [1,2,3],
            )
        h2 = histogram(
            'h2',
            [ ('x', [1,2,3]),
              ],
            data = [1,1,1],
            errors = [1,1,1],
            unit = 'second',
            )
        h3 = h1/h2
        self.assertVectorAlmostEqual( h3.I, (1,2,3) )
        self.assertVectorAlmostEqual( h3.E2, (2,6,12) )
        return


    def test__add__(self):
        "histogram: h+b"
        h = self._histogram + (1,0)
        self.assertVectorEqual( h[0.5, 1], (1,0) )

        h = self._histogram + self._histogram2
        self.assertVectorEqual( h[1.5,1], (6,6) )

        h1 = histogram.histogram( 'h1', [ ['x', range(10)] ] )
        h1[()] = 1,1
        
        h2 = histogram.histogram( 'h2', [ ['x', range(10)] ] )
        h2[()] = 2,2

        h1*=(2.,0)
        h2/=(2.,0)

        h3 = h1+h2
        for x in range(10): self.assertAlmostEqual( h3[x][0], 3 )
        return
    
    
    def test__sub__(self):
        "histogram: h-b"
        h = self._histogram - (1,2)
        self.assertVectorEqual( h[0.5, 1], (-1,2) )

        h = (1,2)  - self._histogram
        self.assertVectorEqual( h[0.5, 1], (1,2) )

        h = self._histogram - self._histogram2
        self.assertVectorEqual( h[1.5,1], (0,6) )
        return
    
    
    def test__mul__(self):
        "histogram: h*b"
        h = self._histogram * (2.,1.)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (2,5) )

        h = self._histogram * self._histogram2
        self.assertVectorEqual( h[1.5,1], (9,54) )
        return
    
    
    def test__div__(self):
        "histogram: h/b"
        h = self._histogram / (2,1)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (0.5,5./16) )

        h = (2,1) / self._histogram 
        self.assertVectorEqual( h[0.5, 3], (2,5.) )

        h = self._histogram / self._histogram2
        self.assertVectorAlmostEqual( h[1.5,1], (1,2./3) )
        return


    def test_dump(self):
        "Histogram: pickle.dump"
        import pickle
        h = self._histogram
        pickle.dump( h, open( "tmp.pkl", 'w' ) )
        return


    def test_load(self):
        "Histogram: pickle.load"
        import pickle
        h = self._histogram
        pickle.dump( h, open( "tmp.pkl", 'w' ) )
        h1 = pickle.load( open("tmp.pkl") )
        self.assertEqual( h.name(), h1.name() )
        print ("data=%s" % h1.data().storage().asNumarray() ) 
        self.assert_( h.data().storage().compare( h1.data().storage() ) )
        print ("errors=%s" % h1.errors().storage().asNumarray() ) 
        self.assert_( h.errors().storage().compare( h1.errors().storage() ) )

        for axisName in h.axisNameList():
            print ("axis %s" % axisName)
            axis = h.axisFromName( axisName )
            axis1 = h1.axisFromName( axisName )
            self.assert_( axis.storage().compare( axis1.storage() ) )
            continue

        from histogram import histogram
        h2 = histogram(
            'h2',
            [ ('x', [1,2,3]),
              ],
            unit = 'meter' )
        pickle.dump( h2, open( "tmp.pkl", 'w' ) )
        h2a = pickle.load( open("tmp.pkl") )
        
        return


    def test_reduce(self):
        "reduce(histogram)"
        from histogram import makeHistogram
        name = "h"
        axes = [ ('x', [1,2,3]), ('yID', [1]) ]
        data = [ [1],[2],[3] ]
        errs = [ [1],[2],[3] ]
        h = makeHistogram( name, axes, data, errs )
        h.reduce()
        shape = h.shape()
        self.assertEqual( shape, (3,))
        return


    def test_axisFromId(self):
        "Histogram: axisFromId"
        from histogram import histogram, axis, arange
        x = axis( 'x', arange(1., 10., 1.) )
        y = axis( 'y', arange(-1., 1., 0.1) )
        h = histogram('h', (x,y) )
        self.assertEqual( h.axisFromId(1), x )
        self.assertEqual( h.axisFromId(2), y )
        return


    def test_values2indexes(self):
        "Histogram: values2indexes"
        from histogram import histogram, axis, arange
        x = axis( 'x', arange(1., 10., 1.) )
        y = axis( 'y', arange(-1., 1., 0.1) )
        h = histogram('h', (x,y) )
        self.assertVectorEqual( h.values2indexes( (2, 0.2) ), (1,12) )
        return


    def test_getattribute(self):
        'Histogram: __getattribute__'
        from histogram import histogram, axis, arange
        x = axis( 'x', arange(1., 10., 1.) )
        y = axis( 'y', arange(-1., 1., 0.1) )
        h = histogram('h', (x,y) )
        self.assertVectorEqual( h.x, x.binCenters() )
        self.assertVectorEqual( h.y, y.binCenters() )
        
        t1 = h.I; t2 = h.data().storage().asNumarray() 
        t1.shape = t2.shape = -1, 
        self.assertVectorEqual( t1, t2 )
        
        t1 = h.E2; t2 = h.errors().storage().asNumarray() 
        t1.shape = t2.shape = -1, 
        self.assertVectorEqual( t1, t2 )

        return


    def test_rename(self):
        "Histogram: rename"
        import tempfile
        outh5 = tempfile.mktemp()
        code = """
from histogram import histogram, arange
h = histogram('h', [('x', arange(10), 'meter')])
h.I = h.x*h.x
h.setAttribute('name', 'abc')
from histogram.hdf import load, dump
dump(h, %r, '/', 'c')
""" % outh5
        script = tempfile.mktemp()
        open(script, 'w').write(code)
        cmd = 'python %s' % script
        import os
        
        if os.system(cmd):
            raise RuntimeError, "%s failed" % cmd
        
        from histogram.hdf import load
        h = load(outh5, 'abc')

        os.remove(outh5)
        os.remove(script)
        return        
    

    def test_rename_sliced_histogram(self):
        "Histogram: rename sliced histogram"
        import tempfile
        outh5 = tempfile.mktemp()
        code = """
from histogram import histogram, arange
h = histogram(
  'h', 
  [('x', arange(10), 'meter'),
   ('y', arange(15), 'meter'),
  ]
  )
h1 = h[(2,5), ()].sum('x')
h1.setAttribute('name', 'abc')
from histogram.hdf import load, dump
dump(h1, %r, '/', 'c')
""" % outh5
        script = tempfile.mktemp()
        open(script, 'w').write(code)
        cmd = 'python %s' % script
        import os
        
        if os.system(cmd):
            raise RuntimeError, "%s failed" % cmd
        
        from histogram.hdf import load
        try:
            h = load(outh5, 'abc')
        except:
            raise RuntimeError, "failed to load histogram from %s" %(
                outh5,)

        os.remove(outh5)
        os.remove(script)
        return        
    

    def test_rename_sliced_histogram_using_rename_method(self):
        "Histogram: rename()"
        import tempfile
        outh5 = tempfile.mktemp()
        code = """
from histogram import histogram, arange
h = histogram(
  'h', 
  [('x', arange(10), 'meter'),
   ('y', arange(15), 'meter'),
  ]
  )
h1 = h[(2,5), ()].sum('x')
h1.rename('abc')
from histogram.hdf import load, dump
dump(h1, %r, '/', 'c')
""" % outh5
        script = tempfile.mktemp()
        open(script, 'w').write(code)
        cmd = 'python %s' % script
        import os
        
        if os.system(cmd):
            raise RuntimeError, "%s failed" % cmd
        
        from histogram.hdf import load
        try:
            h = load(outh5, 'abc')
        except:
            raise RuntimeError, "failed to load histogram from %s" %(
                outh5,)

        os.remove(outh5)
        os.remove(script)
        return        
    

    pass # end of Histogram_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(Histogram_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id$"

# End of file 
