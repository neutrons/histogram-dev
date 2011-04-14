.. _intro:

Introduction
============

This python package provides a fundamental data object for scientific computing:
histogram. A histogram object is a container of axes, data, and error bars. 
With this package, you can create and manipulate histograms, and apply numerical
operators to histograms. 
The datasets in a histogram can be easily retrieved as
`numpy <http://numpy.org/>`_ arrays. 
The meta data of a histogram are 
accessible through member functions
of the histogram and the associated data objects.

Here is an example of a python session::

    from histogram import histogram, axis, arange, plot
    xaxis = axis('x', arange(5), unit='meter')
    yaxis = axis('y', arange(7), unit='cm')
    axes = [xaxis, yaxis]
    h = histogram( "intensity", axes, fromfunction=lambda x,y: x**2+y**2)
    print h
    plot(h)
    help(h)
    slice = h[3, ()]

For more details about how to manipulate histograms,
please read :ref:`python-interface` . 
Histograms can also be accessed
from within the Histogram GUI application, 
which may be more convenient and interactive.
The :ref:`gui` has more details about that.


This package is a product of the
`DANSE <http://danse.us>`_ project, 
which is supported by the US National Science Foundation 
under grant DMR-0520547.
