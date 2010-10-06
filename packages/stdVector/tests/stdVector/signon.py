#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 

if __name__ == "__main__":

    import stdVector
    from stdVector import stdVector as stdVectormodule

    print "copyright information:"
    print "   ", stdVector.copyright()
    print "   ", stdVectormodule.copyright()

    print
    print "module information:"
    print "    file:", stdVectormodule.__file__
    print "    doc:", stdVectormodule.__doc__
    print "    contents:", dir(stdVectormodule)

# version
__id__ = "$Id: signon.py 11 2004-10-01 22:27:14Z tim $"

#  End of file 
