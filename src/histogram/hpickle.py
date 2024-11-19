#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                         (C) 2005 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import logging

logger = logging.getLogger("Histogram")

use = "system pickle"


if use == "system pickle":

    def dump(obj, filename):
        import pickle

        pickle.dump(obj, open(filename, "w"))
        return

    def load(filename):
        import pickle

        return pickle.load(open(filename))

    pass


# version
__id__ = "$Id: __init__.py 799 2006-02-23 16:45:51Z linjiao $"

# End of file
