#!/usr/bin/env python
# Jiao Lin Copyright (c) 2005 All rights reserved


__doc__ = """

NAME:
  hdf5typeUtils
  
PURPOSE:
  find out the native c++ type that corresponds to the given hdf5 data type

DESCRIPTION:
  hdf5 has its own data type system. When read and write a hdf5 file,
  we need to find a way to represent those data types in the native
  format specific to the current platform.

  There will be infinite number of data types if composite data types are
  taken into account. We cannot map each of them into a native type.
  Therefore only common data types are supported for now. This is actually
  good enough because most scientific data are floats, integers, or,
  seldomly, strings.

RELATED:

HISTORY:
  many methods in here were extracted, combined, reshaped from VectorReader,
  VectorWriter, and hdf5fs modules

TODOs:
  + consider remove the dependency on array_kluge
  + consider not using type codes, but more meaningful symbols. strings might be good.
"""


import journal
debug = journal.debug("hdf5typeUtils")


from hdf5fs.typeUtils import getNativeTypeName, typeCodeFromName

#----------------------------------------------------------------------
#utility functions

def nativeTypeCode_from_h5Type( h5type ):
    """retrieve an appropriate native type name from given hdf5 type.
    """
    name = nativeTypeName_from_h5Type( h5type )
    return typeCodeFromName[ name ]

    
def nativeTypeName_from_h5Type( h5type ):
    """retrieve an appropriate native type name from given hdf5 type.
    """
    typeinfo = h5type.info()

    resolvableTypes = ['float', 'integer', 'string']
    if typeinfo['class'] in resolvableTypes:
        typeName = nativeTypeName_from_h5TypeInfo( typeinfo )
    else:
        msg = "Not implemented for hdf5 type class %s" % \
              typeinfo['class']
        raise NotImplementedError, msg
    return typeName



def makeNativeH5Type( original_h5type):
    """create a "native" hdf5 type from given hdf5 type
    This method is useful when reading data from a hdf5 file.
    A hdf5 file may be written in a machine different from what you are
    using right now. In this case, the data were written in a different
    format and your current computer won't be able to understand unless
    proper conversions are done. To achieve this, we would like to use
    hdf5's built-in capability to do the conversion. Suppose we know
    the original hdf5 type in the file, we should create a correspondent
    data type in the current machine for proper reading out.
    """
    typeObj = original_h5type
    debug.log( "original type is %s" % typeObj.info() )
    typeName = nativeTypeName_from_h5Type( typeObj )
    debug.log( "typeName is %s" % typeName )
    from hdf5fs.h5type import H5type
    newType = H5type( typeName )

    debug.log( "original type is %s, new type is %s " % (typeObj.info(), newType.info()) )

    return newType



def nativeTypeName_from_h5TypeInfo( h5typeinfo ):
    """retrieve an appropriate native type name from given hdf5 type info.
    """
    from hdf5fs.typeUtils import getNativeTypeName
    return getNativeTypeName( h5typeinfo )


def nativeTypeCode_from_h5TypeInfo(h5typeinfo):
    """retrieve type code from give H5 type info"""
    name = nativeTypeName_from_h5TypeInfo(h5typeinfo)
    return typeCodeFromName[name]


def checkH5Type( h5type ):
    # work arounds for mysterious behavior from hdf5fs.
    # perhaps needed for h4toh5'd files?

    fileType = h5type

    info = fileType.info()

    debug.log("fileType.info() = %s" % info)

    if info['class'] == 'float' and info['size']==32:
        import hdf5fs.h5type as h5type
        fileType = h5type.H5type( "float")
        debug.log('Changed filetype to H5type( "float")')
    elif info['class'] == 'integer' and info['size']==32 and info['signed']==0:
        import hdf5fs.h5type as h5type
        fileType = h5type.H5type( "unsigned int")
        debug.log('Changed filetype to H5type( "unsigned int")')

    return fileType
    

def getH5Type( h5dataset ):
    "retrieve hdf5 data type of given hdf5 dataset"
    filetype = h5dataset.getType()
    return checkH5Type( filetype )
