# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                Jiao Lin
#                        California Institute of Technology
#                        (C) 2006 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = ndarray
PACKAGE = ndarray

# directory structure

BUILD_DIRS = \
	converters \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse


release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
    __init__.py         \
    AbstractNdArray.py\
    NumpyNdArray.py      \
    StdVectorNdArray.py      \


export:: export-python-modules 


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 118 2006-04-17 06:41:49Z jiao $

# End of file
