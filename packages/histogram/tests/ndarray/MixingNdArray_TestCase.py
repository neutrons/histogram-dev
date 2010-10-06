#!/usr/bin/env python


import unittest

from ndarray.NumpyNdArray import NdArray as NumpyNdArray
from ndarray.StdVectorNdArray import NdArray as StdVectorNdArray

class MixingNdArray_TestCase(unittest.TestCase):

    def testStdVectorNdArray_dividedby_NumpyNdArray(self):
        "StdVectorNdArray/NumpyNdArray"
        a = StdVectorNdArray( 'float', range(1,13,1) )
        a.setShape( (3,4) )
        
        b = NumpyNdArray( 'float', range(1,13,1) )
        b.setShape( (3,4) )

        c = a/b

        shape = c.shape()
        self.assertEqual( shape, (3,4) )

        carr = c.asNumarray().copy()
        carr.shape = -1,
        for i in carr: self.assertAlmostEqual( i, 1. )
        return
        
    
    pass # end of MixingNdArray_TestCase


def pysuite():
    suite = unittest.makeSuite( MixingNdArray_TestCase )
    return unittest.TestSuite( [suite] )


def main():
    import journal
    tests = pysuite()
    unittest.TextTestRunner(verbosity=2).run(tests)
    return


if __name__ == '__main__': main()
    
