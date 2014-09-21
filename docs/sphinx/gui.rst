.. _gui:


Histogram GUI
=============

Histogram GUI interface helps you work on histograms, and see what you are doing.

Launch the Histogram GUI
^^^^^^^^^^^^^^^^^^^^^^^^

To launch the Histogram GUI application, type the following command:

::

  $ HistogramGUIApp.py

The main window will appear.

.. figure:: images/guiapp.png
   :width: 700px

   *Fig. 1 Histogram GUI snapshot*


The window is divided into three parts:

1. list of opened histograms are presented in the upper left corner,
2. plot of the current histogram is presented at the upper right, and
3. embedded python shell is available in the bottom window.

Load a Histogram
^^^^^^^^^^^^^^^^

A histogram can be loaded from a python pickle file.
`Reduction <http://docs.danse.us/histogram/reduction/Software-UserGuide/html/index.html>`_
applications such as LrmecsReductionLight and PharosReductionLight can produce histograms in the
proper format of pickled files.

To load a pickled histogram, select "File" from the main menu, and click "Open
histogram". A file dialog will show up, and you can pick a pickle file. Examples
of file names of pickled histograms are "sqehist.pkl", "spehist.pkl".

After you load the histogram, the name of this histogram will show up in the
histogram list in the window at the upper left, a plot will appear in the upper
right window, and the histogram is also available in the embedded shell window to
be manipulated further. You can save the plot by using menu "File" --> "Save plot
to file".

Embedded python shell
^^^^^^^^^^^^^^^^^^^^^

::

    Note: Some examples in this tutorial can be found under the "Tools" menu.
    
In the embedded python shell you can fine-tune your plot using 
`pylab commands <http://matplotlib.sourceforge.net/matplotlib.pylab.html>`_ .
If you are familiar with pylab or matlab, this should be really easy for you.

Here we explain how you may want to perform some simple tasks with the embedded
python shell.

2D False-Color Plotting
-----------------------


.. figure:: images/sqe.png
   :width: 700px

   *Fig. 2 S(Q,E)*

Let us first open a 2D histogram. From the menu bar, follow the sequence:

::

  File --> Open histogram --> Choose sqehist.pkl --> Click open

or you can do it in the command line window

::

  >>> import pickle
  >>> SQEData = pickle.load( open( 'sqehist.pkl' ) )

A pseudo-color plot will appear. Plot the transpose of I:

::

  >>> SQEData1 = SQEData.transpose()

Choose a range for axes

::

  >>> pylab.xlim( 0, 12 )

Usually the automatically-selected ticks work quite well. But if it is neceesary,
you can choose the tick mark spacing or add minor tick marks:

::

  >>> majorticks = pylab.ticker.MultipleLocator(2)
  >>> minorticks = pylab.ticker.MultipleLocator(1)
  >>> ax = pylab.gca()
  >>> ax.xaxis.set_major_locator( major )
  >>> ax.xaxis.set_minor_locator( minor )

You may notice that the minor ticks are really small, and you many want to change
the apperarance of the plot. We can change labels of the axes. The best visual
appearance can be achieved with LaTeX typesetting. This is done by first enabling
LaTeX support, and then specifying label texts using LaTeX syntax. Please remember
to use "raw" python strings (for example, r"$\AA$' will work, but '$\AA$' won't):

::

  >>> pylab.rcParams['text.usetex'] = 1 #enable LaTeX
  >>> pylab.xlabel( r"$Q {\rm(\AA^{-1})}$" )
  >>> pylab.ylabel( r"$E {\rm(eV)}$" )

You may add a title:

::

  >>> pylab.title( r"$S(Q,E)$" )

or add a colorbar,

::

  >>> pylab.colorbar()

You can choose the range of "z" values in which color-coding will be applied

::

  >>> pylab.clim( 0, 1e-3 )

You can choose a color palette (some color palettes render the faint details better than others). For example:

::

  >>> pylab.hot()
  >>> pylab.bone()

The following color maps are provided by pylab:

::

  autumn bone cool copper flag gray hot hsv jet pink prism
  spring summer winter spectral

If you have questions about color maps, you can get help by

::

  >>> help(pylab.colormaps)

Choice of plotting intensity I or Sqrt(I) or Ln(I) (if no zeroes)

::

  ???

You can zoom into a particular region by left-dragging your mouse. You can get a slice of the original data as fllows

::

  >>> h = SQEData[ (0,10), (-10,10) ]

The slicing syntax is

::

  >>> histslice = histogram[ (axis1min, axis1max), (axis2min, axis2max), ... ]

Again, you might find the
`documentation for pylab <http://matplotlib.sourceforge.net/matplotlib.pylab.html>`_
to be handy.


Plot of a 1D Curve
------------------

.. figure:: images/diffraction-pattern.png
   :width: 700px

   *Fig. 3 Diffraction pattern*


Continueing from the last section, we can create a 1D histogram by taking a sum
of the 2D histogram SQEData over an axis. Before we can do that, we need to know
the name of the axis over which the sum will be taken. This can be done by printing
out the information about a histogram:

::

  >>> print SQEData

and you will see a line like this:

::

  - Axis energy: [ -50.0, -49.0, ..., 50.0 ]

This will tell us there is an axis called "energy", and this axis name becomes
the argument of method "sum" in the following command

::

  >>> I_Q = SQEData.sum( "energy" )

You can zoom into a particular region by left-dragging your mouse. You can also
zoom in by entering commands in the python shell window if you prefer:

::

  >>> pylab.xlim( 2, 10 )
  >>> pylab.ylim( 0.0, )
  
Find bad detectors
------------------


An important task in data reduction is to find out bad detectors. It can be
performed by looking at the histogram of I(detector, pixel).

To obtain I(detector, pixel) from measured data, you can follow the instructions 
`here <http://docs.danse.us/histogram/measurement/UserGuide/html/index.html>`_ .


Tools menu
^^^^^^^^^^

The menu "Tools" is dynamic. You can load a toolset onto that menu by using menu "File-->Load a toolset".

The default set of menus under the "Tools" menu are:

* Raw data
* Reduction
* PRL
* Web