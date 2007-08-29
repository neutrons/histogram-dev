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


import unittest
from unittest import TestCase

from ndarray.NumpyNdArray import NdArray
from histogram.NdArrayDataset import Dataset

class NdArrayDataset_TestCase(TestCase):


    def setUp(self):
        self.Dataset = Dataset
        return
    

    def testCtor(self):
        """ Dataset: ctor """
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', range(3) ) )
        self.assert_( ds.storage().compare( NdArray( 'double', range(3) ) ) )
        return


    def test__neg__(self):
        "Dataset: operator '-a'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', range(3) ) )
        ds2 = -ds
        self.assert_( ds2.storage().compare( NdArray('double', [-0,-1,-2] ) ) )
        return
        

    def test__add__(self):
        "Dataset: operator 'a+b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds2 = ds + 1
        self.assert_( ds2.storage().compare( NdArray('double', [2,3,4] ) ) )

        ds2 = 1 + ds
        self.assert_( ds2.storage().compare( NdArray('double', [2,3,4] ) ) )
        
        ds3 = ds + Dataset( unit = "meter", storage = NdArray('double', [2,3,4] ) )
        self.assert_( ds3.storage().compare( NdArray('double', [3,5,7])) )

        self.assertRaises( NotImplementedError , ds.__add__, "a" )
        return


    def test__mul__(self):
        "Dataset: operator 'a*b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds2 = ds * 2
        self.assert_( ds2.storage().compare( NdArray('double', [2,4,6] ) ) )

        ds2 = 2 * ds 
        self.assert_( ds2.storage().compare( NdArray('double', [2,4,6] ) ) )
        
        ds2 = ds * ds 
        self.assert_( ds2.storage().compare( NdArray('double', [1,4,9] ) ) )
        
        return


    def test__sub__(self):
        "Dataset: operator 'a-b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds2 = ds - 2
        self.assert_( ds2.storage().compare( NdArray('double', [-1,0,1] ) ) )

        ds2 = ds - ds
        self.assert_( ds2.storage().compare( NdArray('double', [0,0,0] ) ) )
        
        return


    def test__div__(self):
        "Dataset: operator 'a/b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds2 = ds / 2
        self.assert_( ds2.storage().compare( NdArray('double', [0.5,1,1.5] ) ) )
        
        ds2 = 1 / ds
        self.assert_( ds2.storage().compare( NdArray('double', [1,1./2,1./3] ) ) )
        
        return


    def test__iadd__(self):
        "Dataset: operator 'a+=b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds += 1
        self.assert_( ds.storage().compare( NdArray('double', [2,3,4] ) ) )

        ds += ds
        self.assert_( ds.storage().compare( NdArray('double', [4,6,8] ) ) )

        self.assertRaises( NotImplementedError , ds.__iadd__, "a" )
        return


    def test__isub__(self):
        "Dataset: operator 'a-=b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds -= 1
        self.assert_( ds.storage().compare( NdArray('double', [0,1,2] ) ) )

        ds -= ds
        self.assert_( ds.storage().compare( NdArray('double', [0,0,0] ) ) )

        self.assertRaises( NotImplementedError , ds.__isub__, "a" )
        return


    def test__imul__(self):
        "Dataset: operator 'a*=b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds *= 2
        self.assert_( ds.storage().compare( NdArray('double', [2,4,6] ) ) )

        ds *= ds
        self.assert_( ds.storage().compare( NdArray('double', [4,16,36] ) ) )
        
        self.assertRaises( NotImplementedError , ds.__imul__, "a" )
        return


    def test__idiv__(self):
        "Dataset: operator 'a/=b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds /= 2
        self.assert_( ds.storage().compare( NdArray('double', [0.5,1,1.5] ) ) )

        ds /= ds
        self.assert_( ds.storage().compare( NdArray('double', [1,1,1] ) ) )

        self.assertRaises( NotImplementedError , ds.__idiv__, "a" )
        return


    def testReverse(self):
        "Dataset: ds -> 1./ds"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds.reverse()
        self.assert_( ds.storage().compare( NdArray('double', [1,1./2,1./3] ) ) )

        return


    def test__getitem__(self):
        "Dataset: operator 'a[3:5], a[3]'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [12], storage = NdArray( 'double', range(12) ) )

        self.assert_( ds[3:5].storage().compare( NdArray('double', [3,4] ) ) )
        self.assertAlmostEqual( ds[3], 3 )

        stor = NdArray( 'double', range(12) ); stor.setShape( (3,4) )
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3,4], storage = stor)

        subarr = ds[1:2, 1:2].storage()
        expected = NdArray('double', [5] ) ; expected.setShape( (1,1) )
        self.assert_( subarr.compare( expected ) )
        return


    def test__setitem__(self):
        "Dataset: operator 'a[3]=4'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [12], storage = NdArray( 'double', range(12) ) )

        ds[3:5] = [1,2]
        self.assert_( ds[3:5].storage().compare( NdArray('double', [1,2] ) ) )

        ds[10] = 11
        self.assertAlmostEqual( ds[10], 11 )
        return


    def testCopy(self):
        "Dataset: method 'copy'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [12], storage = NdArray( 'double', range(12) ) )

        ds.storage().compare( ds.copy().storage() )
        return


    def testSetShape(self):
        "Dataset: method 'setShape'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [12], storage = NdArray( 'double', range(12) ) )
        ds.setShape( (3,4) )
        self.assert_( ds._storage.shape() == (3,4) )
        return


    def testSum(self):
        "Dataset: method 'sum'"
        storage = NdArray( 'double', range(6) )
        storage.setShape( (2,3) )
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { }, shape = [2,3], storage = storage)

        self.assertAlmostEqual( ds.sum(), 15. )
        
        ds1 = ds.sum(0)
        expected = NdArray( 'double', [3,5,7] )
        self.assert_( ds1.storage().compare( expected ) )
        return
        
        
    pass # end of Dataset_TestCase



def pysuite():
    suite1 = unittest.makeSuite(NdArrayDataset_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
    #journal.debug('NdArrayDataset').activate()
##     journal.debug('instrument').activate()
##     journal.debug('instrument.elements').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()




# version
__id__ = "$Id: NdArrayDataset_TestCase.py 1209 2006-11-16 18:51:55Z linjiao $"

# End of file 
