#!/usr/bin/env python

from distutils.core import setup
setup(name = "histogram", version = 0.3, 
      packages=[
        "histogram", 
        "histogram.hdf", 
        "histogram.ndarray", "histogram.ndarray.converters",
        "histogram.scripts",
        "histogram.pyrecomponents", # obsolete
        ]
      )
