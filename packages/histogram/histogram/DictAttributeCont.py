#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

from AttributeContBase import AttributeContBase

class AttributeCont( AttributeContBase):


    def getAttribute( self, name):
        """getAttribute( name) -> value"""
        try:
            attr = self._attributes[ name]
        except KeyError:
            msg = "no attribute named %s" % name
            raise KeyError, msg
        return attr
    

    def listAttributes( self):
        """listAttributes() -> [names of attributes]"""
        return list( self._attributes.keys())
    
    
    def setAttribute( self, name, value):
        """setAttribute( name, value) -> None"""
        self._attributes[name] = value
        return
    
    
    def __init__( self, attributes = None):
        if attributes is None: attributes = {}
        self._attributes = attributes
        return
    

# version
__id__ = "$Id$"

# End of file
