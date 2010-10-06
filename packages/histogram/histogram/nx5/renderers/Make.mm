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
PACKAGE = renderers


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    AbstractGraphFromObject.py \
    DataExtractor.py  \
    File_FromGraph.py  \
    Graph_FromFile.py \
    Graph_FromXML.py \
    GraphFromObjectOfStaticStructure.py \
    HDFPrinter.py \
    HDFVisitor.py \
    SetPath.py \
    XML_FromGraph.py \
    __init__.py  \


export:: export-package-python-modules

# version
# $Id: Make.mm 123 2007-03-24 05:09:30Z linjiao $

# End of file
