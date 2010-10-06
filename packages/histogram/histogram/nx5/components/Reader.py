#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 T. M. Kelley
#                   (C) Copyright 2005  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.components.Component import Component


class Reader(Component):


    class Inventory(Component.Inventory):

        import pyre.inventory as inv
        
        filename = inv.str( "filename", default = "")
        filename.meta['tip'] = "path and name of file"
        # end of inventory


    def read( self, selector, vector = None, start = [], sizes = []):
        return self._reader.read( selector, vector, start, sizes)


    def selector( self):
        return self._file.selector()


    def __init__(self, name = 'Reader'):

        Component.__init__(self, name, facility='Reader')

        return

    # -------------------- end of public interface ------------------------


    def _defaults(self):
        Component._defaults(self)
        return


    def _configure(self):
        Component._configure(self)
        
        self._filename = self.inventory.filename
        self._debug.log("filename is %s" % self._filename)

        # open file for r/w
        import nx5.file
        self._file = nx5.file.file( self._filename, 'w')
        
        # create reader:
        from nx5.file.VectorReader import Reader
        self._reader = Reader()
        
        return


    def _init(self):
        Component._init(self)
        return


# version
__id__ = "$Id: Reader.py 61 2005-04-13 23:21:28Z tim $"

# Generated automatically by PythonMill on Wed Apr 13 14:26:09 2005

# End of file 
