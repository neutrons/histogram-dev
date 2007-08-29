#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal
debug = journal.debug("histogram.DatasetBase")


msg = "class %s must override %s"

class DatasetBase( object):
    """dataset interface"""

    def attribute( self, name):
        """attribute( attrName) -> attrValue"""
        raise NotImplemented, msg % (self.__class__.__name__, 'attribute')


    def listAttributes( self):
        """listAttributes() -> [list of attr names]"""
        raise NotImplemented, msg % (self.__class__.__name__, 'listAttributes')
        return list( self._attributes.keys())


    def name( self):
        """name() -> name of this axis"""
        raise NotImplemented, msg % (self.__class__.__name__, 'name')


    def setAttribute( self, name, value):
        """setAttribute( name, value) -> None"""
        raise NotImplemented, msg % (self.__class__.__name__, 'setAttribute')


    def shape( self):
        """shape() -> [list of dimensions]"""
        raise NotImplemented, msg % (self.__class__.__name__, 'shape')


    def storage( self):
        """storage() -> storage object"""
        raise NotImplemented, msg % (self.__class__.__name__, 'storage')
    

    def typecode( self):
        """typecode() -> type code"""
        raise NotImplemented, msg % (self.__class__.__name__, 'typecode')


    def typecodeAsC( self):
        """typecodeAsC() -> code
        get type code as C type ('float', 'double', 'int', 'unsigned')"""
        raise NotImplemented, msg % (self.__class__.__name__, 'typecodeAsC')


    def typecodeAsNA( self):
        """typecodeAsNA() -> code
        typecode translated to numpy type ('Float32', 'Float64', 'Int32',
        'UInt32)"""
        raise NotImplemented, msg % (self.__class__.__name__, 'typecodeAsNA')


    def typecodeAsStdVector( self):
        """typecodeAsStdVector() -> code
        Typecode translated to stdVector types.  Type codes are:
            5.....float (single precision)
            6.....double (double precision)
            24....int (typically 32 bit)
            25....unsigned int (typically 32 bit)"""
        raise NotImplemented, msg % (self.__class__.__name__, 'typecodeAsNA')


    def unit( self):
        """unit() -> unit for this axis"""
        raise NotImplemented, msg % (self.__class__.__name__, 'unit')
    

    def __init__( self, name='', unit='', attributeCont = None,
                  shape = [], storage = None):
        """DatasetBase( name='', unit='', attributes={},
        shape = [], storage = None)
        Inputs:
            name: name (string)
            unit: unit (string)
            attributes: additional user defined attributes (dictionary)
            shape: axes dimensions ([integers > 0])
            storage: raw array/vector etc.
        Output:
            new DatasetBase object
        Exceptions: None
        Notes: None"""

        self._attributeCont = attributeCont

        self.setAttribute( 'name', name)
        self.setAttribute( 'unit', unit)

        self._shape = shape
        self._storage = storage
        
        if storage is not None:
            self._typecode = storage.datatype()
        else:
            self._typecode = ''
        
        return


    _typesSV2C = { 5:'float',
                   6:'double',
                   24:'int',
                   25:'unsigned'
                   }

    _typesC2SV = { 'float'   :5,
                   'double'  :6,
                   'int'     :24,
                   'unsigned':25
                   }

    _typesSV2NA = { 5: 'Float32',
                    6: 'Float64',
                    24:'Int32',
                    25:'UInt32'
                    }

    _typesNA2SV = { 'Float32':5,
                    'Float64':6,
                    'Int32'  :24,
                    'UInt32' :25
                    }


# version
__id__ = "$Id$"

# End of file
