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
PACKAGE = histogram


# directory structure

BUILD_DIRS = \
	hdf \
	ndarray \
	pyrecomponents \
	scripts \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AttributeContBase.py \
	Axis.py	  \
	AxisMapper.py\
	AxisMapperCreater.py \
	DatasetBase.py   \
	DatasetContainer.py  \
	DetHistCollection.py \
	DictAttributeCont.py \
	DiscreteAxisMapper.py\
	ContinuousAxisMapper.py \
	EvenlyContinuousAxisMapper.py \
	Histogram.py \
	NdArrayDataset.py\
	SimpleHistCollection.py \
	SimpleRebin.py \
	SlicingInfo.py   \
	ValueWithError.py \
	ErrorPropagator.py \
	_loop.py \
	_units.py \
	__init__.py  \
	data_plotter.py  \
	paths.py  \
	plotter.py   \
	hpickle.py  \
	pylab_extensions.py  \

#    MonitorData.py       \


export:: export-python-modules


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id$

# End of file
