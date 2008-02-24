#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004


## \namespace stdVector::TemplateCObject
## 
## provides base class for classes wrapping c++ template classes
##
## It is a subclass of CObject, and superclass of classes wrapping
## c++ template classes, like StdVector.
##
## TemplateCObject keeps track of the template type, i.e., the
##  "T" of 
## "template <class T>". It can be returned by method TemplateCObject.templateType.


from CObject import CObject

class TemplateCObject( CObject):
    """Base class that minds a handle, classname, and a template type code
    for classes that wrap C++ template objects
    """

    def templateType( self):
        """Get the typecode of the template class for this object."""
        return self._templateType

    datatype = templateType


    def __init__( self, templateType = None, handle = None, klass = None):
        """TemplateCObject( templateType, handle, className) 
        """
        CObject.__init__( self, handle, klass)
        self._templateType = templateType
        return


    def _isCompatible( self, other):
        if self._templateType != other._templateType:
            msg = "template (data) types do not agree, this obj's type ="
            msg += str( self._templateType) + ", other's type = "
            msg += str( other._templateType)
            raise TypeError, msg
        return CObject._isCompatible( self, other)

# version
__id__ = "$Id: TemplateCObject.py 134 2006-10-09 15:21:57Z linjiao $"

# End of file
