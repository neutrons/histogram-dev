# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               T. M. Kelley
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = stdVector
PACKAGE = stdVector

#--------------------------------------------------------------------------
#

all: export

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
    __init__.py         \
    CObject.py          \
    Slice.py            \
    StdVector.py        \
    StdVectorIterator.py\
    TemplateCObject.py  \
    VectorProxy.py \


export:: export-python-modules


include doxygen/default.def
docs: export-doxygen-docs

# version
# $Id: Make.mm 140 2007-05-15 22:06:44Z linjiao $

# End of file
