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
from histogram import createDataset
from histogram.DatasetContainer import DatasetContainer


ds = createDataset( "ds", shape = (3,4) )
ds2 = createDataset( "ds2", shape = (3,4) )


class DatasetContainer_TestCase(TestCase):


    def testCtor(self):
        """ DatasetContainer: ctor """
        dc = DatasetContainer()
        return


    def testAddDataset(self):
        """ DatasetContainer: addDataset"""
        dc = DatasetContainer()
        dc.addDataset( "ds", 0, ds )
        return

    
    def testDeleteDataset(self):
        """ DatasetContainer: deleteDataset"""
        dc = DatasetContainer()
        dc.addDataset( "ds", 0, ds )
        dc.deleteDataset( 'ds', 0 )
        l = dc.listDatasets()
        self.assertEqual( len(l), 0 )
        return

    
    def testReplaceDataset(self):
        """ DatasetContainer: replaceDataset"""
        dc = DatasetContainer()
        dc.addDataset( "ds", 0, ds )
        dc.replaceDataset( "ds", ds2 )
        self.assert_( dc.datasetFromName( "ds" ) == ds2 )
        return

    
    def testDatasetFromName(self):
        """ DatasetContainer: datasetFromName"""
        dc = DatasetContainer()
        dc.addDataset( "ds", 0, ds )
        self.assert_( dc.datasetFromName( "ds" ) == ds )
        return

    
    def testDatasetFromId(self):
        """ DatasetContainer: datasetFromId"""
        dc = DatasetContainer()
        dc.addDataset( "ds", 0, ds )
        self.assert_( dc.datasetFromId( 0 ) == ds )
        return

    
    def testListDatasets(self):
        """ DatasetContainer: listDatasets"""
        dc = DatasetContainer()
        dc.addDataset( "ds", 0, ds )
        l = dc.listDatasets()
        self.assertEqual( len(l), 1 )
        item0 = l[0]
        id0, name0 = item0
        self.assertEqual( name0, "ds" )
        self.assertEqual( id0, 0 )
        return

    
    pass # end of Dataset_TestCase



def pysuite():
    suite1 = unittest.makeSuite(DatasetContainer_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
    #journal.debug('DatasetContainer').activate()
##     journal.debug('instrument').activate()
##     journal.debug('instrument.elements').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()




# version
__id__ = "$Id: DatasetContainer_TestCase.py 1209 2006-11-16 18:51:55Z linjiao $"

# End of file 
