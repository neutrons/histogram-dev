#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 

if __name__ == "__main__":

    import histogram
    from histogram import histogram as histogrammodule

    print "copyright information:"
    print "   ", histogram.copyright()
    print "   ", histogrammodule.copyright()

    print
    print "module information:"
    print "    file:", histogrammodule.__file__
    print "    doc:", histogrammodule.__doc__
    print "    contents:", dir(histogrammodule)

    print
    print histogrammodule.hello()

# version
__id__ = "$Id$"

#  End of file 
