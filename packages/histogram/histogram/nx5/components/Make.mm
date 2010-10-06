# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               T. M. Kelley
#                        California Institute of Technology
#                        (C) 1998-2003  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = nx5
PACKAGE = components


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES =  \
    Reader.py            \
    Writer.py            \
    __init__.py          \


export:: export-package-python-modules

# version
# $Id: Make.mm 61 2005-04-13 23:21:28Z tim $

# End of file
