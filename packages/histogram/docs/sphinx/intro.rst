.. _intro:

Introduction
============

This python package provides a fundamental data object for scientific computing:
histogram. A histogram object is a container of data, error bars, and axes. With
this package, you can create and manipulate histograms, and apply numerical
operators to histograms. The datasets in a histogram can be easily retrieved as
`numpy <http://numpy.org/>`_ arrays. The meta data of a histogram are accessible through member functions
of the histogram and the associated data objects.

This package is developed in the `DANSE <http://danse.us/>`_ package as the fundamental data object for
`DrChops <http://danse.us/trac/DrChops>`_, a reduction software for direct-geometry neutron chopper spectrometers.

A user can access a histogram through its public interface using the python shell.
Here is an example of a python session:

::

    from histogram import histogram, axis
    taxis = axis('t', [1.,2.,3.], unit='second')
    axes = [taxis]
    data = [3, 10, 5]
    errs = [3, 10, 5]
    h = histogram( "intensity", axes, data, errs)
    print h
    help(h)

For more details about how to manipulate histograms from the python command line,
please read :ref:`python-interface` . Histograms can also be accessed
from the Histogram GUI application, which may be more convenient and interactive.
The :ref:`gui` has more details about that.

