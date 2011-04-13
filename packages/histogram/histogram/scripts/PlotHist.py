#!/usr/bin/env python


from histogram import plot as plotHist


def plotPklFile( filename, min = None, max = None, output=None ):
    from histogram.hpickle import load
    h = load( filename )
    plotHist( h, min = min, max = max, output=output )
    return


def plotH5File( h5filename, pathinh5file = None, min = None, max = None, output=None ):
    if pathinh5file is None:
        from histogram.hdf.utils import getOnlyEntry
        pathinh5file = getOnlyEntry( h5filename )
    from histogram.hdf import load
    h = load( h5filename, pathinh5file )
    plotHist( h , min = min, max = max, output=output )
    return


def main():
    from optparse import OptionParser
    usage = "usage: %prog [options] histogram-data-file [internal-path]"
    parser = OptionParser(usage)
    parser.add_option("", "--min", dest="min", default = None,
                      type = "float", help="minimum")
    parser.add_option("", "--max", dest="max", default = None,
                      type = "float", help="maximum")
    parser.add_option("", '--output', dest='output', default='window',
                      help='window or filename.png')

    (options, args) = parser.parse_args()
    if not len(args) in [1,2]:
        parser.error("incorrect number of arguments")
        raise "should not reach here"

    filename = args[0]
    min = options.min
    max = options.max
    output = options.output
    
    if filename.endswith( 'h5' ):
        msg = "path to the histogram inside the h5 file '%s' is needed\n\n" % (
            filename, )
        msg += "  PlotHist.py --min=<min> --max=<max> histograms.h5 /path/to/histogram/in/h5file"
        if len(args) not in [1,2]: parser.error( msg )
        if len(args) == 1:
            entry = None
        else:
            entry = args[1]
        plotH5File( filename, entry, min = min, max = max, output = output )
        return
    
    plotPklFile( filename, min = min, max = max, output = output )
    return

