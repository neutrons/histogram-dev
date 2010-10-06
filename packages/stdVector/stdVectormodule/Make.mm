# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               T. M. Kelley
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = stdVector
PACKAGE = stdVectormodule
MODULE = stdVector

include std-pythonmodule.def
include local.def

PROJ_CXX_SRCLIB = -ljournal -lstdVector

PROJ_SRCS = \
    bindings.cc    \
    ctor_bdgs.cc   \
    exceptions.cc  \
    iterators.cc   \
    misc.cc        \
    numarray_bdgs.cc \
    proxy_bdgs.cc \
    pylist2vector.cc \
    reduceSum_bdgs.cc\
    slice_bdgs.cc \
    ufuncs.cc        \
    vector2pylist.cc \
    vectorCast_bdgs.cc \
    vec_scalar_arith_bdgs.cc \
    vec_vec_arith_bdgs.cc \

#    utils.cc         \


include doxygen/default.def
docs: export-doxygen-docs

# version
# $Id: Make.mm 140 2007-05-15 22:06:44Z linjiao $

# End of file
