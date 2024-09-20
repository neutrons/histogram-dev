:orphan:

.. _install-details:

Installation Details
====================

Prerequsites
------------

The histogram package requires the following packages:

* numpy (http://numpy.org)


Optionally, you may want to install:

* `h5py <http://code.google.com/p/h5py/>`_: for load/dump histograms
* `matplotlib <http://matplotlib.sourceforge.net/>`_: for plotting


Install
-------
The histogram package can be installed by using pip install in editable mode currently::

 First, $ git clone git@github.com:neutrons/histogram-dev.git. Navigate to the root directory
 of histogram-dev. Create appropriate conda environment:
 $ conda env create 
 This will create an environment using the environment.yml file.

To install the package, in the correct environment(histogram-dev)::

 $ pip install -e . --no-deps
