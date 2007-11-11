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


class AbstractDataSource:


    def fetch(self, starts, shape):
        '''fetch data 
        starts: indexes where the data slice start
        shape: shape of the data slice
        '''
        raise NotImplementedError
    

    pass # end of AbstractDataSource


# version
__id__ = "$Id$"

# End of file 
