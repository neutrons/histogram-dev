.. _commands:


Commands
========

PlotHist.py
-----------

Synopsis ::

 Usage: PlotHist.py [options] histogram-file [internal-path]
 
 Options:
 
  -h, --help       show this help message and exit
  --output=OUTPUT  window or filename.png

Examples

There is only one entry in hist.h5::

 $ PlotHist.py hist.h5

There is multiple entries in hist.h5, and we want the entry
at "/diffraction_pattern"::

 $ PlotHist.py hist.h5 /diffraction_pattern

Plot the histogram into an image file::

 $ PlotHist.py --output=plot.png hist.h5 
