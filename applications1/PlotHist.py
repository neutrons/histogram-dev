#!/usr/bin/env python


def plotPklFile( filename, min = None, max = None ):
    from histogram.hpickle import load
    h = load( filename )
    from histogram.plotter import defaultPlotter
    defaultPlotter.interactive( 0 )
    defaultPlotter.plot( h, min = min, max = max)
    return


usage = """
PlotHist.py <histogram pickle file name>
PlotHist.py <histogram pickle file name> <min> <max>
"""


def main():
    import sys
    argc = len(sys.argv)
    if argc > 4 or argc < 2: raise usage

    min = max = None
    
    if argc == 2: 
        fn = sys.argv[1]
    elif argc == 3: 
        fn = sys.argv[1]
        min = float(sys.argv[2])
    elif argc == 4: 
        fn = sys.argv[1]
        min = float(sys.argv[2])
        max = float(sys.argv[3])
    else: raise usage
    
    plotPklFile( fn, min = min, max = max )
    return


if __name__ == "__main__": main()
    

