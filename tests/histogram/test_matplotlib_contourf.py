#!/usr/bin/env python

from numpy import *

def main():
    import pylab
    a, b = 3,10
    x, y, z = array(arange(a)), array(arange(b)), array( arange((a)*(b)) )
    z.shape = b,a
    pylab.contourf( x,y, z, arange( (a)*(b) ) )
    pylab.show()
    return


if __name__ == "__main__": main()

