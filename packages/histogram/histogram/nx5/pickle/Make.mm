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
PACKAGE = pickle


BUILD_DIRS = \
    object_hierarchy \

RECURSE_DIRS = $(BUILD_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

release: tidy
	svn release .

update: clean
	svn update .

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
	NXGraphFromObjectHierarchy.py \
	ObjectHierarchyFromNXGraph.py \
	Pickler.py \
	UnPickler.py \
	__init__.py \
	nexmlpath.py \
	storage.py \


export:: export-package-python-modules

# version
# $Id: Make.mm 118 2007-03-14 18:26:58Z linjiao $

# End of file
