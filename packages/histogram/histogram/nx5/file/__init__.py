#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               T. M. Kelley
#                        California Institute of Technology
#                        (C) 2005  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


def file( filename, mode, factory = None, fs = None):
    """file( filename, mode) -> create a new file object
    modes: 'r' (read-only), 'w' (write-append), 'c' (create/truncate-existing)
    """
    if factory is None:
##         from SimpleFileFactory import FileFactory
##         factory = FileFactory()
        from File import File
        factory = File
        from SimpleFileInitializer import FileInitializer
        initializer = FileInitializer()
    return factory( filename, mode, initializer, fs = fs)


def reader():
    from VectorReader import Reader
    return Reader()


def writer():
    from VectorWriter import Writer
    return Writer()


def copyright():
    return "nx5 pyre module: Copyright (c) 1998-2004 T. M. Kelley";


# version
__id__ = "$Id: __init__.py 141 2008-06-01 15:44:12Z linjiao $"

#  End of file 
