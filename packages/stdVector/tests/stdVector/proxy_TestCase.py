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


'''
test utility class VectorProxy
'''

import unittest

import journal
journal.debug('proxy').activate()

from array_kluge import pylist2vptr, vPtr2stdvectorPtr
from stdVector.VectorProxy import VectorProxy
from stdVector.stdVector import stdVector_ctor, stdVector_proxy
from stdVector import vector


typecode = 6
length = 10

class proxy_TestCase(unittest.TestCase):

    def testPython(self):
        """VectorProxy: python method"""
        #create pycobject of std::vector pointer
        a = pylist2vptr ( range(length), typecode )
        vecPtr = vPtr2stdvectorPtr( a, length, typecode )

        #create proxy
        vecProxy = VectorProxy( typecode, vecPtr )
        
        # test out
        l = vecProxy.asList ()
        for i,v in enumerate(l): self.assertAlmostEqual( i, v )

        #check reference count
        del vecPtr
        l = vecProxy.asList ()
        for i,v in enumerate(l): self.assertAlmostEqual( i, v )

        return
        
     
    def testBinding(self):
        """VectorProxy: binding"""
        #create pycobject of std::vector pointer
        a = pylist2vptr ( range(length), typecode )
        vecPtr  =vPtr2stdvectorPtr ( a, length, typecode)

        # create pycobject of VectorProxy pointer
        proxyPtr = stdVector_proxy (typecode, vecPtr)

        # create stdVector object of VectorProxy
        vecProxy = vector (typecode,None, handle=proxyPtr )

        # test out
        l = vecProxy.asList ()
        for i,v in enumerate(l): self.assertAlmostEqual( i, v )

        #make sure reference couting is correct
        #delete the proxy then the real pointer, and we should still be fine:
        del vecProxy
        del vecPtr
        #we still have the proxyPtr, which should keep a refernce to vecPtr
        #so although we delete the vecPtr, it still exists
        #so we can make a vector proxy out of the proxyPtr, and see if it
        #really works out
        vecProxy = vector (typecode,None, handle=proxyPtr )
        l = vecProxy.asList ()
        for i,v in enumerate(l): self.assertAlmostEqual( i, v )


        #test again
        #this time we delete the vector pointer first, and then the proxy pointer
        #then we see if vectorProxy still works
        vecPtr  = vPtr2stdvectorPtr ( a, length, typecode)
        proxyPtr = stdVector_proxy (typecode, vecPtr)
        vecProxy = vector (typecode,None, handle=proxyPtr )
        del vecPtr
        del proxyPtr
        #although we delete all underlying pointers, they are still referenced
        #by vecProxy, so we are fine
        l = vecProxy.asList ()
        for i,v in enumerate(l): self.assertAlmostEqual( i, v )
        return



    pass #end of proxy_TestCase
            
    
def pysuite():
    suite1 = unittest.makeSuite(proxy_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()


# version
__id__ = "$Id: proxy_TestCase.py 130 2005-07-07 15:24:11Z linjiao $"

# End of file 
