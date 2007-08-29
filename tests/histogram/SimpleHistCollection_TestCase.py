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


from histogram.SimpleHistCollection import SimpleHistCollection


import unittest


from unittestX import TestCase
class SimpleHistCollection_TestCase(TestCase):

    def testCtor(self):
        """ ctor
        """
        hist = 1
        hists = SimpleHistCollection( hist )
        return


    def testCall(self):
        """ __call__
        """
        hist = 1
        hists = SimpleHistCollection( hist )
        #default call
        self.assertEqual( hists(), hist )
        
        #call with a detector instance
        class Detector: pass
        self.assertEqual( hists( Detector() ), hist )
        return
        
        
        
    pass # end of SimpleHistCollection_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(SimpleHistCollection_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
##     journal.debug('instrument').activate()
##     journal.debug('instrument.elements').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id$"

# End of file 
