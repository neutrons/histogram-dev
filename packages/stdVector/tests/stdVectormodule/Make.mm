# -*- Makefile -*-
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

PROJECT = stdVector

# directory structure

BUILD_DIRS = \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


PROJ_PYTESTS = alltests.py
PROJ_CPPTESTS =
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)


#--------------------------------------------------------------------------
#

all:
	BLD_ACTION="all" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

export::
	BLD_ACTION="export" $(MM) recurse

test::
	for test in $(PROJ_TESTS) ; do $${test}; done

# version
# $Id: Make.mm 475 2006-04-07 08:07:06Z jiao $

# End of file
