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


from AbstractNode import AbstractNode as base

class NdArray(base):

    def __init__(self, name, shape, datasource):
        base.__init__(self,name)
        self.shape = shape
        self._datasource = datasource
        return


    def fetch(self, slices = None):
        '''fetch nD data array from data source.
        slices: list of slices for each dimension or None
        if slices is None: the whole array will be fetched.
        '''
        if slices is None:
            slices = [
                slice(0, size) for size in self.shape ]
            pass
        return self._fetch1( slices )


    def _fetch1(self, slices):
        '''fetch nD data array from data source.
        slices: list of slices for each dimension
        '''
        for s in slices:
            assert s.step in [1, None], \
                   "step=%s slicing is not yet supported. slices = %s" % (
                s.step, slices)
            continue
        starts = [s.start for s in slices]
        shape = [ s.stop-s.start for s in slices ]
        return self._fetch2( starts, shape )


    def _fetch2(self, starts=None, shape=None):
        '''fetch nD data array from data source.
        starts: indexes where the data slice start
        shape: shape of the data slice
        '''
        if starts is None: starts = [0 for i in self.shape ]
        if shape is None: shape = self.shape
        return self._datasource.fetch( starts, shape )


    pass # end of NdArray


# version
__id__ = "$Id$"

# End of file 
