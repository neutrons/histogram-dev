#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.applications.Script import Script


def bracket(low, high):
    def _(x):
        if x>=low and x<=high: return x
        raise ValueError, '%s is not in [%s, %s]' % (x, low, high)
    return _


def parseHistogramIdentifier(identifier):

    #identifier should be the file path or a tuple of filepath and histogram entry
    
    tokens = identifier.split(',')
    ntokens = len(tokens)
    # make sure it is either a 2-tuple or just a path
    if ntokens<1 or ntokens>2: raise ValueError, "not a valid identifier: %s" % identifier

    # the first one is always the path
    filepath = tokens[0]
    
    # if entry is not specified, try to guess it
    if ntokens==1 or ntokens==2 and not tokens[1]:
        entry = _getOnlyEntry(filepath)
    else:
        entry = tokens[1]
    return filepath, entry

    
def _getOnlyEntry( h5filename ):
    from hdf5fs.h5fs import H5fs
    fs = H5fs( h5filename, 'r' )
    root = fs.open('/')
    entries = root.read()
    if len(entries)>1:
        msg = "Hdf5 file %s has multiple entries: %s. Please specify"\
              "the entry you want to open." % (
            h5filename, entries )
        raise RuntimeError, msg
    if len(entries)==0:
        msg = "Hdf5 file %s has no entry." % h5filename
        raise RuntimeError, msg
    
    entry = entries[0]
    return entry


class CompresshistogramApp(Script):


    class Inventory(Script.Inventory):

        import pyre.inventory

        level = pyre.inventory.int('z', default=1, validator=bracket(1,10))
        level.meta['tip'] = 'compression level. 1-10'

        histogram = pyre.inventory.str('in', default='histogram.h5')

        out = pyre.inventory.str('out', default='')


    def main(self, *args, **kwds):
        import histogram.hdf as hh
        h = hh.load(self.filepath, self.entry)
        hh.dump(h, self.out, mode='c', compression=self.level)
        return


    def __init__(self):
        Script.__init__(self, 'compressHistogram')
        return


    def _configure(self):
        Script._configure(self)
        self.level = self.inventory.level
        self.histogram = self.inventory.histogram
        self.out = self.inventory.out
        return


    def _init(self):
        Script._init(self)
        if self._showHelpOnly: return
        self.filepath, self.entry = parseHistogramIdentifier(self.histogram)
        if not self.out:
            self.out = '.'.join([self.filepath, 'compressed'])
        return



def main():
    app = CompresshistogramApp()
    return app.run()


# main
if __name__ == '__main__':
    # invoke the application shell
    main()


# version
__id__ = "$Id$"

# End of file 
