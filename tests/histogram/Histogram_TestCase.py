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



def createHistogram(noerror = False):
    from histogram import createContinuousAxis, arange, createDiscreteAxis
    #create axis E
    axisE = createContinuousAxis( 'E', 'meter', arange(0.5, 3.5, 1.0) )
    
    #create axis "tubeId"
    axisTubeId = createDiscreteAxis( "tubeId", [1, 3, 99], 'int')
    
    #create histogram
    from histogram import createDataset
    from ndarray.StdVectorNdArray import NdArray
    dataStorage = NdArray( 'double', range(9) ); dataStorage.setShape( (3,3) )
    errorsStorage = NdArray( 'double', range(9) ); errorsStorage.setShape( (3,3) )
    
    data = createDataset('data', storage = dataStorage )
    if noerror: errors = None
    else: errors  = createDataset('errors', storage = errorsStorage )
    from histogram.Histogram import Histogram
    histogram = Histogram( name = 'I(E, TubeId)', data = data, errors = errors,
                           axes = [axisE, axisTubeId])
    return histogram
    


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
        self.assertVectorEqual(slice5.shape(), (2,3) )
        
        slice6 = histogram[(None,1.5), ()]
        self.assertVectorEqual(slice5.shape(), (2,3) )

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
        self.assertVectorEqual( h[0.5, 3], (2,9) )

        h = self._histogram.copy()
        h2 = self._histogram2
        h *= h2
        self.assertVectorEqual( h[1.5,1], (9,108) )
        return
    
    
    def test__idiv__(self):
        "histogram: h/=b"
        h = self._histogram.copy()
        h /= (2,1)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (0.5,9./16) )

        h = self._histogram.copy()
        h /= (2,0)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (0.5,1./4) )

        h = self._histogram.copy()
        h2 = self._histogram2
        h /= h2
        self.assertVectorAlmostEqual( h[1.5,1], (1,4.0/3) )

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
        return


    def test__add__(self):
        "histogram: h+b"
        h = self._histogram + (1,0)
        self.assertVectorEqual( h[0.5, 1], (1,0) )

        h = self._histogram + self._histogram2
        self.assertVectorEqual( h[1.5,1], (6,6) )
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
        h = self._histogram * (2,1)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (2,9) )

        h = self._histogram * self._histogram2
        self.assertVectorEqual( h[1.5,1], (9,108) )
        return
    
    
    def test__div__(self):
        "histogram: h/b"
        h = self._histogram / (2,1)
        self.assertVectorEqual( h[0.5, 1], (0,0) )
        self.assertVectorEqual( h[0.5, 3], (0.5,9./16) )

        h = (2,1) / self._histogram 
        self.assertVectorEqual( h[0.5, 3], (2,9.) )

        h = self._histogram / self._histogram2
        self.assertVectorAlmostEqual( h[1.5,1], (1,4./3) )
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
        self.assertEqual( len(shape), 1 )
        self.assertEqual( shape[0], 3 )
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
