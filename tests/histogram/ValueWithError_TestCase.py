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



import unittestX as unittest


from histogram.ValueWithError import ValueWithError

class ValueWithError_TestCase(unittest.TestCase):


    def assertVEqual( self, ve, t ):
        t1 = ve.asTuple()
        self.assertVectorAlmostEqual( t1, t )
        return


    def test__iadd__(self):
        "ValueWithError: h+=b"
        h = ValueWithError( 3., 4. )
        b = 3.
        
        h += b
        self.assertVEqual( h, (6, 4) )

        b = ValueWithError( 2., 2. )
        h += b
        self.assertVEqual( h, (8, 6) )

        l = ValueWithError( 2 )
        r = ValueWithError( 1, 3 )
        self.assertVEqual( l+r, (3,3) )
        return
    
    
    def test__isub__(self):
        "ValueWithError: h-=b"
        l = ValueWithError( 2 )
        r = ValueWithError( 1, 3 )
        l-=r
        self.assertVEqual( l, (1,3) )
        
        l = ValueWithError( 2, 2 )
        r = ValueWithError( 1, 1 )
        l-=r
        self.assertVEqual( l, (1,3) )
        
        l = ValueWithError( 2, 2 )
        r = ValueWithError( 1 )
        l-=r
        self.assertVEqual( l, (1,2) )
        
        return
    
    
    def test__imul__(self):
        "ValueWithError: h*=b"

        l = ValueWithError( 2 )
        r = ValueWithError( 1, 3 )
        l *= r
        self.assertVEqual( l, (2,12) )
        
        r = ValueWithError( 2 )
        l = ValueWithError( 1, 3 )
        l *= r
        self.assertVEqual( l, (2,12) )
        
        l = ValueWithError( 2 )
        r = ValueWithError( 1 )
        l *= r
        self.assertVEqual( l, (2,0) )
        
        l = ValueWithError( 2, 1 )
        r = ValueWithError( 1, 1 )
        l *= r
        self.assertVEqual( l, (2,9) )
        
        return
    
    
    def test__idiv__(self):
        "ValueWithError: h/=b"
        l = ValueWithError( 2 )
        r = ValueWithError( 1, 2 )
        l /= r
        self.assertVEqual( l, (2,8) )
        
        r = ValueWithError( 2 )
        l = ValueWithError( 1, 2 )
        l/= r
        self.assertVEqual( l, (1./2,1./2) )
        
        l = ValueWithError( 2 )
        r = ValueWithError( 1 )
        l/= r
        self.assertVEqual( l, (2,0) )
        
        l = ValueWithError( 2, 1 )
        r = ValueWithError( 1, 1 )
        l/= r
        self.assertVEqual( l, (2,9) )
        
        return


    def test__add__(self):
        "ValueWithError: h+b"
        l = ValueWithError( 2 )
        r = ValueWithError( 1, 3 )
        self.assertVEqual( l-r, (1,3) )
        
        l = ValueWithError( 2, 2 )
        r = ValueWithError( 1, 1 )
        self.assertVEqual( l-r, (1,3) )
        
        l = ValueWithError( 2, 2 )
        r = ValueWithError( 1 )
        self.assertVEqual( l-r, (1,2) )
        return
    
    
    def test__sub__(self):
        "ValueWithError: h-b"
        l = ValueWithError( 2 )
        r = ValueWithError( 1, 3 )
        self.assertVEqual( l-r, (1,3) )
        
        l = ValueWithError( 2, 2 )
        r = ValueWithError( 1, 1 )
        self.assertVEqual( l-r, (1,3) )
        
        l = ValueWithError( 2, 2 )
        r = ValueWithError( 1 )
        self.assertVEqual( l-r, (1,2) )
        return
    
    
    def test__mul__(self):
        "ValueWithError: h*b"
        l = ValueWithError( 2 )
        r = ValueWithError( 1, 3 )
        self.assertVEqual( l*r, (2,12) )
        
        r = ValueWithError( 2 )
        l = ValueWithError( 1, 3 )
        self.assertVEqual( l*r, (2,12) )
        
        l = ValueWithError( 2 )
        r = ValueWithError( 1 )
        self.assertVEqual( l*r, (2,0) )
        
        l = ValueWithError( 2, 1 )
        r = ValueWithError( 1, 1 )
        self.assertVEqual( l*r, (2,9) )
        
        return
    
    
    def test__div__(self):
        "ValueWithError: h/b"
        l = ValueWithError( 2 )
        r = ValueWithError( 1, 2 )
        self.assertVEqual( l/r, (2,8) )
        
        r = ValueWithError( 2 )
        l = ValueWithError( 1, 2 )
        self.assertVEqual( l/r, (1./2,1./2) )
        
        l = ValueWithError( 2 )
        r = ValueWithError( 1 )
        self.assertVEqual( l/r, (2,0) )
        
        l = ValueWithError( 2, 1 )
        r = ValueWithError( 1, 1 )
        self.assertVEqual( l/r, (2,9) )
        
        return

    pass # end of ValueWithError_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(ValueWithError_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id$"

# End of file 
