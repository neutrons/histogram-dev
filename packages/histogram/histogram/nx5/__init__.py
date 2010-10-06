#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               T. M. Kelley
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \mainpage nx5
##
## python package to access nexus file (in hdf5 format)
##
## The nx5 package simplifies reading and writing of pseudo-nexus files.
## (I say "pseudo-nexus", because not all of the groups we use are official
## nexus classes. Having said it once, I suppose I'll rely on the reader to
## remember that whenever I say "nexus", I mean "pseudo-nexus").
##
## nx5 is written purely in Python, all the interfacing to the
## actual hdf5 libraries is handled by the hdf5fs package.
## 
## \section dir_struct_sec Directory Structure
##
## - nexml: Classes for nexus elements.
## - file: Classes for file structure, reading, and writing datasets.
## - renderers: Classes for rendering file structure representations.
## - components: pyre components
##


def copyright():
    return "nx5 pyre module: Copyright (c) 1998-2004 T. M. Kelley";


# version
__id__ = "$Id: __init__.py 114 2006-10-12 00:35:38Z linjiao $"

#  End of file 
