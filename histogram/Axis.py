#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved
# Jiao Lin Copyright (c) 2006 All rights reserved


## \package histogram.Axis
##
## This package contains the class "Axis".
##


from NdArrayDataset import Dataset


class Axis( Dataset):
    
    """Dataset that models a HistogramAxis"""

    def __init__( self, name='', unit='1', attributes = {},
                  length = 0, storage = None, mapper = None):
        """HistogramAxis( attributes={},
        length=0, storage=None)
        Inputs:
            attributes: additional user defined attributes 
            length: number of cells in axis (int >= 1)
            storage: raw array/vector etc. holding BIN BOUNDARIES
        Output:
            new HistogramAxis object
        Exceptions: None
        Notes: Meant to hold histogram bin boundaries
        """
        
        if length == 0 and storage is not None: length = storage.size()-1
        elif length !=0 and storage is not None:
            if int(length) !=  int(storage.size()-1) :
                raise "incompatible inputs: length = %s, storage.shape = %s" % (
                    length, storage.shape())
            pass
        shape = [length+1]

        Dataset.__init__( self, name, unit, attributes, shape, storage)

        self._mapper = mapper
        if isinstance( mapper, DiscreteAxisMapper ): self._isDiscrete = True
        else: self._isDiscrete = False

        self._cache = {}
        return


    def copy(self): return self._copy()


    def cellIndexFromValue( self, value ):
        try: return self._mapper(value)
        except IndexError, msg:
            newmsg = "%s\nAxis %s: cannot find index of %s. (axis bin centers=%s)" % (
                msg, self.name(), value, self.binCenters())
            raise IndexError , newmsg
        

    def binCenters( self):
        """list of bin centers"""
        keyword = 'binCenters'
        if keyword not in self._cache:
            bblist = self._storage.asList()
            if self.isDiscrete():
                self._cache[keyword] = bblist[:-1]
            else:
                numcells = len(bblist) - 1
                self._cache[keyword] = [
                    (bblist[i+1] + bblist[i])/2.0 for i in range(numcells)]
                pass
            pass
        return self._cache[ keyword ]


    def binBoundaries( self):
        """binBoundaries() -> bin boundaries storage object"""
        return self._storage


    def binBoundariesAsList( self):
        """binBoundariesAsList() -> list of bin boundaries"""
        keyword = 'binBoundaries'
        if keyword not in self._cache:
            self._cache[keyword] = self._storage.asList()            
        return self._cache[keyword]


    def changeUnit(self, unit):
        Dataset.changeUnit(self, unit)
        #!!! need to remove cache!!!
        self._cache = {}
        return
    

    def isDiscrete(self): return self._isDiscrete


    def __len__( self):
        """len(axis) -> number of bins"""
        return self.size()


    def size( self):
        """size() -> number of bins"""
        return int(self._storage.size() - 1)


    def __getitem__(self, s):
        '''axis[ SlicingInfo( a,b ) ] --> a slice of the original axis
        axis[ index ] --> binboundaries[index] * unit
        '''
        if not isSlicingInfo(s): return Dataset.__getitem__(self, s)
        slicingInfo = s
        indexStart, indexEnd = self.slicingInfo2IndexSlice( slicingInfo )
        s = slice(indexStart, indexEnd + 1 ) #inclusive
        stor = self.storage()[s]
        return self._copy( storage = stor )


    def slicingInfo2IndexSlice(self, slicingInfo):
        """slicingInfo2Range(slicingInfo) --> slice instance
        note: slicing is inclusive
        """
        start, end = slicingInfo.start, slicingInfo.end
        bc = self.binCenters()
        if start == front: start = bc[0]
        if end == back: end = bc[-1]
        #slice. +1 is due to the difference of bin boundaries and bin centers
        s = ( self.cellIndexFromValue( start ),
              self.cellIndexFromValue( end ) + 1 )
        return s

        
    def _copy(self, storage = None, mapper = None):
        keys = self.listAttributes()
        attrs = {}
        for key in keys: attrs[key] = self.attribute( key )

        #create a copy of my storage if necessary
        if storage is None: storage = self.storage().copy()

        if mapper is None:
            from AxisMapperCreater import creater
            mapper = creater.create( storage.asList(), self._mapper.__class__ )

        copy = self.__class__(
            name=self.name(), unit=self.unit(), attributes = attrs,
            length = 0, storage = storage, mapper = mapper)
        return copy
    

        
from SlicingInfo import front, back
        
from SlicingInfo import SlicingInfo
def isSlicingInfo( s ):
    return isinstance(s, SlicingInfo)


from DiscreteAxisMapper import DiscreteAxisMapper
        

# version
__id__ = "$Id$"

# End of file
