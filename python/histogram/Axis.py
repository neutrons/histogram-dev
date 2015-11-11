#!/usr/bin/env python


## \package histogram.Axis
##
## This package contains the class "Axis".
##


from NdArrayDataset import Dataset


class Axis(Dataset):
    
    """Axis

    Public interface:
      axis.unit(): return the unit
      axis.binCenters(): return bin centers as an array
      axis.binBoundariesAsList(): return bin boundaries as a list.
      axis.name(): return the name
      axis.changeUnit(newunit): change the unit of this axis to new unit.
        The new unit must be compatible with the old unit.
      numerical operators: + - * /
    """

    def __init__( self, name='', unit='1', attributes = None,
                  length = 0, storage = None, mapper = None, centers = None):
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
        if isinstance( mapper, DiscreteAxisMapper ): 
            self._isDiscrete = True
        else: 
            self._isDiscrete = False

        self._cache = {}

        if centers is not None: centers = N.array(centers)
        self._centers = centers
        self.__isslice = False
        return


    def copy(self): return self._copy()


    def cellIndexFromValue( self, value ):
        try:             
            return self._mapper(value)
        except IndexError, msg:
            newmsg = "%s\nAxis %s: cannot find index of %s. (axis bin centers=%s)" % (
                msg, self.name(), value, self.binCenters())
            raise IndexError , newmsg
        

    def binCenters( self):
        """list of bin centers"""
        keyword = 'binCenters'
        if keyword not in self._cache:
            self._cache[keyword] = self._getBinCenters()
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
        #save old unit
        oldunit = self.unit()

        #use parent class's changeUnit, but please remember:
        if self.__isslice:
            msg =  "This axis %r is a slice. cannot change unit." % self.name()
            raise RuntimeError, msg
        
        #there is a problem with mapper!!!!
        Dataset.changeUnit(self, unit)
        
        #mapper need to be reset
        self._mapper = createMapper( self._storage.asList(), self._mapper.__class__ )
        #!!! need to remove cache!!!
        self._cache = {}
        #also need to update centers if necssary
        if self._centers is not None:
            self._centers = N.array(self._centers) * (oldunit/self.unit())
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
        ret = self._copy( storage = stor )
        ret.__isslice = True
        return ret

    def __neg__(self): return self._overloaded_operator('__neg__')
    def __add__(self, other): return self._overloaded_operator('__add__', other)
    __radd__ = __add__
    def __sub__(self, other): return self._overloaded_operator('__sub__', other)
    def __rsub__(self, other):return self._overloaded_operator('__rsub__', other)
    def __mul__(self, other): return self._overloaded_operator('__mul__', other)
    __rmul__ = __mul__
    def __div__(self, other): return self._overloaded_operator('__div__', other)
    def __rdiv__(self, other):return self._overloaded_operator('__rdiv__', other)
    def __iadd__(self, other):return self._overloaded_operator('__iadd__', other)
    def __isub__(self, other):return self._overloaded_operator('__isub__', other)
    def __imul__(self, other):return self._overloaded_operator('__imul__', other)
    def __idiv__(self, other):return self._overloaded_operator('__idiv__', other)

    def slicingInfo2IndexSlice(self, slicingInfo):
        """slicingInfo2Range(slicingInfo) --> slice instance
        note: slicing is inclusive
        """
        unit = self.unit()

        start, end = slicingInfo.start, slicingInfo.end

        # if axis has dimensional unit, convert start and end to pure numbers if necessary
        if isDimensional(unit):
            if isDimensional(start): start = start/unit
            if isDimensional(end): end = end/unit

        # if axis' unit is a number. it is assumed that the start and end are always given with unit
        # so we need to divide them by the unit
        if isNumber(unit) and unit not in [1, 1.0]:
            if isNumber(start): start = start/unit
            if isNumber(end): end = end/unit

        # if start and end are special objects, convert to numbers as well
        bc = self.binCenters()
        if start == front: start = bc[0]
        if end == back: end = bc[-1]

        # at this point, start and end should all be numbers
        if not isNumber(start) or not isNumber(end):
            raise RuntimeError, "At this point, start and end should all be numbers: start=%s(%s), end=%s(%s)" % (start, type(start), end, type(end))
        #slice. +1 is due to the difference of bin boundaries and bin centers
        s = ( self.cellIndexFromValue( start ),
              self.cellIndexFromValue( end ) + 1 )
        return s

        
    def _overloaded_operator(self, operator, *args, **kwds):
        ret = getattr(super(Axis, self), operator)(*args, **kwds)
        # the parent class, NdArrayDataset, does not know about axis mapper
        # we need to reinitialize the axis mapper.
        # the way this is done here is to call method changeUnit, which
        # recalculates the axis mapper
        ret.changeUnit(ret.unit())
        return ret
    

    def _copy(self, storage = None, mapper = None):
        keys = self.listAttributes()
        attrs = {}
        for key in keys: attrs[key] = self.attribute( key )

        #create a copy of my storage if necessary
        if storage is None: storage = self.storage().copy()

        if mapper is None:
            try:
                mapper = createMapper( storage.asList(), self._mapper.__class__ )
            except NotImplementedError, err:
                raise 'Unable to create copy of axis %s: %s, %s' % (
                    self, err.__class__.__name__, err )
                

        copy = self.__class__(
            name=self.name(), unit=self.unit(), attributes = attrs,
            length = 0, storage = storage, mapper = mapper)
        return copy
    

    def _getBinCenters(self):
        if self._centers is not None:
            return self._centers
        bblist = self._storage.asNumarray()
        if self.isDiscrete():
            return bblist[:-1]
        else:
            numcells = len(bblist) - 1
            return (bblist[1:]+bblist[:-1])/2.
        raise RuntimeError, "should not reach here"


    pass # end of Axis



class LogicError(Exception): pass


from _units import isDimensional
def isNumber(candidate):
    return isFloat(candidate) or isInteger(candidate)

import types
def isFloat(candidate):
    return isinstance(candidate, types.FloatType)
def isInteger(candidate):
    return isinstance(candidate, types.IntType) or isinstance(candidate, N.int32)


import numpy as N


from AxisMapperCreater import creater
createMapper = creater.create
del creater
        
from SlicingInfo import front, back
        
from SlicingInfo import SlicingInfo
def isSlicingInfo( s ):
    return isinstance(s, SlicingInfo)


from DiscreteAxisMapper import DiscreteAxisMapper
        

# version
__id__ = "$Id$"

# End of file
