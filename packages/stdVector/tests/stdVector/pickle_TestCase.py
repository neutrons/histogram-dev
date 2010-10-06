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

import pickle

typecode = 6
length = 10

v = vector( 6, range(10) )

class pickle_TestCase(unittest.TestCase):


    def test_dump(self):
        "stdVector: pickle.dump"
        pickle.dump( v, open( "tmp.pkl", 'w' ) )
        return


    def test_load(self):
        "stdVector: pickle.load"
        pickle.dump( v, open( "tmp.pkl", 'w' ) )
        v1 = pickle.load( open( "tmp.pkl" ) )
        assert v1.compare(v)
        return


    pass #end of pickle_TestCase
            
    
def pysuite():
    suite1 = unittest.makeSuite(pickle_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()


# version
__id__ = "$Id: pickle_TestCase.py 130 2005-07-07 15:24:11Z linjiao $"

# End of file 
