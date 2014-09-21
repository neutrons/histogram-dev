.. _intro:

Introduction
============

The histogram `python <http://python.org>`_ package
provides a simple yet fundamental 
data structure for scientific computing: histogram.
A histogram object is a container of axes, data, and error bars.
With this package, you can create histograms, take slices of them,
and perform numerical operations. 

.. The datasets in a histogram can be easily retrieved as
.. `numpy <http://numpy.org/>`_ arrays. 
.. The meta data of a histogram are 
.. accessible through member functions
.. of the histogram and the associated data objects.

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
    from histogram.hdf import dump
    dump(slice, 'slice.h5')


Features
^^^^^^^^

* :ref:`Carries both data and error bars <cheatsheat>` and 
  has a :ref:`default implementation for error propagation <error-prop>`
* :ref:`Flexible slicing to get sub-histograms <slicing>`
* :ref:`Easy access to data as numpy arrays <I_E2>`
* :ref:`Dump/load histograms in hdf format <save_load>`
* :ref:`Quick plot using matplotlib <plot>`
* Minimal GUI application that 


Getting Started
^^^^^^^^^^^^^^^

* :ref:`Installation <install>`
* :ref:`Python interface <python-interface>`
* :ref:`Minimal GUI <gui>`


More information
^^^^^^^^^^^^^^^^
* `The histogram user group <http://googlegroups.com/group/histogram-users>`_
* `The danse project <http://danse.us>`_


This package is a product of the
`DANSE <http://danse.us>`_ project, 
which is supported by the US National Science Foundation 
under grant DMR-0520547.

.. For more details about how to manipulate histograms,
.. please read :ref:`python-interface` . 
.. Histograms can also be accessed
.. from within the Histogram GUI application, 
.. which may be more convenient and interactive.
.. The :ref:`gui` has more details about that.
