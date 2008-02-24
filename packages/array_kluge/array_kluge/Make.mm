# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        (C) 1998-2003 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = array_kluge
PACKAGE = array_kluge

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
    __init__.py \
    create_type_lookup_table.py \
    numarray__vptr.py \
    pylist__vptr.py \
    string__charPtr.py \
    stdvector__vptr.py \
    test_platform.py \


export:: export-python-modules #export-docs


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 48 2007-05-15 17:18:00Z linjiao $

# End of file
