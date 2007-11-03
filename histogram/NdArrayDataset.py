#!/usr/bin/env python
# Jiao Lin Copyright (c) 2006 All rights reserved

from DatasetBase import DatasetBase
import journal
debug = journal.debug("NdArrayDataset")


class Dataset( DatasetBase):
    """datasets that use stdVectors"""

    def __init__( self, name='', unit='1', attributes = {},
                  shape = [], storage = None, isslice = False):
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
        #whether this dataset is a slice of another dataset
        self._isslice = isslice
        
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


    def name( self):
        """name() -> name of this axis"""
        return self._attributeCont.getAttribute('name')


    def isunitless(self):
        from _units import isunitless
        return isunitless( self.unit() )


    def isslice(self):
        "is this dataset a slice of another dataset?"
        return self._isslice


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


    def changeUnit(self, unit):
        '''change unit. update data array accordingly'''

        unit = tounit( unit )
        myunit = self.unit()
        
        try: unit + myunit
        except: ValueError, "cannot set dataset of unit %s to new unit %s" % (
            myunit, unit)

        ratio = myunit/unit
        self._storage *= ratio
        self._setunit( unit )
        return
    

    def attribute( self, name):
        """attribute( attrName) -> attrValue"""
        return self._attributeCont.getAttribute( name)


    def listAttributes( self):
        """listAttributes() -> [list of attr names]"""
        return self._attributeCont.listAttributes()


    def setAttribute( self, name, value):
        """setAttribute( name, value) -> None"""
        self._attributeCont.setAttribute( name, value)
        return


    def copy(self):
        return self._copy( )


    def sum(self, axis = None):
        if axis is None : return self.storage().sum() * self.unit()
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
        if isNumber(other) and self.isunitless():
            stor += other/self.unit()
        elif isDimensional(other):
            try: self.unit() + other
            except: raise ValueError, "unit mismatch: %s and %s" % (
                self.unit(), other)
            stor += other/self.unit()
        elif isUnitCompatibleDataset(self, other):
            stor += other.storage() * (other.unit()/self.unit())
        elif isDataset(other):
            raise ValueError, "Incompatible datasets: %s, %s" (
                self, other)
        else:
            raise NotImplementedError , "%s + %s" % (
                self.__class__.__name__, other.__class__.__name__, 
                )
        return self


    def __isub__(self, other):
        if other is None: return self
        stor = self.storage()
        if isNumber(other) and self.isunitless(): stor -= other/self.unit()
        elif isDimensional(other): stor -= other/self.unit()
        elif isUnitCompatibleDataset(self, other):
            stor -= other.storage() * (other.unit()/self.unit())
        else:
            raise NotImplementedError , "%s - %s" % (
                self.__class__.__name__, other.__class__.__name__)
        return self


    def __imul__(self, other):
        stor = self.storage()
        if isNumber(other) and (other == 0 or other == 0.0):
            stor *= 0
            return self
        if self.isslice() and isNumber(other):
            #if this dataset is a slice, and other is a number
            #we just need to work on the array. But we cannot
            #change unit.
            stor *= other
            return self
        
        if self.isslice():
            # if this dataset is actually a slice of another dataset, then
            # we cannot change unit. otherwise this dataset will
            # have different unit than the original dataset
            raise ValueError , \
                  "%s*%s. This dataset is a slice, we cannot change unit" % (
                self, other)
        
        if isNumber(other) or isDimensional(other):
            self.setAttribute( 'unit', self.unit()*other )
        elif isCompatibleDataset(self, other):
            stor *= other.storage()
            self.setAttribute( 'unit', self.unit()*other.unit() )
        else:
            raise NotImplementedError , "%s * %s" % (
                self.__class__.__name__, other.__class__.__name__)
        return self
    

    def __idiv__(self, other):
        stor = self.storage()
        
        if self.isslice() and isNumber(other):
            #if this dataset is a slice, and other is a number
            #we just need to work on the array. But we cannot
            #change unit.
            stor /= other
            return self
        
        if self.isslice():
            # if this dataset is actually a slice of another dataset, then
            # we cannot change unit. otherwise this dataset will
            # have different unit than the original dataset
            raise ValueError , \
                  "%s/%s. This dataset is a slice, we cannot change unit" % (
                self, other)
        
        if isNumber(other) or isDimensional(other):
            self.setAttribute('unit', 1.* self.unit()/other)
        elif isCompatibleDataset(self, other):
            stor /= other.storage()
            self.setAttribute( 'unit', 1.* self.unit()/other.unit() )
        else:
            raise NotImplementedError , "%s * %s" % (
                self.__class__.__name__, other.__class__.__name__)
        return self


    def square(self):
        self.storage().square()
        self.setAttribute( 'unit', self.unit()**2 )
        return
    

    def sqrt(self):
        self.storage().sqrt()
        from math import sqrt
        self.setAttribute( 'unit', self.unit()**(1./2) )
        return


    def reverse(self):
        self.storage().reverse()
        self.setAttribute( 'unit', 1./self.unit() )
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
        
        if isinstance(s, int): return self._storage[s] * self.unit()
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
        
        if slicing: return self._copy( self._storage[s], slicing = True )
        return self._storage[s] * self.unit()
        

    def __setitem__(self, s, rhs):
        if isDataset( rhs ):
            rhs = rhs._storage * (rhs.unit()/self.unit())
        else:
            try: rhs /= self.unit()
            except Exception , msg :
                raise ValueError, \
                      '__setitem__: the rhs must be either dataset or numpy data array'\
                      ' with unit. rhs = %s.\n'\
                      '%s: %s' %  (rhs, msg.__class__.__name__, msg)
            pass
        try:
            self._storage[s] = rhs
        except Exception, err:
            raise ValueError , "rhs = %s. %s:%s" % (rhs, err.__class__, err)
        return rhs 


    def __str__(self):
        return '''Dataset %s(unit=%s): %s''' % (
            self.name(), self.unit(), self.storage().asNumarray() )
    

    def _copy(self, storage = None, slicing = False):
        keys = self.listAttributes()
        attrs = {}
        for key in keys: attrs[key] = self.attribute( key )

        #create a copy of my storage if necessary
        if storage is None: storage = self.storage().copy()
        
        copy = self.__class__(
            name=self.name(), unit=self.unit(), attributes = attrs,
            shape = [], storage = storage, isslice = slicing)
        return copy


    def _setunit(self, unit):
        self.setAttribute( 'unit', unit )
        return
    

    pass # end of Class Dataset


from _units import *


def isDataset(ds):
    return isinstance(ds, DatasetBase)


def isCompatibleDataset(a,b):
    if not isinstance(a, DatasetBase) or not isinstance(b, DatasetBase):
        debug.log("either %s or %s is not a dataset" % (a.__class__.__name__,
                                                        b.__class__.__name__,) )
        return False
    
    if a.shape() != b.shape():
        debug.log("imcompatible shape: %s, %s" % (a.shape(), b.shape()) )
        return False

    return True


def isUnitCompatibleDataset(a,b):
    if not isCompatibleDataset(a,b): return False
    try: a.unit() + b.unit()
    except:
        debug.log("imcompatible units: %s, %s" % (a.unit(), b.unit()) )
        return False
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
