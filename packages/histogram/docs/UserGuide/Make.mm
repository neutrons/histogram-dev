#-*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = histogram
PACKAGE = UserGuide

# directory structure

BUILD_DIRS = \

OTHER_DIRS = \


RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#

all: 
	BLD_ACTION="all" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy:: tidy-tmpxml tidy-tmpxsl
	BLD_ACTION="tidy" $(MM) recurse

export::
	BLD_ACTION="export" $(MM) recurse

test::
	BLD_ACTION="test" $(MM) recurse



DOCBOOKSOURCETEMPLATES = \
	Introduction.txml \
	CommandlineInterface.txml \
	HistogramGUI.txml \


include docbook/default.def

docs: export-docbook-docs



# version
# $Id: Make.mm 444 2006-03-31 07:20:49Z linjiao $

# End of file
