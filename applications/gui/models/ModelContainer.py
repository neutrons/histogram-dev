#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class ModelContainer:

    def __init__(self):
        self._store = {}
        self._seq = []
        return


    def get(self, name):
        return self._store.get(name)


    def set(self, name, model):
        self._store[name] = model
        return

    pass # end of ModelContainer


# version
__id__ = "$Id$"

# End of file 
