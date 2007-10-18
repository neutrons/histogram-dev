# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = histogram
PACKAGE = ins

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	ARCSDetHistCollection.py\
	DetectorsTOFData.py	\
	DetPackData.py	\
	DetPixTOFData.py	\
	EnergyPhiData.py	\
	EnergyPixelData.py 	\
	EnergyQData.py	\
	MonitorData.py	\
	SModQEData.py	\
	SPhiEData.py	\
	SQEData.py	\
	TOFPixelData.py	\
	VanadiumData.py	\
	__init__.py	\


include doxygen/default.def

export:: export-package-python-modules 

# version
# $Id: Make.mm 1205 2006-11-15 16:23:10Z linjiao $

# End of file
