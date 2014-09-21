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

PROJECT = histogram/ndarray
PACKAGE = converters

#--------------------------------------------------------------------------
#

all: export

tidy:: 
	BLD_ACTION="tidy" $(MM) recurse

#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	__init__.py \
	NumpyNdArray2StdVectorNdArray.py \
	StdVectorNdArray2NumpyNdArray.py \
	utils.py \


include doxygen/default.def

export:: export-package-python-modules 



# version
# $Id$

# End of file
