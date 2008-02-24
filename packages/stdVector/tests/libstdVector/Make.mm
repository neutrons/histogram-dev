# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               T. M. Kelley
#                        (C) 2004 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

include local.def

PROJECT = libstdVector/tests
PACKAGE = libTestStdVector
PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_CXX_LIB = $(BLD_LIBDIR)/$(PACKAGE).$(EXT_SAR)
PROJ_PYTESTS = 
PROJ_CPPTESTS = run_stdVectorTests #  stdVectorTest readCastTest
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES += -L$(BLD_LIBDIR) -L$(EXPORT_ROOT)/lib -L. -lTestStdVector -lstdVector -ljournal -lARCSTest
PROJ_CXX_INCLUDES += ../../src .

PROJ_SRCS = \
    stdVectorTest_add_scalar_vec.cc   \
    stdVectorTest_add_scalar_vecIt.cc \
    stdVectorTest_mult_scalar_vec.cc  \
    stdVectorTest_mult_scalar_vecIt.cc\
    stdVectorTest_vecPlus.cc         \
    stdVectorTest_vec_plusEquals.cc   \
    stdVectorTest_vec_minus.cc  \
    stdVectorTest_vec_minusEquals.cc  \
    stdVectorTest_vec_times.cc  \
    stdVectorTest_vec_timesEquals.cc  \
    stdVectorTest_vec_divide.cc \
    stdVectorTest_vec_divideEquals.cc \
    stdVectorTest_it_plusEquals.cc    \
#     stdVectorTest_divEquals.cc   \
#     stdVectorTest_extractSlice.cc   \
#     stdVectorTest_reduceSum2d.cc    \
#     stdVectorTest_reduceSum3d.cc    \
#     stdVectorTest_timesEquals.cc    \
#     stdVectorTest_squareVector.cc   \


#--------------------------------------------------------------------------
#

all: proj-cxx-lib $(PROJ_TESTS) 

test:
	for test in $(PROJ_TESTS) ; do $${test}; done

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#

rvm_srcs = \
    run_stdVectorTests.cc \
    main.cc             \


run_stdVectorTests:  $(rvm_srcs) $(BLD_LIBDIR)/libTestStdVector.$(EXT_SAR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ $(rvm_srcs) $(PROJ_LIBRARIES)



# version
# $Id: Make.mm 73 2005-05-17 23:36:46Z tim $

# End of file
