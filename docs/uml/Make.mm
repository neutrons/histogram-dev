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


# this Make.mm requires non-standard config package that includes 
#  config/make/std-docs.def

PROJECT = histogram
PACKAGE = uml


# directory structure

BUILD_DIRS = \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


PROJ_CLEAN =

#--------------------------------------------------------------------------
#

all: docs 
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

docs: export-all-files 
	BLD_ACTION="docs" $(MM) recurse


include std-docs.def


export-all-files::
	mkdir -p $(EXPORT_DOCDIR)
	rsync -av ./ $(EXPORT_DOCDIR)


# version
# $Id: Make.mm 1213 2006-11-18 16:17:08Z linjiao $

# End of file
