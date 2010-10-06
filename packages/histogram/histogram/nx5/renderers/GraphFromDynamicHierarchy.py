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


from AbstractGraphFromObject import Renderer as Base

class Renderer(Base):

    """This renderer deals with a hierarchy of objects.

    Each object must have an identify method to identify
    itself to this renderer.

    The implementation of this renderer really depends
    on the hierarchy to be visited. So solid implementation
    of this class should be placed inside whatever package
    that uses visitor pattern and has the need of dumping
    structure to a hdf5 file. An obvious usage would be
    the to render the instrument representation to a
    nexml graph.
    """

    def render(self, obj):
        raise NotImplementedError

    pass # end of Renderer



# version
__id__ = "$Id$"

# End of file 
