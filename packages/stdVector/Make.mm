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
    libstdVector \
    stdVectormodule \
    stdVector \

OTHER_DIRS = \
    tests \
    examples \


RECURSE_DIRS = $(BUILD_DIRS) + $(OTHER_DIRS)

#--------------------------------------------------------------------------
#

all:
	BLD_ACTION="all" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

docs::
	BLD_ACTION="docs" $(MM) recurse


# version
# $Id: Make.mm 144 2007-12-11 16:51:23Z linjiao $

# End of file
