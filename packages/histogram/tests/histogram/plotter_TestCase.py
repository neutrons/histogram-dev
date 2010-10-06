#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


interactive = False


import unittest


from unittestX import TestCase
class plotter_TestCase(TestCase):

    def test1D(self):
        "pylab plotter: 1D"
        import histogram as H, pylab
        h = H.histogram(
            'h', 
            [('x', H.arange(10))], 
            fromfunction=lambda x: x*x,
            unit = "10" )
        self.plotter.plot(h)
        if interactive:
            raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return
        
    def test1D_largearray(self):
        "pylab plotter: 1D large array"
        import histogram as H, pylab
        h = H.histogram('h', [('x', H.arange(100000))], fromfunction=lambda x: x*x)
        self.plotter.plot(h)
        if interactive:
            raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return
        
    def test2Da(self):
        "pylab plotter: 2D. z<0"
        import histogram as H, pylab
        h = H.histogram(
            'h',
            [('x', H.arange(10)),
             ('y', H.arange( 5 )),
             ],
            fromfunction=lambda x,y: -(x*x + y*y),
            )
        self.plotter.plot(h)
        if interactive:
            raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return
    
    def test2Db(self):
        "pylab plotter: 2D. z>0"
        import histogram as H, pylab
        h = H.histogram(
            'h',
            [('x', H.arange(10)),
             ('y', H.arange( 5 )),
             ],
            fromfunction=lambda x,y: x*x + y*y,
            )
        self.plotter.plot(h)
        if interactive:
            raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return

    def test3(self):
        'plot sqe'
        import histogram.hdf as hh, pylab
        sqe = hh.load( 'sqe.h5/S(Q,E)' )
        self.plotter.plot(sqe)
        if interactive:
            raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return
    
    def test3a(self):
        'plot sqe with interpolation'
        import histogram.hdf as hh, pylab
        sqe = hh.load( 'sqe.h5/S(Q,E)' )
        self.plotter.plot(sqe, interpolation='bicubic')
        if interactive:
            raw_input('Press ENTER to continue')
        pylab.clf()
        pylab.close()
        return


    def __init__(self, *args, **kwds):
        super(plotter_TestCase, self).__init__(*args, **kwds)
        if not interactive:
            import matplotlib
            matplotlib.use('PS')
        from histogram.plotter import defaultPlotter
        if not interactive:
            defaultPlotter.interactive(0)
        self.plotter = defaultPlotter
        return
    
    
    pass # end of plotter_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(plotter_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    global interactive
    interactive = True
    
    import journal
##     journal.debug('instrument').activate()
##     journal.debug('instrument.elements').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id: plotter_TestCase.py 834 2006-03-03 14:39:02Z linjiao $"

# End of file 
