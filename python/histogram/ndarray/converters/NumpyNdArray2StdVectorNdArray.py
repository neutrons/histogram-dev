#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

def NumpyNdArray2StdVectorNdArray( src ):
    # this is a slow implementation, and should be improved
    # in the near future
    l = src.asNumarray().copy()
    l.shape = -1,
    l = list(l)
    from stdVector import vector
    from ndarray.NumpyNdArray import getAKTypecode
    v = vector( getAKTypecode( src.asNumarray() ), l )
    
    # the following import cannot be put into module level
    # otherwise recursion will happen
    from ndarray.StdVectorNdArray import arrayFromVector as ndarrayFromStdVectorArray
    rt = ndarrayFromStdVectorArray( v )
    rt.setShape( src.shape() )
    return rt



# version
__id__ = "$Id$"

# End of file 
