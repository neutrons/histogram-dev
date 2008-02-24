# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        (C) 1998-2003 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = pyre
PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS = signon.py array_kluge_TestCase.py
PROJ_CPPTESTS = 
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -larray_kluge


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

hello: hello.cc $(BLD_LIBDIR)/libarray_kluge.$(EXT_AR)
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ hello.cc $(PROJ_LIBRARIES)

# version
# $Id: Make.mm 26 2006-04-17 03:41:54Z jiao $

# End of file
