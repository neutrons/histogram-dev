# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               T. M. Kelley
#                        (C) 1998-2003 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = nx5
PACKAGE = nx5

BUILD_DIRS =  \
    file      \
    nexml     \
    pickle   \
    renderers \

RECURSE_DIRS = $(BUILD_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
    ConsoleDisambiguator.py \
    Disambiguator.py        \
    Exceptions.py           \
    NXpath.py               \
    NXUnambiguous.py        \
    Types.py                \
    Unambiguous.py          \
    __init__.py             \


export:: export-python-modules
	BLD_ACTION="export" $(MM) recurse


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 131 2007-05-15 21:34:05Z linjiao $

# End of file
