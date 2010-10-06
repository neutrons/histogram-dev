#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004

from stdVector import StdVector, stdVector as sv

def test1():
    s = StdVector.StdVector( [1., 2.,3.], 6)
    sv.assign( s.handle(), 6, s.size(), 2.3)
    s2 = StdVector.StdVector( [2.3]*3, 6)
    return s.compare( s2)


if __name__ == '__main__':
    import journal
    d = journal.debug('ARCSStdVector')
    d.activate()
    print test1()


# version
__id__ = "$Id: stdvecmodTest_assign.py 20 2004-10-14 22:04:58Z tim $"

# End of file
