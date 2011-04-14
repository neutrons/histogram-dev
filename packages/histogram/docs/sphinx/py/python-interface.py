from numpy import *
from histogram import *


def create():
    h = histogram( "h", [ ('tof', arange(1000., 3000., 1.0), "microsecond") ] )
    return h

def t1(h):
    # get the tof bin centers
    tof = h.tof
    # now we apply the function to the axis and assign it to the histogram
    h.I = exp(-tof/1000.)
    print h
    plot(h)
    return


def t2():
    from histogram import histogram, arange
    from numpy import  exp
    h = histogram(
        "h", [ ('tof', arange(1000., 3000., 1.0), "microsecond") ],
        fromfunction = lambda x: exp(-x/1000.) )
    print h
    plot(h)
    return


def t7():
    from histogram import histogram
    axes = [ ('x', [1,2,3]), ('yID', [1]) ]
    data = [[1],[2],[3]]; errs = [[1],[2],[3]]
    h = histogram( 'h', axes, data, errs )
    assert h.shape() == (3,1)
    h.reduce()
    assert h.shape() == (3,)
    return


def main():
    h = create()
    t1(h)
    t2()
    t7()
    return


if __name__ == '__main__': main()
