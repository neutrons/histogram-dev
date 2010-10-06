# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2003  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = array_kluge

include std-pythonmodule.def
include local.def

#PROJ_CXX_SRCLIB = $(BLD_LIBDIR)/lib$(PROJECT).$(EXT_LIB) -ljournal
PROJ_CXX_SRCLIB = -ljournal

PROJ_SRCS = \
    bindings.cc \
    exceptions.cc \
    misc.cc \
    charPtr2stringBdgs.cc \
    vPtr2stdvectorPtrBdgs.cc \
    vPtr2numarrayBdgs.cc \


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 51 2007-08-25 17:54:40Z linjiao $

# End of file
