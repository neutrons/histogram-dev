# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = histogram
PACKAGE = applications/gui/tools

PROJ_TIDY += *.log
PROJ_CLEAN =

# directory structure

BUILD_DIRS = \

OTHER_DIRS = \
 
RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#
all: export
	BLD_ACTION="all" $(MM) recurse
 
distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse
#--------------------------------------------------------------------------
#

EXPORT_PYTHON_MODULES = \
	raw_data.py \
	PRL.py \
	Reduction.py \
	WebAppTools.py \
	__init__.py \



export:: export-package-python-modules 



# version
# $Id: Make.mm 925 2006-05-22 06:45:13Z jiao $

# End of file
