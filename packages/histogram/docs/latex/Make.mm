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


# this Make.mm requires non-standard config package that includes 
#  config/make/std-docs.def
#  config/external/doxygen

PROJECT = histogram
PACKAGE = histogram


PROJ_TIDY = *.aux *.bbl *.pdf *.log *.blg *.dvi *.tex
TEX_DVIPS = dvips -Ppdf


# directory structure

BUILD_DIRS = \
	DeveloperGuide \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


PROJ_CLEAN = $(CLEAN_LATEX)  developer.tex developer.pdf
#developer.tex is generated from lyx file
# should we use *.pdf? maybe. pdf should all be generated automatically
# should we use *.tex? maybe not...


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse


#--------------------------------------------------------------------------
#
# export


TEXDOCS = \
	developer.pdf \
	developer2.pdf \

include std-docs.def


%.tex: %.lyx
	lyx --export latex $<

export:: 

export-texdocs:: $(TEXDOCS) $(EXPORT_DOCDIR)
	$(CP_F) *.pdf $(EXPORT_DOCDIR)


docs:: export-texdocs

# version
# $Id: Make.mm 1213 2006-11-18 16:17:08Z linjiao $

# End of file
