#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from _journal import *

from AbstractDataSource import AbstractDataSource



class H5DataSource(AbstractDataSource):


    def __init__(self, dimensions, path, h5selector, h5reader):
        self._dimensions = dimensions
        self._path = path
        self._selector = h5selector
        self._reader = h5reader
        return


    def fetch(self, starts, shape):
        '''fetch data
        
        starts: indexes where the data slice start
        shape: shape of the data slice
        '''
        kwds = {"userStarts": starts,
                "userSizes" : shape,
                }
        storage = self._readArrayFromPath(  **kwds )
        from ndarray.StdVectorNdArray import arrayFromVector
        ret = arrayFromVector(storage)
        ret.setShape( shape )
        return ret
    

    def _readArrayFromPath( self, **kwds ):
        global _readArrayFromPath
        storage = _readArrayFromPath(
            self._path, self._selector, self._reader, **kwds )
        return storage
    

    pass # end of H5DataSource



def _readArrayFromPath( path, h5selector, h5reader, **kwds ):
    h5selector.select( path)
    debug.log("read from path: %s" % (path,) )
    vector = h5reader.read( h5selector, **kwds )
    return vector


# version
__id__ = "$Id$"

# End of file 
