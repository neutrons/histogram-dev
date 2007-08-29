#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

def StdVectorNdArray2NumpyNdArray( src ):
    # the following import cannot be put into module level
    # otherwise recursion will happen
    from ndarray.NumpyNdArray import arrayFromNumpyArray as ndarrayFromNumpyArray

    na = src.asNumarray()
    rt = ndarrayFromNumpyArray( na )
    return rt



# version
__id__ = "$Id$"

# End of file 
