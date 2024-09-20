# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

include local.def

PROJECT = histogram
PACKAGE = libhistogram

PROJ_SAR = $(BLD_LIBDIR)/$(PACKAGE).$(EXT_SAR)
PROJ_DLL = $(BLD_BINDIR)/$(PACKAGE).$(EXT_SO)
PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)
PROJ_CLEAN += $(PROJ_SAR) $(PROJ_DLL)

PROJ_SRCS = \
	Array_1D.cc \
	events2Ix.cc \
	events2Ixy.cc \
	Event2Quantity.cc \
	NdArray.cc \
	NdArraySlice.cc \


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# build the library

all: $(PROJ_SAR) export

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ifeq (Win32, ${findstring Win32, $(PLATFORM_ID)})

# build the shared object
$(PROJ_SAR): product_dirs $(PROJ_OBJS)
	$(CXX) $(LCXXFLAGS) -o $(PROJ_DLL) \
	-Wl,--out-implib=$(PROJ_SAR) $(PROJ_OBJS)

# export
export:: export-headers export-libraries export-binaries

else

# build the shared object
$(PROJ_SAR): product_dirs $(PROJ_OBJS)
	$(CXX) $(LCXXFLAGS) -o $(PROJ_SAR) $(PROJ_OBJS)

# export
export:: export-headers export-libraries

endif

EXPORT_HEADERS = \
	Array_1D.h \
	Array_1D.icc \
	AxisMapper.h \
	Event2Quantity.h \
	GridData_1D.h \
	GridData_2D.h \
	GridData_4D.h \
	EvenlySpacedAxisMapper.h \
	EvenlySpacedGridData_1D.h \
	EvenlySpacedGridData_2D.h \
	EvenlySpacedGridData_4D.h \
	Exception.h\
	Histogrammer.h \
	NdArray.h \
	NdArray.icc \
	NdArraySlice.h \
	NdArraySlice.icc \
	OutOfBound.h\
	events2histogram.h \
	events2EvenlySpacedIx.h \
	events2EvenlySpacedIxy.h \
	events2EvenlySpacedIxxxx.h \
	events2Ix.h \
	events2Ixy.h \
	events2Ixxxx.h \
	_macros.h \


EXPORT_LIBS = $(PROJ_SAR)
EXPORT_BINS = $(PROJ_DLL)


# version
# $Id$

#
# End of file
