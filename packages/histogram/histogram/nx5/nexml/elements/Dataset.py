# (c) 2005 T. M. Kelley California Institute of Technology tkelley@caltech.edu

from NexusElement import NexusElement

class Dataset(NexusElement):

    def setCompression(self, level):
        from Compression import Compression
        self.compression = Compression(level)
        return
    
    
    def datatype(self): return self._datatype


    def dimensions(self): return self._dimensions


    def identify(self, inspector):
        return inspector.onDataset(self)


    def isDataset( self):
        return True


    def isGroup( self):
        return False


##     def id( self, inspector):
##         print "Deprecated: use identify"
##         return self.identify( inspector)


    def rank(self):
        dims = 0
        try:
            dims = len(self._dimensions)
        except TypeError, msg:
            print msg, "Simple dimensions"
            raise
        return dims


    def storage( self):
        """storage() -> StdVector or similar object
        Get the object in which the dataset's data is stored, if available."""
        return self._storage
    

    def __init__(self, name, className, nxpath, pathstr, dimensions, datatype,
                 storage = None):
        """Dataset( name, className, nxpath, pathstr, dimensions, datatype,
                 storage = None) -> new nexml Dataset
        Create node to represent dataset.
        Inputs:
            name: name of dataset (string)
            className: class (string, probably best left empty)
            nxPath: NXPath instance (set to None unless using nexml searcher)
            pathstr: string representing this node's path, use '/' as
                     path separator
            dimensions: list of dimension sizes
            datatype: nx5 datatype. Popular types include:
                4.......char
                5.......float
                6.......double
                24......unsigned int
                25......int
            storage: StdVector-like object that contains the actual data for
                     the dataset (default None)
        Output:
            new Dataset object to represent a dataset in an nx5 file."""
        NexusElement.__init__(self, name, className, nxpath, pathstr)
        self._dimensions = dimensions
        self._datatype = datatype
        self._storage = storage
        return


    def _compare(self, otherDataset, verbose=0):
        same = 1
        od = otherDataset
        sameNE = NexusElement._compare(self, od, verbose)
        same *= sameNE
        if self._dimensions != od.dimensions(): same *= 0
        if self._datatype != od.datatype(): same *= 0
        if verbose:
            print "nexus.nexml.elements.Dataset._compare(): same =",same
            print "dimensions: %s, %s" % (self._dimensions, od.dimensions())
            print "datatype: %s, %s" % (self._datatype, od.datatype())
        return same

# version
__id__ = "$Id: Dataset.py 143 2009-01-05 00:05:03Z linjiao $"

# End of file
