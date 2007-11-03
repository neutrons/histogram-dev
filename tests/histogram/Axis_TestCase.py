#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


#import histogramTest_Axis as oldtest
#from histogramTest_Axis import log, target, aspects, utilities


from histogram import calcBinBoundaries, ndArray, axis
from histogram.Axis import Axis


import unittest

from unittestX import TestCase
class Axis_TestCase(TestCase):

    def testContinuousMapper(self):
        "Axis: ContinuousMapper"
        from histogram.EvenlyContinuousAxisMapper import EvenlyContinuousAxisMapper as AxisMapper
        min = 0.5; delta = 1.0; nBins = 3
        binBoundaries = calcBinBoundaries( min, delta, nBins )
        storage = ndArray( "double", binBoundaries )
        
        self.assertVectorEqual( binBoundaries, [0.0, 1.0, 2.0, 3.0] )
        axisMapper = AxisMapper( binBoundaries = binBoundaries )
        
        axis = Axis(
            'x', unit='1', attributes = {},
            length = nBins, storage = storage, mapper = axisMapper)
            
        self.assertEqual( axis.cellIndexFromValue( 0.5 ), 0 )
        self.assertEqual( axis.cellIndexFromValue( 0. ), 0 )
        self.assertEqual( axis.cellIndexFromValue( 1. ), 1 )
        self.assertEqual( axis.cellIndexFromValue( 2. ), 2 )
        self.assertEqual( axis.cellIndexFromValue( 0.9 ), 0 )
        self.assertEqual( axis.cellIndexFromValue( 1.9 ), 1 )
        self.assertRaises( IndexError, axis.cellIndexFromValue, -0.5 )
        self.assertRaises( IndexError, axis.cellIndexFromValue, 3.5 )
        self.assertVectorEqual( axis.binCenters(), [0.5,1.5,2.5] )
        return
        
    
    def testDiscreteMapper(self):
        "Axis: DiscreteMapper"
        from histogram.DiscreteAxisMapper import DiscreteAxisMapper as AxisMapper
        items = [10,100,2999]
        itemDict = {}
        for i, value in enumerate(items): itemDict[value] = i
        axisMapper = AxisMapper( itemDict )

        from histogram import ndArray
        storage = ndArray( 'int', items + [-1] ) # -1 is a patch
        from histogram.Axis import Axis
        axis = Axis( name = "category", storage = storage, mapper = axisMapper )
        
        self.assertEqual( axis.cellIndexFromValue( 10 ), 0 )
        self.assertEqual( axis.cellIndexFromValue( 100 ), 1 )
        self.assertEqual( axis.cellIndexFromValue( 2999 ), 2 )
        self.assertRaises( IndexError, axis.cellIndexFromValue, -1 )
        self.assertVectorEqual( axis.binCenters(), [10,100,2999])
        return

    
    def testSlicing(self):
        "Axis[3:5]"
        from histogram import createContinuousAxis, arange
        axis = createContinuousAxis(
            "distance", "meter", arange( 1.0, 2.0, 0.1 ) )
        
        from histogram.SlicingInfo import SlicingInfo
        
        new = axis[ SlicingInfo( (1.1, 1.5) ) ]
        self.assertVectorAlmostEqual(
            new.storage().asList(),
            [1.05, 1.15, 1.25, 1.35, 1.45, 1.55] )

        new = axis[ SlicingInfo( (1.0, 1.9) ) ]
        self.assertVectorAlmostEqual(
            new.storage().asList(),
            axis.storage().asList() )

        
        self.assertRaises( IndexError,  axis.__getitem__, SlicingInfo( (1.0, 2.0) )  )
        return


    def test_rsub(self):
        "Axis: number-axis"
        taxis= axis('t', range(10) )
        t1axis = 10-taxis
        self.assert_( isinstance( t1axis, Axis) )
        return


    def test_changeUnit(self):
        'Axis: changeUnit'
        taxis= axis('t', range(3), unit='second' )
        taxis.changeUnit( 'millisecond' )
        self.assertVectorAlmostEqual( taxis.binBoundaries().asNumarray(),
                                      [-500, 500, 1500, 2500] )
        self.assertVectorAlmostEqual( taxis.binCenters(), 
                                      [0, 1000, 2000] )
        return
    
    
    #def test_0(self): self._run_oldtest(0)
    #def test_1(self): self._run_oldtest(1)
    #def test_2(self): self._run_oldtest(2)
    #def test_3(self): self._run_oldtest(3)

    def _run_oldtest(self, i):
        aspect = aspects[i]
        utilities.preReport( log, target, aspect )
        run = eval( "oldtest.test_%s" % i )
        passed = run()
        utilities.postReport( log, target, aspect, passed)
        self.assertEqual( passed, True )
        return

    pass # end of Axis_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(Axis_TestCase)
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
