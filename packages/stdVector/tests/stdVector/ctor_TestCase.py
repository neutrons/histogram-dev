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


import unittest


from stdVector import vector

length = 10

class ctor_TestCase(unittest.TestCase):


    def test_asList(self):
        "stdVector.asList"
        l = range(10)
        builtinTypes = {
            'float': float,
            'double': float,
            'int': int,
            'unsigned': int,
            }
        for typename in ["float", "double", "int", "unsigned"]:
            v = vector( typename, l)
            t = builtinTypes[ typename ]
            for i,j in zip( v.asList(), l ):
                self.assertEqual( i, t( j ) )
                continue
            continue

        s = "hello"
        self.assertEqual( s, vector('char', s).asList() )
        return


    def test_asList_str(self):
        "stdVector.asList for strings with NULL characters"
        s = '\x00\x01'.decode( 'string-escape' )
        assert len(s) == 2
        self.assertEqual( s, vector('char', s).asList() )
        return        


    def test_datatype(self):
        "stdVector.__init__:  datatype"
        for typename in ["float", "double", "int", "unsigned"]:
            v = vector( typename, 10, 0)
            continue
        
        for typecode in [5,6, 24, 25]:
            v = vector( typecode, 10, 0)
            continue

        self.assertRaises( ValueError, vector,  'c', 10, 0 )
        self.assertRaises( ValueError, vector,  999, 10, 0 )
        return


    def test_nelements(self):
        "stdVector.__init__:  nelements"
        vector( 6, 10, 0 )
        vector( 5, 10L, 0 )
        return


    def test_initVal(self):
        "stdVector.__init__:  initVal"
        vector( 6, 10, 0 )
        self.assertRaises( TypeError, vector,  6, 10, 'a' )
        self.assertRaises( TypeError, vector,  6, 10, [0] )
        return


    def test_numlist(self):
        "stdVector.__init__:  numlist or string"
        vector(6, [1,2,3])
        vector("char", "hello")
        vector(4, "hello")
        self.assertRaises( TypeError, vector, 6, "hello" )
        self.assertRaises( TypeError, vector, 4, [1,2,3] )
        self.assertRaises( TypeError, vector, 'char', [1,2,3] )
        return


    def test_wrong_arg2(self):
        "stdVector.__init__:  arg2"
        self.assertRaises( ValueError, vector, 6, 3.3 )
        return

    pass #end of ctor_TestCase
            
    
def pysuite():
    suite1 = unittest.makeSuite(ctor_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()


# version
__id__ = "$Id: ctor_TestCase.py 130 2005-07-07 15:24:11Z linjiao $"

# End of file 
