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
PACKAGE = pickle/object_hierarchy


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
	Branch.py \
	Builtin.py \
	Construction.py \
	Dict.py \
	Global.py \
	Instance.py \
	Leaf.py \
	Link.py \
	List.py \
	ObjectHierarchyFromObject.py \
	ObjectFromObjectHierarchy.py \
	Printer.py \
	Tuple.py \
	__init__.py \
	testobject.py \


export:: export-package-python-modules

# version
# $Id: Make.mm 118 2007-03-14 18:26:58Z linjiao $

# End of file
