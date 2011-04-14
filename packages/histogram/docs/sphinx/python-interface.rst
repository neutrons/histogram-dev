.. _python-interface:


Histogram Python Interface
==========================

For simplicity, in the following
examples, we all start by importing 
from the packages *histogram* and *numpy*. 

.. They include many
.. convenient functions like "histogram" factory and "exp" math functions.

::

 >>> from numpy import *
 >>> from histogram import *


Create a histogram
^^^^^^^^^^^^^^^^^^

To make an instance of a histogram:

::

 >>> h = histogram( "h", [ ('tof', arange(1000., 3000., 1.0), "microsecond") ] )

Here, string "h" denotes the name of the histogram. The tuple

::

  ('tof', arange(1000., 3000., 1.0), "microsecond")

defines a time-of-flight axis. The axis has a name 'tof', and the centers of the
bins on the axis are

::

  1000., 1001., ..., 2999.

The string "microsecond" is the unit of the tof axis. The tuple

::

  ('tof', arange(1000., 3000., 1.0), "microsecond")

is put into a list.


.. note::
   In many cases, histograms are multi-dimensional. For a multi-dimensional
   histogram, we need a list of axes, in which each item describes an axis.
   So, even for a 1D histogram, we require user to supply a single-item list,
   in which the only item describes the only axis for the histogram.

.. note::
   To construct a histogram, you could supply its axes using a list of tuples, 
   while each tuple represents an axis::

    [ ('x', range(10)), ('y', range(15)) ]
   
   or using a list of instances of Axis class::
   
    [ axis('x', range(10)), axis('y', range(15)) ]

.. _cheatsheat:

What is in a histogram? -- a quick overview
-------------------------------------------
If we try to print a histogram::

 >>> print h

The following text show up::

    Histogram "h"
    - Axes:
       - Axis tof: [ 1000.0, 1001.0, ... 2998.0, 2999.0 ]

    - Shape: [2000L]
    - Metadata: [('name', 'h')]
    - Data: ... [0. 0. ... 0.]
    - Errors: ... [0. 0. ... 0.]
    
A histogram has a name, a bunch of axes,
some meta data, and two main datasets: "data" and "errors".

* name: h.name()
* bin centers of an axis: h.<axisname>
 - For example, a histogram has an axis named "x", then the bin
   centers of "x" axis can be accessed as h.x.
* data (the "intensities" array): h.I
* error squares (the squares of error bars array): h.E2

For more details, please refer to :ref:`access-data`.


Equation: A test function
-------------------------
Now we want
to make this histogram more meaningful. Say we want the histogram "h" to have the
form of an exponential function


.. math::
   I = \exp(-\dfrac{tof}{1000})



In the python command line, we enter::

 >>> # get the bin centers the tof axis
 >>> tof = h.tof
 >>> # now we apply the function to the axis and assign it to the histogram
 >>> h.I = exp(-tof/1000.)
  
A shortcut to create the same histogram from scratch::

 >>> h = histogram(
      "h", 
      [
       ('tof', arange(1000., 3000., 1.0), "microsecond") 
      ],
      fromfunction = lambda x: exp(-x/1000.) )


.. _slicing:

Slicing
^^^^^^^

Probably the most important functionality of a histogram is slicing. First note
that the syntax of histogram slicing is different from normal python array slicing.
A python slicing looks like

::

 >>> a[ 3:10, 1:9 ]

whereas a histogram slicing looks like

::

 >>> h[ (3,10), (1,9) ]

Examples
--------

Create a histogram:

::

 >>> x = 'x', arange(-1, 1, 0.05 )
 >>> y = 'y', arange(-1, 1, 0.05 )
 >>> h = histogram( 'h', [x,y], fromfunction = lambda x,y: x*x + y*y )

Get a slice in the region x=(0.5, 0.9), y=(-0.8, 0.8)

::

 >>> h1 = h[ (0.5, 0.9), (-0.8, 0.8) ]

Get a slice in the region x=(minimum, 0.5), y=(-0.8, 0.8)

::

 >>> h2 = h[ (None, 0.5), (-0.8, 0.8) ]

Get a slice at x=0.5 over the full range of y

::

 >>> h3 = h[ 0.5, () ]

the resulting histogram is a 1D curve.

.. note::
   Slicing is by reference. No new data array will be created, and the new
   histogram is refering to a section of the original data. If you really
   need a copy, please use the "copy" method of the histogram object.

To set a slice is easy::

 >>> h[ <slice specification> ] = <new data>, <new error^2>

For example::

 >>> ycube = h.y**3
 >>> h[ 0.3, () ] = ycube, None
  
You may notice that we need a tuple on the right-hand side. The reason is there
are two datasets in a histogram: one for the data, another for the error squares. 
(Recall
that the squares of the errors are stored to reduce computation time.) 
In the 2-tuple

::

  ycube, None

"ycube" will be assign to the "data" dataset, 
and "None" will be assigned to the
"error bar squares" dataset. 
Actually "None" is a special dataset for error bar
squares: it means all error bars are zero.


Numerical Operators
^^^^^^^^^^^^^^^^^^^

Some basic numerical operators are available for manipulating histograms.
When these computations are performed, both data and error bars are processed.

The supported operators are:

::

  +, -, *, /, +=, -=, *=, /=


Examples
--------

First, create a histogram

::

 >>> x = 'x', arange(-1, 1, 0.05 )
 >>> y = 'y', arange(-1, 1, 0.05 )
 >>> h = histogram( 'h', [x,y], fromfunction = lambda x,y: x*x + y*y )

Then we add a constant to the histogram:

::

 >>> h += 3., 1.

Please note that there are two numbers on the right hand side, one for data,
another for error bar squares.

Next we add a histogram to a histogram

::

 >>> h1 = histogram( 'h1', [x,y], fromfunction = lambda x,y: x + y )
 >>> h2 = h + h1
 >>> h2 += h

You can do similar things with the other operators, following ususal Python syntax.

.. _error-prop:

Error Propagation
-----------------

It is assumed that the physical quantites represented by the histograms involved
in compuations are uncorrelated, and the error propagations are defined by the
following formulas:


.. math::
   z = x + y; \sigma^2_z = \sigma^2_x + \sigma^2_y


.. math::
   z = x - y; \sigma^2_z = \sigma^2_x + \sigma^2_y


.. math::
   z = x / y; \frac{\sigma^2_z}{z^2}  = \frac{\sigma^2_x}{x^2} + \frac{\sigma^2_y}{y^2}


.. math::
   z = x * y; \frac{\sigma^2_z}{z^2}  = \frac{\sigma^2_x}{x^2} + \frac{\sigma^2_y}{y^2}


Functions
^^^^^^^^^

sum
---

Description
"""""""""""

It will sum the data and the error bar squares of all bins, and return the total
counts and its error bar square. It can also sum a high-dimensional (D) histogram
along one axis, and return a histogram of reduced dimension (D-1).


Examples
""""""""

First, create a histogram

::

 >>> x = 'x', arange(-1, 1, 0.05 )
 >>> y = 'y', arange(-1, 1, 0.05 )
 >>> h = histogram( 'h', [x,y], fromfunction = lambda x,y: x*x + y*y )

Now,

::

 >>> h.sum()

returns a 2-tuple of counts and error bar square of all bins summed together.
The expression

::

 >>> h.sum( 'x' )

returns a 1-D histogram that results from summing over the axis 'x'.

reduce
------

Description
"""""""""""

Sometime you may have a histogram having an axis that is only one bin wide. Such
histograms (n-dimensional) are actually (n-1)-dimensional. You can reduce the
dimensionality of this kind of histogram by using this command.

Examples
""""""""

::

 >>> axes = [ ('x', [1,2,3]), ('yID', [1]) ]
 >>> data = [ [1,2,3] ]; errs = [ [1,2,3] ]
 >>> h = histogram( 'h', axes, data, errs )
 >>> h.reduce()


transpose
---------

Description
"""""""""""

This function transpose the axes of a histogram.

Examples
""""""""

The following commands create a 2-D histogram, and then transpose the x and y axes.

::

 >>> x = 'x', arange(-1, 1, 0.05 )
 >>> y = 'y', arange(0, 5, 0.05 )
 >>> h = histogram( 'h', [x,y], fromfunction = lambda x,y: x*x + y*y )
 >>> ht = h.transpose()


.. _access-data:

Accessing data
^^^^^^^^^^^^^^

.. _I_E2:

Retrieve Data and Error Bar Square Arrays
-----------------------------------------

Description
"""""""""""

Sometimes it may be necessary to develop new numeric operators and methods for
customized computation on the data array encapsulated in the histogram object.
They are accessible as attributes 'I' and 'E2'.

Examples
""""""""

::

 >>> x = 'x', arange(-1, 1, 0.05 )
 >>> y = 'y', arange(0, 5, 0.05 )
 >>> h = histogram( 'h', [x,y], fromfunction = lambda x,y: x*x + y*y )
 >>> dataarr = h.I
 >>> errsarr = h.E2
  
Both "dataarr" and "errsarr" are numpy arrays that reference to the underlying
data stored in the histogram. You can work directly on these arrays, and the
original histogram will be changed. 
Please see `numpy <http://www.numpy.org/>`_ documentation to learn of
other methods that are available in the numpy package.


axes
----

Description
"""""""""""

You can retrieve information about axes of a histogram using
methods of Histogram class:

* h.axes(): return a list of all axes
* h.axisNameList(): return a list of names of axes
* h.axisFromName(name): return the axis given the axis' name.

An axis contains data like bin boundaries and bin centers,
and metadata like unit.


Examples
""""""""

::

 >>> x = 'x', arange(-1, 1, 0.05 )
 >>> y = 'y', arange(0, 5, 0.05 )
 >>> h = histogram( 'h', [x,y], fromfunction = lambda x,y: x*x + y*y )
 >>> print h.axes()
 >>> print h.axisNameList()
 >>> xaxis = h.axisFromName( 'x' )
 >>> print xaxis.unit()
 >>> print xaxis.binCenters()
 >>> print xaxis.binBoundaries()


.. _plot:

Plot a histogram
^^^^^^^^^^^^^^^^

 >>> from histogram import plot
 >>> plot(h)


.. _save_load:

Save/load a histogram
^^^^^^^^^^^^^^^^^^^^^
You can save/load a histogram in hdf5 format.

* To save a histogram::
 >>> from histogram.hdf import dump
 >>> dump(h, 'myhist.h5')

* To load a histogram::
 >>> from histogram.hdf import load
 >>> h = load('myhist.h5')
