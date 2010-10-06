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



class AbstractPickler:

    """similar to python pickler, but save/load objects
    to hdf5 files
    """

    def dump(self, obj, fn, path = None):
        """dump a python object to the file "fn".

        path: path in the HDF file in which the object will be
          dumped.
        """
        raise NotImplementedError


    def load(self, fn, path = None):
        raise NotImplementedError

    pass # end of Pickler


# version
__id__ = "$Id$"

# End of file 
