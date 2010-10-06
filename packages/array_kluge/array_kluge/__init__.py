#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                Tim Kelley
#                        California Institute of Technology
#                        (C) 1998-2003 All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \mainpage array_kluge
## The array_kluge package is useful for converting c arrays. Following converters exist:
##
##  - pylist__vptr: python list <-> poninter to c array
##  - numarray__vptr: numpy array <-- pointer to c array
##  - stdvector__vptr: pointer to c++ std::vector object <-- pointer to c array
##  - string__charPtr: python string <--> pointer to c char array
##
## Note:
##
##   No type checking is done in conversion. So the developer must
##   do type checking somewhere else. It is hard to do type checking
##   because a PyCObject of C pointer does not necessarily carries
##   any type information. Be careful when you use methods in this
##   package. Read documentation of each method carefully.


from create_type_lookup_table import *


def copyright():
    return "array_kluge pyre module: Copyright (c) 1998-2003 California Institute of Technology";


from pylist__vptr import *
from stdvector__vptr import *
from numarray__vptr import *
from string__charPtr import *


# version
__id__ = "$Id: __init__.py 46 2007-05-02 16:39:50Z linjiao $"

#  End of file 
