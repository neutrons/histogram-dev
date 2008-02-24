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

#--------------------------------------------------------------------------
#

all: clean

release: clean
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#

clean::
	@find * -name \*.bak -exec rm {} \;
	@find * -name \*.pyc -exec rm {} \;
	@find * -name \*~ -exec rm {} \;

# version
# $Id: Make.mm 2 2003-06-12 20:45:07Z tim $

# End of file
