#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004


## \namespace stdVector::CObject
##
## provides base class for classes wrapping c++ classes
##
## CObject class keeps track of the c++ class name and the handle
## to the underlying c++ object. It has two public methods:
##  - CObject.handle: PyCObject with a void pointer to the underlying c++ object
##  - CObject.type: c++ class name
##


class CObject( object):
    """Mix-in class that provides handle and type methods
    """

    def handle( self):
        """Get the PyCObject with a void pointer to type
        """
        return self._handle


    def type( self):
        """Get the name of the class/type this CObject wraps
        """
        return self._type


    def __init__( self, handle = None, klass = None):
        self._handle = handle
        self._type = klass
        return


    def _isCompatible( self, other):
        if self._type != other._type:
            msg = "C++ class types do not agree, this object's type ="
            msg += str( self._type) + ", other's type = "
            msg += str( other._type)
            raise TypeError, msg
        return

    
# version
__id__ = "$Id: CObject.py 134 2006-10-09 15:21:57Z linjiao $"

# End of file
