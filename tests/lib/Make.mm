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

PROJ_PYTESTS = signon.py
PROJ_CPPTESTS = test_NdArray test_DataGrid1D test_DataGrid2D test_Itof test_Itof2
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

test_DataGrid1D: test_DataGrid1D.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_DataGrid1D.cc $(PROJ_LIBRARIES)

test_DataGrid2D: test_DataGrid2D.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_DataGrid2D.cc $(PROJ_LIBRARIES)

test_Itof: test_Itof.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_Itof.cc $(PROJ_LIBRARIES)

test_Itof2: test_Itof2.cc $(BLD_LIBDIR)/libhistogram.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_Itof2.cc $(PROJ_LIBRARIES)



# version
# $Id$

# End of file
