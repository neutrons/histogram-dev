#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \namespace stdVector::VectorProxy
## provides a method to convert a PyCObject of void pointer to
## a stl vector object to a StdVector.StdVector.
## The pointer wraps by StdVector.StdVector is a pointer to a
## VectorWrapper object which keeps a "magic number" that identifies
## the type of the wrapped pointer.
## In order to to create a StdVector.StdVector instance out of
## a raw stl vector pointer, we need to wraps that pointer and
## create a VectorWrapper object. This is done by method
## VectorProxy here.
##


from StdVector import StdVector as Vector

def VectorProxy( typecode, vectorPtr ):
    """
    VectorProxy( typecode, pyc_stdvecor ) ---> instance of stdVector.StdVector.StdVector
    inputs:
      typecode:    type code of the element of the given std::vector instance
      vectorPtr:   PyCObject of the pointer to the underlying c++ std::vector object
    outputs:
      an instance of stdVector.StdVector.StdVector

    Be very careful when using this method. If possible, simply use stdVector.vector
    to create vectors. This method cannot check the consistency between the std::vector
    and the typecode. Only use this when extremely necessary.
    """
    proxyPtr = _createProxyPointer( typecode, vectorPtr )
    proxy = Vector( typecode, None, handle = proxyPtr)
    return proxy



from stdVector import stdVector_proxy

def _createProxyPointer( typecode, vectorPtr ):
    """_createProxyPointer( typecode, pychandle_stdvector ) --> PyCObject of a VectorProxy pointer
    details:
      TK's stdVector python binding wraps a c++ std::vector instance inside a wrapper class.
      All TK's stdVector functions access std::vector instances through the wrapper.
      Thus, for a PyCObject of a raw std::vector pointer, we need to make a similar wrap. 
      The class VectorProxy does this job. This function return a pyc handle to a c++ instance
      of class VectorProxy. 
    inputs:
      typecode:   type code to identify element type
      vectorPtr:  PyCObject of the pointer to the underlying c++ std::vector object
    outputs:
      a pyc handle to a c++ instance of class VectorProxy
    """
    return stdVector_proxy( typecode, vectorPtr )


    
# version
__id__ = "$Id: proxy_TestCase.py 130 2005-07-07 15:24:11Z linjiao $"

# End of file 
