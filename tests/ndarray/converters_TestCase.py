#!/usr/bin/env python


skip = True

import unittest

from ndarray.converters import *

class converters_TestCase(unittest.TestCase):

    def testStdVectorNdArray2NumpyNdArray(self):
        "ndarray.converters: StdVectorNdArray2NumpyNdArray"
        from ndarray.StdVectorNdArray import NdArray
        v = [1,2,3] 
        a = NdArray( 'int', v )
        n = a.as_( "NumpyNdArray" )
        self.assertEqual( n.size(), 3 )
        l = n.asList()
        for a, b in zip( l, v ):
            self.assertEqual( a, b )
            continue
        self.assertEqual( n.__module__, "ndarray.NumpyNdArray" )
        
        v = range(12)
        a = NdArray( 'int', v )
        a.setShape( (3,4) )
        n = a.as_( "NumpyNdArray" )
        self.assertEqual( n.size(), 12 )
        self.assertEqual( n.shape(), (3,4) )
        
        l = n.asNumarray().copy()
        l.shape = -1,
        for a, b in zip( l, v ):
            self.assertEqual( a, b )
            continue
        self.assertEqual( n.__module__, "ndarray.NumpyNdArray" )
        
        return
    
    def testNumpyNdArray2StdVectorNdArray(self):
        "ndarray.converters: NumpyNdArray2StdVectorNdArray"
        from ndarray.NumpyNdArray import NdArray
        v = [1,2,3] 
        a = NdArray( 'int', v )
        n = a.as_( "StdVectorNdArray" )
        self.assertEqual( n.size(), 3 )
        l = n.asList()
        for a, b in zip( l, v ):
            self.assertEqual( a, b )
            continue
        self.assertEqual( n.__module__, "ndarray.StdVectorNdArray" )

        v = range(12)
        a = NdArray( 'int', v )
        a.setShape( (3,4) )
        n = a.as_( "StdVectorNdArray" )
        self.assertEqual( n.size(), 12 )
        self.assertEqual( n.shape(), (3,4) )
        
        l = n.asNumarray().copy()
        l.shape = -1,
        for a, b in zip( l, v ):
            self.assertEqual( a, b )
            continue
        self.assertEqual( n.__module__, "ndarray.StdVectorNdArray" )
        
        return
    
    pass # end of converters_TestCase


def pysuite():
    suite = unittest.makeSuite( converters_TestCase )
    return unittest.TestSuite( [suite] )


def main():
    import journal
    tests = pysuite()
    unittest.TextTestRunner(verbosity=2).run(tests)
    return


if __name__ == '__main__': main()
    
