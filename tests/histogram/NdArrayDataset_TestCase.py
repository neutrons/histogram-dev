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


from pyre.units.length import meter


import unittest
from unittestX import TestCase

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
        v = ds2.storage().asNumarray() * ds2.unit() / meter
        self.assertVectorAlmostEqual( v, [-0,-1,-2] )
        return
        

    def test__add__(self):
        "Dataset: operator 'a+b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds2 = ds + 1*meter
        v = ds2.storage().asNumarray() * ds2.unit() / meter
        self.assertVectorAlmostEqual( v, [2,3,4] ) 

        #ds2 = 1*meter + ds
        #self.assert_( ds2.storage().compare( NdArray('double', [2,3,4] ) ) )
        
        ds3 = ds + Dataset( unit = "meter", storage = NdArray('double', [2,3,4] ) )
        v = ds3.storage().asNumarray() * ds3.unit() / meter
        self.assertVectorAlmostEqual( v, [3,5,7] )

        self.assertRaises( NotImplementedError , ds.__add__, "a" )
        return


    def test__mul__(self):
        "Dataset: operator 'a*b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds2 = ds * 2
        v = ds2.storage().asNumarray() * ds2.unit() / meter
        self.assertVectorAlmostEqual( v, [2,4,6] ) 
        
        ds2 = 2 * ds 
        v = ds2.storage().asNumarray() * ds2.unit() / meter
        self.assertVectorAlmostEqual( v, [2,4,6] ) 
        
        ds2 = ds * ds 
        v = ds2.storage().asNumarray() * ds2.unit() / meter/meter
        self.assertVectorAlmostEqual( v, [1,4,9] ) 
        return


    def test__sub__(self):
        "Dataset: operator 'a-b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds2 = ds - 2 * meter
        v = ds2.storage().asNumarray() * ds2.unit() / meter
        self.assertVectorAlmostEqual( v, [-1,0,1] ) 

        ds2 = ds - ds
        v = ds2.storage().asNumarray() * ds2.unit() / meter
        self.assertVectorAlmostEqual( v, [0,0,0] ) 
        
        return


    def test__div__(self):
        "Dataset: operator 'a/b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds2 = ds / 2
        v = ds2.storage().asNumarray() * ds2.unit() / meter
        self.assertVectorAlmostEqual( v, [0.5,1,1.5] ) 
        
        ds2 = 1 / ds
        v = ds2.storage().asNumarray() * ds2.unit() / meter
        self.assertVectorAlmostEqual( v, [1,1./2,1./3] ) 
        return


    def test__iadd__(self):
        "Dataset: operator 'a+=b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds += 1 * meter
        v = ds.storage().asNumarray() * ds.unit() / meter
        self.assertVectorAlmostEqual( v, [2,3,4] ) 

        ds += ds
        v = ds.storage().asNumarray() * ds.unit() / meter
        self.assertVectorAlmostEqual( v, [4,6,8] ) 

        self.assertRaises( NotImplementedError , ds.__iadd__, "a" )

        ds = self.Dataset(name = 'intensity', unit = '-1',
                          shape = [3], storage = NdArray( 'double', [1,2,3] )
                          )
        ds += 1
        self.assertAlmostEqual( ds[0], 0 )
                          
        return


    def test__isub__(self):
        "Dataset: operator 'a-=b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds -= 1 * meter
        v = ds.storage().asNumarray() * ds.unit() / meter
        self.assertVectorAlmostEqual( v, [0,1,2] ) 

        ds -= ds
        v = ds.storage().asNumarray() * ds.unit() / meter
        self.assertVectorAlmostEqual( v, [0,0,0] ) 

        ds = self.Dataset(name = 'intensity', unit = '-1',
                          shape = [3], storage = NdArray( 'double', [1,2,3] )
                          )
        ds -= 1
        self.assertAlmostEqual( ds[0], -2 )

        self.assertRaises( NotImplementedError , ds.__isub__, "a" )
        return


    def test__imul__(self):
        "Dataset: operator 'a*=b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds *= 2 
        v = ds.storage().asNumarray() * ds.unit() / meter
        self.assertVectorAlmostEqual( v, [2,4,6] ) 

        ds *= ds
        v = ds.storage().asNumarray() * ds.unit() / meter/meter
        self.assertVectorAlmostEqual( v, [4,16,36] ) 
        
        self.assertRaises( NotImplementedError , ds.__imul__, "a" )

        ds1 = self.Dataset(
            'time', unit = 'second',
            shape = [3], storage = NdArray( 'double', [1,2,3] ),
            )
        ds *= ds1
        return


    def test__imul__2(self):
        'Dataset: a[?]*=b'
        a = self.Dataset(name = 'a', unit = 'meter', shape = [5],
                         storage = NdArray('double', range(5) )
                         )
        a[1:3] *= 2
        
        try:
            a[1:3] *= 2 * meter
            raise "Should raise ValueError"
        except ValueError:
            pass
        return


    def test__idiv__(self):
        "Dataset: operator 'a/=b'"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds /= 2
        v = ds.storage().asNumarray() * ds.unit() / meter
        self.assertVectorAlmostEqual( v, [0.5,1,1.5] ) 

        ds /= ds
        v = ds.storage().asNumarray() * ds.unit() 
        self.assertVectorAlmostEqual( v, [1,1,1] ) 

        self.assertRaises( NotImplementedError , ds.__idiv__, "a" )
        return


    def test__idiv__2(self):
        'Dataset: a[?]*=b'
        a = self.Dataset(name = 'a', unit = 'meter', shape = [5],
                         storage = NdArray('double', range(5) )
                         )
        a[1:3] /= 2
        
        try:
            a[1:3] /= 2 * meter
            raise "Should raise ValueError"
        except ValueError:
            pass
        return


    def testReverse(self):
        "Dataset: ds -> 1./ds"
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3], storage = NdArray( 'double', [1,2,3] ) )
        ds.reverse()
        v = ds.storage().asNumarray() * ds.unit() * meter
        self.assertVectorAlmostEqual( v, [1,1./2,1./3] )

        return


    def test__getitem__(self):
        "Dataset: operator 'a[3:5], a[3]'"
        #1D dataset
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [12], storage = NdArray( 'double', range(12) ) )
        #slicing
        self.assert_( ds[3:5].storage().compare( NdArray('double', [3,4] ) ) )
        #indexing
        self.assertAlmostEqual( ds[3]/meter, 3 )

        #2D dataset
        stor = NdArray( 'double', range(12) ); stor.setShape( (3,4) )
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3,4], storage = stor)
        #slicing
        subarr = ds[1:2, 1:2].storage()
        expected = NdArray('double', [5] ) ; expected.setShape( (1,1) )
        self.assert_( subarr.compare( expected ) )
        #indexing
        self.assertAlmostEqual( ds[1,1]/meter, 5 )
        return


    def test__setitem__(self):
        "Dataset: operator 'a[3]=4'"
        #1D dataset
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [12], storage = NdArray( 'double', range(12) ) )
        #set slice
        from numpy import array
        ds[3:5] = array([1,2])*meter
        self.assert_( ds[3:5].storage().compare( NdArray('double', [1,2] ) ) )
        #set item
        ds[10] = 11*meter
        self.assertAlmostEqual( ds[10]/meter, 11 )
        
        #2D dataset
        stor = NdArray( 'double', range(12) ); stor.setShape( (3,4) )
        ds = self.Dataset(name = "distance", unit = "meter",
                          attributes = { },
                          shape = [3,4], storage = stor)
        #slicing
        ds[1:2, 1:2] = array([[999]])*meter
        subarr = ds[1:2, 1:2].storage()
        expected = NdArray('double', [999] ) ; expected.setShape( (1,1) )
        self.assert_( subarr.compare( expected ) )
        #indexing
        self.assertAlmostEqual( ds[1,1]/meter, 999 )
        ds[1,1] = 333 * meter
        self.assertAlmostEqual( ds[1,1]/meter, 333 )

        #set slice with datasets
        ds1v = NdArray( 'double', range(12) ); ds1v.setShape( (3,4) )
        ds1 = self.Dataset(
            name = "distance", unit = "meter", shape = [3,4], storage = ds1v )
        ds2v = NdArray( 'double', range(4) ); ds2v.setShape( (2,2) )
        ds2 = self.Dataset(
            name = "distance", unit = "meter", shape = [2,2], storage = ds2v )
        ds1[1:3, 1:3] = ds2

        #set slice with one number
        ds1v = NdArray( 'double', range(12) ); ds1v.setShape( (3,4) )
        ds1 = self.Dataset(
            name = "distance", unit = "meter", shape = [3,4], storage = ds1v )
        ds1[1:3,1:3] = 1*meter
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

        self.assertAlmostEqual( ds.sum()/meter, 15. )
        
        ds1 = ds.sum(0)
        expected = NdArray( 'double', [3,5,7] )
        self.assert_( ds1.storage().compare( expected ) )
        return


    def testChangeUnit(self):
        'Dataset: changeUnit'
        storage = NdArray( 'double', range(3) )
        ds = self.Dataset(name = "distance", unit = "meter", storage = storage )
        ds.changeUnit( 'mm' )
        self.assertVectorAlmostEqual( ds.storage().asNumarray(), [0, 1000, 2000] )
        return


    def testSqrt(self):
        'Dataset: sqrt'
        storage = NdArray( 'double', range(3) )
        ds = self.Dataset(name = "distance", unit = "meter", storage = storage )
        ds.sqrt()
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
