#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2003 All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 

if __name__ == "__main__":

    import array_kluge
    from array_kluge import array_kluge as array_klugemodule

    print "copyright information:"
    print "   ", array_kluge.copyright()
    print "   ", array_klugemodule.copyright()

    print
    print "module information:"
    print "    file:", array_klugemodule.__file__
    print "    doc:", array_klugemodule.__doc__
    print "    contents:", dir(array_klugemodule)


# version
__id__ = "$Id: signon.py 26 2006-04-17 03:41:54Z jiao $"

#  End of file 
