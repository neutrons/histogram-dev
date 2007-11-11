# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = histogram
PACKAGE = hdf/nodes


# directory structure

BUILD_DIRS = \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AbstractDataSource.py \
	AbstractNode.py \
	Axis.py \
	Grid.py \
	H5DataSource.py \
	Histogram.py \
	__init__.py \
	_journal.py \
	NdArray.py \
	PhysicalValueNdArray.py \


export:: export-package-python-modules 


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 1302 2007-10-01 12:34:50Z linjiao $

# End of file
