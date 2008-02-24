#!/usr/bin/env python
# Jiao Lin Copyright (c) 2005 All rights reserved


import journal
debug = journal.debug('ins.histogram.AxisMapperCreater')


from EvenlyContinuousAxisMapper import EvenlyContinuousAxisMapper
from DiscreteAxisMapper import DiscreteAxisMapper


class AxisMapperCreater:

    def create(self, binBoundaries = None, mapperClass = None):
        if binBoundaries is None: raise ValueError ,"AxisMapperCreater can only be called with valid bin boundaries"

        if mapperClass is None: return None
        
        elif mapperClass is DiscreteAxisMapper:
            
            m = {}
            for index, value in enumerate( list(binBoundaries) ):
                m[value] = index
                continue
            return mapperClass(m)
        
        elif mapperClass is EvenlyContinuousAxisMapper:

            minBB = binBoundaries[0]
            binSize = binBoundaries[1]-binBoundaries[0]
            nBB = len(binBoundaries)
            return mapperClass( minBinBoundaries=minBB, binSize=binSize, nBinBoundaries=nBB )

        else:

            raise NotImplementedError ,"creater for %s not implemented" % mapperClass

        raise

    pass # end of AxisMapperCreater


creater = AxisMapperCreater()

             
# version
__id__ = "$Id$"

# End of file
