#!/usr/bin/env python


def plotHist( h, min = None, max = None ):
    from histogram.plotter import defaultPlotter
    defaultPlotter.interactive( 0 )
    defaultPlotter.plot( h, min = min, max = max)
    return


def plotPklFile( filename, min = None, max = None ):
    from histogram.hpickle import load
    h = load( filename )
    plotHist( h, min = min, max = max )
    return


def plotH5File( h5filename, pathinh5file, min = None, max = None ):
    from histogram.hdf import load
    h = load( h5filename, pathinh5file )
    plotHist( h , min = min, max = max )
    return



def main():
    from optparse import OptionParser
    usage = "usage: %prog [options] histogram-data-file [args]"
    parser = OptionParser(usage)
    parser.add_option("", "--min", dest="min", default = None,
                      type = "float", help="minimum")
    parser.add_option("", "--max", dest="max", default = None,
                      type = "float", help="maximum")

    (options, args) = parser.parse_args()
    if not len(args) in [1,2]:
        parser.error("incorrect number of arguments")
        raise "should not reach here"

    filename = args[0]
    min = options.min
    max = options.max
    
    if filename.endswith( 'h5' ):
        msg = "path to the histogram inside the h5 file '%s' is needed\n\n" % (
            filename, )
        msg += "  PlotHist.py --min=<min> --max=<max> histograms.h5 /path/to/histogram/in/h5file"
        if len(args) != 2: parser.error( msg )

        plotH5File( filename, args[1], min = min, max = max )
        return
    
    plotPklFile( filename, min = min, max = max )
    return


if __name__ == "__main__": main()
    

