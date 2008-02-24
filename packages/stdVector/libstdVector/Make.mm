# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

include local.def

PROJECT = stdVector
PACKAGE = libstdVector

PROJ_CXX_LIB = $(BLD_LIBDIR)/$(PACKAGE).$(EXT_LIB)
#PROJ_SAR = $(BLD_LIBDIR)/$(PACKAGE).$(EXT_SAR)
PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)
PROJ_CLEAN += $(PROJ_INCDIR) $(PROJ_SAR)

PROJ_SRCS = \
    hello.cc   \
    vec_scalar_arith.cc \
    vec_vec_arith.cc	\
    vector2pylist.cc    \
    pylist2vector.cc    \
    reduceSum.cc        \
    utils.cc            \
#    VectorProxy.cc \

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# build the library

all: proj-cxx-lib export

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# build the shared object

$(PROJ_SAR): product_dirs $(PROJ_OBJS)
	$(CXX) -o $(PROJ_SAR) $(PROJ_OBJS) $(LCXXFLAGS)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# export

export:: export-headers export-libraries

EXPORT_HEADERS = \
    hello.h            \
    pylist2vector.h    \
    reduceSum.h        \
    reduction_utils.h  \
    reduction_utils.icc\
    slice.h            \
    slice.icc          \
    utils.h            \
    utils.icc            \
    vec_scalar_arith.h \
    vec_vec_arith.h \
    vector2pylist.h    \
    VectorProxy.h \
    VectorProxy.icc \


EXPORT_LIBS = $(PROJ_SAR) $(PROJ_CXX_LIB)


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 140 2007-05-15 22:06:44Z linjiao $

#
# End of file
