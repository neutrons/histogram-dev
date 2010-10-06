# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               T. M. Kelley
#                        California Institute of Technology
#                        (C) 1998-2003  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = nx5
PACKAGE = file


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES =  \
    hdf5typeUtils.py     \
    vectorShapeUtils.py  \
    File.py              \
    File2.py             \
    FileFactory.py       \
    FileGraph.py         \
    QuasiSingleton.py    \
    QuasiSingleton2.py    \
    Reader.py            \
    Selector.py          \
    SimpleFileFactory.py \
    SimpleFileInitializer.py \
    VectorReader.py      \
    VectorWriter.py      \
    Writer.py            \
    XMLRep.py            \
    __init__.py


export:: export-package-python-modules

# version
# $Id: Make.mm 108 2005-10-28 00:21:07Z linjiao $

# End of file
