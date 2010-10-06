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


def t():
    v = vector( 6, range(10000) )
    a = v.asNumarray()
    b = v.asNumarray()
    del v
    return a,b

class asNumarray_TestCase(unittest.TestCase):

    def test(self):
        a,b = t()
        v1 = vector( 6, range(1000,0,-1) )
        
        a[0] = 3
        print a,b
        return

    def test2(self):
        v1 = vector( 6, range(12) )
        shape = 3,4
        a = v1.asNumarray( shape )
        s = a.shape
        self.assertEqual( tuple(s), tuple(shape) )

    pass #end of asNumarray_TestCase
            
    
def pysuite():
    suite1 = unittest.makeSuite(asNumarray_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()


# version
__id__ = "$Id: asNumarray_TestCase.py 130 2005-07-07 15:24:11Z linjiao $"

# End of file 
