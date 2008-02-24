#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from DatasetBase import DatasetBase
import journal
debug = journal.debug("histogram.Dataset")

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

        debug.log("storage = %s" % str(storage))

        DatasetBase.__init__( self, name, unit, attributeCont, shape, storage)

        debug.log("here")
        return


# version
__id__ = "$Id$"

# End of file
