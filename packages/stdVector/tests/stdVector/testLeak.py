#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from array_kluge import pylist2vptr
from array_kluge import *
from stdVector.VectorProxy import VectorProxy

import journal
journal.debug("array_kluge").activate();


__doc__ = """
With debug turned on for array_kluge bindings, you can see the sequence
of creating and deleting of a std::vector object. You can also see the reference
counting caused the delay of delete of std::vector.

A typical output would look like:

----------------------------------------------------------------------
linjiao@DHCP-30-147:.../arcs/packages/stdVector/tests/stdVector:: ./testLeak.py import Numeric
 >> vPtr2stdvectorPtr.h:26:newVector
 >> array_kluge(debug)
 -- created pointer0x30eca0
deleting v_ptr...
done
deleting vecProxy...
 >> utils.icc:35:deleteObject
 >> array_kluge(debug)
 -- deleted pointer0x30eca0
done
End of test
----------------------------------------------------------------------

"""

def testLeak():
    length = 10
    typecode = 6
    
    a = pylist2vptr ( range(length), typecode )
    v_ptr  = vPtr2stdvectorPtr ( a, length, typecode)
    
    #create proxy
    vecProxy = VectorProxy( typecode, v_ptr )

    print "deleting v_ptr..."
    del v_ptr
    print "done"

    print "deleting vecProxy..."
    del vecProxy
    print "done"
    
    print "End of test"
    return
        


if __name__ == "__main__": testLeak()


# version
__id__ = "$Id: proxy_TestCase.py 130 2005-07-07 15:24:11Z linjiao $"

# End of file 
