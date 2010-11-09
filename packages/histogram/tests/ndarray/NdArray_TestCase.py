#!/usr/bin/env python

# NdArray has a fixed interface
# this test test the subclasses of NdArray and see if all methods
# defined in the interface are satisfied.
# In the NdArray module, we have a unittest TestCase base class to test
# all those methods.
# Here we just need to override the setUp method of the TestCase
# base class so that different subclass can be tested.


import unittest

from ndarray.AbstractNdArray import NdArray_TestCase
def createTestCase(klass):
    class TC(NdArray_TestCase):
        def setUp(self):
            self.NdArray = klass
            #print klass
            return
        pass # end of TC
    return TC


def pysuite():
    from ndarray.NumpyNdArray import NdArray as NumpyNA

    klasses = [ NumpyNA ] 
    testcases = [ createTestCase( klass ) for klass in klasses ]
    suites = [ unittest.makeSuite( tc ) for tc in testcases ]
    return unittest.TestSuite( suites )


def main():
    import journal
##     journal.debug('instrument').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    
