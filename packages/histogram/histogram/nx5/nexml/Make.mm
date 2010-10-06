# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2003  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = nx5
PACKAGE = nexml

BUILD_DIR = \
    elements \
    parser \

RECURSE_DIRS = $(BUILD_DIR)

#--------------------------------------------------------------------------
#

all: export

tidy::
	BLD_ACTION="tidy" $(MM) recurse

release: tidy
	cvs release .

update: clean
	cvs update .


#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    Parser.py \
    Searcher.py \
    StringStream.py \
    __init__.py \
    template.py \


export:: export-package-python-modules
	BLD_ACTION="export" $(MM) recurse

# version
# $Id: Make.mm 126 2007-03-29 21:49:38Z linjiao $

# End of file
