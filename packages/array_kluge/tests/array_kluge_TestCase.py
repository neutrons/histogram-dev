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
test utility class array_kluge
'''

import unittest

import journal
journal.debug('array_kluge').activate()

from array_kluge import *


typecode = 6
typename = 'double'
wrongtypename = 'char'
length = 10


typecodes = [
    5,
    6,
    24,
    25,
    ]


class array_kluge_TestCase(unittest.TestCase):


    def testlist_ptr(self):
        """array_kluge: python list <-> pointer to c array"""
        typeCodes = typecodes + [21] #21 is unsigned char
        origList = range( length )
        for typecode in typeCodes: self._testlist_ptr(origList, typecode)

        # char is special
        origList = ['a', 'b', 'c']
        cptr = pylist2vptr( origList, 4 )
        l = vptr2pylist( cptr, 3, 4 )
        self.assertEqual( list( l[0] ), origList )
        return
    

    def teststring_charptr(self):
        """array_kluge: python string <--> char pointer"""
        s = "abc"

        ptr1 = string2charPtr( s )
        s1 = charPtr2string( ptr1 )
        self.assertEqual( s, s1 )
        
        ptr2 = string2charPtrWD( s )
        s2 = charPtr2string( ptr2 )
        self.assertEqual( s, s2 )
        return
            
     
    def teststdvector_ptr(self):
        """array_kluge: pointer to c array -> pointer std::vector"""
        origList = range( length )
        for typecode in typecodes:
            self._teststdvector_ptr(origList, typecode)
            self._teststdvector_ptr_WD(origList, typecode)
            continue
        return


    def testnumarray_ptr(self):
        """array_kluge: pointer to c array -> numeric array"""
        origList = range( length )
        for typecode in typecodes: self._testnumarray_ptr(origList, typecode)
        return


    def _testlist_ptr(self, origList, typecode ):
        vptr = pylist2vptr ( origList, typecode )
        length = len( origList )
        l = vptr2pylist ( vptr, length, typecode )
        for a, b in zip(l, origList): self.assertAlmostEqual( a,b )
        return
        

    def _teststdvector_ptr(self, origList, typecode):
        # test vPtr2stdvectorPtr
        length = len(origList)

        vptr = pylist2vptr ( origList, typecode )
        vecPtr = vPtr2stdvectorPtr( vptr, length, typecode )
        #currently we have to use stdVector to test it
        try:
            import stdVector
        except ImportError:
            print "Warning: stdVector package is not available, cannot do full test of vPtr2stdvectorPtr"
            return
        
        from stdVector.VectorProxy import VectorProxy
        proxy = VectorProxy( typecode, vecPtr )
        l = proxy.asList()
        for a, b in zip(l, origList): self.assertAlmostEqual( a,b )
        return


    def _teststdvector_ptr_WD(self, origList, typecode):
        # test vPtr2stdvectorPtrWD
        length = len(origList)

        vptr = pylist2vptr ( range(length), typecode )
        vecPtr = vPtr2stdvectorPtrWD( vptr, length, typecode )
        #currently we have to use stdVector to test it
        try:
            import stdVector
        except ImportError:
            print "Warning: stdVector package is not available, cannot do full test of vPtr2stdvectorPtr"
            return
        
        from stdVector.VectorProxy import VectorProxy
        proxy = VectorProxy( typecode, vecPtr )
        l = proxy.asList()
        for a, b in zip(l, origList): self.assertAlmostEqual( a,b )
        return


    def _testnumarray_ptr(self, origList, typecode):
        #array_kluge: pointer to c array -> numeric array
        vptr = pylist2vptr ( origList, typecode )
        typename = gettypename( typecode )
        length = len(origList )
        arr = vPtr2numarray( vptr, length, typecode, typename)
        for a, b in zip(arr, origList): self.assertAlmostEqual( a,b )
        
        arr = vPtr2numarray( vptr, length, typecode, typename, copy = 0)
        for a, b in zip(arr, origList): self.assertAlmostEqual( a,b )

        #make sure type mismatch got caught
        self.assertRaises( AssertionError , vPtr2numarray, vptr, length, typecode, wrongtypename )
        return


    pass #end of array_kluge_TestCase
            
    
def pysuite():
    suite1 = unittest.makeSuite(array_kluge_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()


# version
__id__ = "$Id: array_kluge_TestCase.py 130 2005-07-07 15:24:11Z linjiao $"

# End of file 
