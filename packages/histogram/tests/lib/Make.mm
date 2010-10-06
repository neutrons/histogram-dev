# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = histogram
PACKAGE = tests

PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS = 
PROJ_CPPTESTS = test_NdArray \
	test_NdArraySlice \
	test_GridData_1D \
	test_GridData_2D \
	test_GridData_4D \
	test_EvenlySpacedGridData_1D \
	test_EvenlySpacedGridData_2D \
	test_EvenlySpacedGridData_4D \

PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lhistogram


#--------------------------------------------------------------------------
#

all: $(PROJ_TESTS)

test:
	for test in $(PROJ_TESTS) ; do $${test}; done

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#

test_NdArray: test_NdArray.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_NdArray.cc $(PROJ_LIBRARIES)

test_NdArraySlice: test_NdArraySlice.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_NdArraySlice.cc $(PROJ_LIBRARIES)

test_GridData_1D: test_GridData_1D.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_GridData_1D.cc $(PROJ_LIBRARIES)

test_GridData_2D: test_GridData_2D.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_GridData_2D.cc $(PROJ_LIBRARIES)

test_GridData_4D: test_GridData_4D.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_GridData_4D.cc $(PROJ_LIBRARIES)

test_EvenlySpacedGridData_1D: test_EvenlySpacedGridData_1D.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_EvenlySpacedGridData_1D.cc $(PROJ_LIBRARIES)

test_EvenlySpacedGridData_2D: test_EvenlySpacedGridData_2D.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_EvenlySpacedGridData_2D.cc $(PROJ_LIBRARIES)

test_EvenlySpacedGridData_4D: test_EvenlySpacedGridData_4D.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_EvenlySpacedGridData_4D.cc $(PROJ_LIBRARIES)


# version
# $Id$

# End of file
