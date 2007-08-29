#!/usr/bin/env python
# Jiao Lin Copyright (c) 2006 All rights reserved

from DatasetBase import DatasetBase
import journal
debug = journal.debug("NdArrayDataset")


class Dataset( DatasetBase):
    """datasets that use stdVectors"""

    def attribute( self, name):
        """attribute( attrName) -> attrValue"""
        return self._attributeCont.getAttribute( name)


    def listAttributes( self):
        """listAttributes() -> [list of attr names]"""
        return self._attributeCont.listAttributes()


    def name( self):
        """name() -> name of this axis"""
        return self._attributeCont.getAttribute('name')


    def setAttribute( self, name, value):
        """setAttribute( name, value) -> None"""
        self._attributeCont.setAttribute( name, value)
        return


    def shape( self):
        """shape() -> [list of dimensions]"""
        return list( self._shape)


    def setShape(self, newShape):
        self._storage.setShape( newShape )
        self._shape = newShape
        return


    def storage( self):
        """storage() -> storage object"""
        return self._storage
    

    def typecode( self):
        """typecode() -> type code
        Type codes are:
            5.....float (single precision)
            6.....double (double precision)
            24....int (typically 32 bit)
            25....unsigned int (typically 32 bit)"""
        return int( self._typecode)


    def typecodeAsC( self):
        """typecodeAsC() -> code
        get type code as C type ('float', 'double', 'int', 'unsigned' """
        return str( self._typesSV2C[self._typecode])


    def typecodeAsNA( self):
        """typecodeAsNA() -> code
        typecode translated to numpy type ('Float32', 'Float64', 'Int32',
        'UInt32)"""
        return str( self._typesSV2NA[ self._typecode])


    def typecodeAsStdVector( self):
        return int(self._typecode)


    def unit( self):
        """unit() -> unit for this axis"""
        return self._attributeCont.getAttribute('unit')
    

    def __init__( self, name='', unit='', attributes = {},
                  shape = [], storage = None):
        """DatasetBase( name='', unit='', attributes={},
        shape = [], storage = None)
        Inputs:
            name: name (string)
            unit: unit (string)
            attributes: additional user defined attributes (dictionary)
            shape: axes dimensions ([integers > 0])
            storage: raw array/vector etc. holding BIN BOUNDARIES
        Output:
            new DatasetBase object
        Exceptions: None
        Notes: None"""
        from DictAttributeCont import AttributeCont
        # copy user's attributes to avoid confusion
        attributeCont = AttributeCont( dict(attributes))

        #debug.log("storage = %s" % str(storage))
        
        if shape == [] and storage is not None: shape = storage.shape()
        if shape != [] and storage is not None:
            if list(storage.shape()) != list(shape):
                raise "Incompaitlbe inputs: shape = %s, storage.shape = %s" % (
                    shape, storage.shape())
            pass
        shape = list(shape)
        _checkShape(shape)

        #debug.log("shape = %s" % (storage.shape(),))

        DatasetBase.__init__( self, name, unit, attributeCont, shape, storage)
        return



    def copy(self):
        return self._copy( )


    def sum(self, axis = None):
        if axis is None : return self.storage().sum()
        name = "sum of %s along axis %s" % (self.name(), axis)
        unit = self.unit() #sum don't change unit

        #copy attributes
        keys = self.listAttributes()
        attrs = {}
        for key in keys: attrs[key] = self.attribute( key )

        #shape
        shape = list(self.shape())
        del shape[ axis ]

        #storage
        storage = self.storage().sum(axis)
        
        new = self.__class__(
            name=name, unit = unit, attributes = attrs, shape = shape, storage = storage)
        return new
    

     #operators
    def __neg__(self):
        return -1. * self


    def __add__(self, other):
        r = self.copy()
        r += other
        return r
    

    __radd__ = __add__


    def __sub__(self, other):
        r = self.copy()
        r -= other
        return r


    def __rsub__(self, other):
        r = self.copy()
        r *= -1
        r += other
        return r


    def __mul__(self, other):
        r = self.copy()
        r *= other
        return r


    __rmul__ = __mul__
    
            
    def __div__(self, other):
        return self * (1./other)
            

    def __rdiv__(self, other):
        if isNumber(other):
            r = self.copy()
            stor = r.storage()
            stor[:] = other/self.storage()
            return r
        raise NotImplementedError , "__rdiv__ is not defined for %s and %s" % (
            other.__class__.__name__, self.__class__.__name__, )



    def __iadd__(self, other):
        if other is None: return self
        stor = self.storage()
        if isNumber(other): stor += other
        elif isCompatibleDataset(self, other):
            stor += other.storage()
        else:
            raise NotImplementedError , "%s + %s" % (
                self.__class__.__name__, other.__class__.__name__)
        return self


    def __isub__(self, other):
        if other is None: return self
        stor = self.storage()
        if isNumber(other): stor -= other
        elif isCompatibleDataset(self, other):
            stor -= other.storage()
        else:
            raise NotImplementedError , "%s - %s" % (
                self.__class__.__name__, other.__class__.__name__)
        return self


    def __imul__(self, other):
        stor = self.storage()
        if isNumber(other): stor *= other
        elif isCompatibleDataset(self, other):
            stor *= other.storage()
        else:
            raise NotImplementedError , "%s * %s" % (
                self.__class__.__name__, other.__class__.__name__)
        return self
    

    def __idiv__(self, other):
        stor = self.storage()
        if isNumber(other): stor /= other
        elif isCompatibleDataset(self, other):
            stor /= other.storage()
        else:
            raise NotImplementedError , "%s * %s" % (
                self.__class__.__name__, other.__class__.__name__)
        return self


    #shoud we change the unit???
    def square(self): self.storage().square()


    def sqrt(self): self.storage().sqrt()


    def reverse(self):
        self.storage().reverse()
        return


    def transpose(self, *args):
        '''Returns a view of dataset with axes transposed.
        Axes should be give as integers.
        If no axes are given,
        or None is passed, switches the order of the axes. For a 2-d
        histogram, this is the usual matrix transpose. If axes are given,
        they describe how the axes are permuted.

        !!!How should meta data change?
        '''
        name = self.name()
        unit = self.unit()
        attrs = {}
        for n in self.listAttributes():
            attrs[n] = self.attribute( n )
            continue
        storage = self.storage().transpose()
        shape = storage.shape()
        return Dataset( name = name, unit = unit, attributes = attrs,
                        shape = shape, storage = storage )


    def __getitem__(self, s):
        if isinstance(s, list): s = tuple(s)
        
        if isinstance(s, int): return self._storage[s]
        elif isinstance(s, tuple):
            s = list(s)
            slicing = False
            for i in s:
                if not isinstance(i, int): slicing = True; break
                continue
        elif isinstance(s, slice):
            slicing = True
        else:
            raise IndexError , "Don't know how to do indexing by %s" % (s,)
        
        if slicing: return self._copy( self._storage[s] )
        return self._storage[s]
        

    def __setitem__(self, s, rhs):
        if isDataset( rhs ): rhs = rhs._storage
        self._storage[s] = rhs
        return rhs 


    def _copy(self, storage = None):
        keys = self.listAttributes()
        attrs = {}
        for key in keys: attrs[key] = self.attribute( key )

        #create a copy of my storage if necessary
        if storage is None: storage = self.storage().copy()
        
        copy = self.__class__(
            name=self.name(), unit=self.unit(), attributes = attrs,
            shape = [], storage = storage)
        return copy
    

    pass # end of Class Dataset



def isDataset(ds):
    return isinstance(ds, DatasetBase)


def isNumber(a):
    return isinstance(a, float) or isinstance(a, int )


def isCompatibleDataset(a,b):
    if not isinstance(a, DatasetBase) or not isinstance(b, DatasetBase):
        debug.log("either %s or %s is not a dataset" % (a.__class__.__name__,
                                                        b.__class__.__name__,) )
        return False
    
    if a.shape() != b.shape():
        debug.log("imcompatible shape: %s, %s" % (a.shape(), b.shape()) )
        return False
    
##     if a.unit() != b.unit():
##         debug.log("imcompatible unit: %s, %s" % (a.unit(), b.unit()) )
##         return False
    return True



def _checkShape(shape):
    for i in shape:
        assert isinstance(i, int) or isinstance(i, long), "wrong shape %s" % (
            shape,)
        continue
    return
        


# version
__id__ = "$Id: StdvectorDataset.py 581 2005-07-27 01:53:42Z tim $"

# End of file
