#!/usr/bin/env python

from numpy import *

def main():
    import pylab
    a, b = 3,10
    x, y, z = array(arange(a)), array(arange(b)), array( arange((a-1)*(b-1)) )
    z.shape = b-1,a-1
    X,Y = meshgrid (x,y)
    pylab.pcolor( X,Y, z)
    pylab.show()
    return


if __name__ == "__main__": main()

