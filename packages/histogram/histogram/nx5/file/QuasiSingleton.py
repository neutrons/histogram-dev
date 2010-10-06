#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import journal
debug = journal.debug("nx5.file.quasisingleton")

import weakref, sys

class QuasiSingleton( object):
    """Base class that ensures no more than one interface to a given file"""

    instances = {}

    def __new__( cls, filename, mode, initializer, *args, **kwds):
        """get nx5 file interface"""

        # use only filename as key: want to ensure others can't get a separate
        # interface

        debug.line("filename.__class__.__name__: %s" % filename.__class__.__name__)
        debug.log("cls.__name__: %s; str(cls): %s" % ( cls.__name__, str(cls)))

        try:
            debug.log("file instances: %s" % cls.instances)
            theFile = cls.instances[ filename]()

            # if the referent has been garbage collected, the weak ref will
            # come out to None
            if theFile is not None:
                return theFile
        except KeyError:
            pass

        # 
        debug.log("about to instantiate object of class %s" % cls.__name__)

        theFile = object.__new__( cls)
        theFile.initialize( filename, mode, initializer, *args, **kwds)
        cls.instances[ filename] = weakref.ref( theFile)

        debug.log("new instance fs.h5ref has ref count: %s" % sys.getrefcount( theFile._fs.h5ref))
        debug.log("%s instances: %s" % (cls.__name__, cls.instances))

        return theFile


    # subclasses should provide file creation logic here
    def initialize( self, filename, mode, *args, **kwds):
        msg = "class %s must override initialize" % self.__class__.__name__
        raise NotImplementedError, msg
    

    def __del__( self):
        # Remove the instance corresponding to self._filename, if there is one,
        # from the class dictionary.        

##         print "%s instances: %s" % \
##               (self.__class__.__name__, self.__class__.instances)

        self.__class__.instances.pop( self._filename)        

        return


# version
__id__ = "$Id: QuasiSingleton.py 110 2006-07-20 05:54:01Z linjiao $"

# End of file
