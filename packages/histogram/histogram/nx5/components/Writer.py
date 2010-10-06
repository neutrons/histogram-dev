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


class Writer(Component):


    class Inventory(Component.Inventory):

        import pyre.inventory as inv

        filename = inv.str("name")
        filename.meta['tip'] = "path and name of file"
        # end of inventory

    def write( self, selector, vector, starts, sizes):
        return self._writer( selector, vector, starts, sizes)


    def selector( self):
        return self._file.selector()
    

    def __init__(self, name = "Writer"):

        Component.__init__(self, name, facility='Writer')

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
        
        # create writer:
        from nx5.file.VectorWriter import Writer
        self._writer = Writer()
        
        return


    def _init(self):
        Component._init(self)
        return


# version
__id__ = "$Id: Writer.py 61 2005-04-13 23:21:28Z tim $"

# Generated automatically by PythonMill on Wed Apr 13 14:36:41 2005

# End of file 
