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
PACKAGE = nexml/elements


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    Compression.py \
    Dataset.py     \
    DetectorArray.py \
    DetectorPack.py  \
    Group.py       \
    Instrument.py   \
    LPSD.py \
    LPSDPixel.py\
    Moderator.py \
    Monitor.py  \
    Nexus.py  \
    NexusElement.py  \
    __init__.py


export:: export-package-python-modules

# version
# $Id: Make.mm 143 2009-01-05 00:05:03Z linjiao $

# End of file
