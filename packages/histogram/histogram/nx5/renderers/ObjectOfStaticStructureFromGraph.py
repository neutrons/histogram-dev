#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
It would nice to have a generic renderer
to render a data object from a nexml graph.
But this is almost impossible.
Different developers might write their hdf
file in totally different structure.
It is better to write a special renderer as a visitor
of nexml element hierarchy to render an object.
"""

# version
__id__ = "$Id$"

# End of file 
