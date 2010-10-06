#!/usr/bin/env python
# (c) 2003 T. M. Kelley, California Institute of Technology

import journal
debug = journal.debug("nx5.file.Reader")

from hdf5typeUtils import nativeTypeCode_from_h5Type, makeNativeH5Type, getH5Type
from vectorShapeUtils import volume, checkLength, checkShape

from Reader import Reader as ReaderBase

class Reader( ReaderBase):
    """reads datasets from nexus files into stdVectors."""

    def read( self, selector, vector = None, userStarts = [],
              userSizes = [], targetType = None):
        """read( selector, vector=None [, userStarts=[], userSizes=[] [, targetType=None]])
        Insert a nexus dataset, optionally a slab with starting indices
        given by starts, and dimension lengths given by sizes, into a
        stream, optionally converting from original datatype to targetType.
        selector: an nx5.file.Selector object.
        vector: vector from the stdVector package, data read into here
        starts: list of indices at which to start reading
            (length must be same as dataset rank)
        sizes: how many elements to read in each dimension
            (length must be same as dataset rank)
        targetType: Not Implemented Yet (NIY!) type you'd like results cast to (shd match vector!)
        Exceptions: IndexError, NotImplementedError, TypeError, ValueError
        Notes: http://wiki.cacr.caltech.edu/danse/index.php/Nexus_related_components_VectorReader
        To do: implement for string/char types
        """

        # open dataset:
        fs = selector.fs()
        selection = self.__getSelection( selector)
        dataset = fs.open( selection)

        # type
        fileType = getH5Type( dataset )

        # file space: prefer user specified size, default to what's in the file
        fileSpace = dataset.getSpace()
        fileDims = fileSpace.info()['dims']

        starts, sizes = self.__setStartsSizes( fileDims, userStarts, userSizes)

        readSize = volume(sizes)

        # create new space
        import hdf5fs.h5space
        newfileSpace = hdf5fs.h5space.H5space( fileDims)
        newfileSpace.selectHyperslab( "set", tuple(starts), tuple(sizes))

        # if user did not provide storage, allocate now,
        # otherwise check user vector ok
        vector = self.__getVector( vector, fileType, sizes)
        
        # memory space (delightfully flat!)
        memSpace = hdf5fs.h5space.H5space( (readSize,) )

        # read
        buff = vector.voidPtr().handle()
        # We need to be more careful about how we specify the type. If we just
        # say fileType, then we'll end up with exactly what's in the file, which
        # will fail to be portable across systems of different endian-ness, among
        # other vices.
        memType = self.__makeType( fileType)
        dataset.read( buff, memType, memSpace, newfileSpace)
        
        return vector


    def __init__(self):
        """Reader( ) -> new reader object"""
        ReaderBase.__init__( self)
        return 

# _______________________ end of public interface _____________________________


    def __getSelection( self, selector):
        # check selector (make sure same file)
#        self.__checkSelector( selector)

        # get selection from Selector, selection should be a path
        selection = selector.selection()

        # check that selection is a dataset
        # self.__checkDataset( selection)

        return selection
    

    def __getVector( self, vector, fileType, sizes):
        if vector is None:
            debug.log("vector == None")
            vector = self.__makeVector( fileType, sizes)
        else:
            # make sure user provided decent vector
            self.__checkVectorLength( vector, sizes)
            self.__checkVectorType( fileType, vector.datatype())
        return vector
    

##     def __checkSelector( self, selector):
##         if selector.filename() != self._filename:
##             msg = "selector refers to different file (%s) than Reader (%s)" %\
##                   ( selector.filename(), self._filename)
##             raise ValueError, msg
##         return
    
    
    def __checkVectorType( self, fileType, vecType):
        typeCode = self.__getTypeCode( fileType)
        debug.log("file type code: %s" % typeCode)
        if typeCode != vecType:
            msg = "vector type (%s) does not match code (%s) from file type (%s)" % \
                  ( vecType, typeCode, fileType.info())
            raise TypeError, msg
        return
    

    def __checkVectorLength( self, vector, sizes): checkLength( vector, volume(sizes) )


    def __makeType( self, typeObj): return makeNativeH5Type( typeObj )


    def __makeVector( self, typeObj, dims):
        typeCode = self.__getTypeCode( typeObj)
        length = volume( dims )
        debug.log("typeCode: %s, length  %s" % (typeCode, length))
        
        from stdVector import vector 
        vect = vector( typeCode, length)
        return vect


    def __getTypeCode( self, typeObj):
        return nativeTypeCode_from_h5Type( typeObj )
    
       
    def __setStartsSizes( self, fileDims, userStarts, userSizes):
        rank = len( fileDims)
        # if user specifies neither, starts = [ 0, ...], sizes = fileDims
        if userStarts == []:
            if userSizes == []:
                starts = [0 for i in range( rank)]
                sizes = [dim for dim in fileDims]
            else:
                # if user specifies sizes, but not starts, set starts at
                # beginning, ascertain sizes within dataset dimensions
                starts = [0 for i in range( rank)]
                self.__checkSizes( userSizes, fileDims)
                sizes = userSizes
        else:
            # if user specifies starts, but not sizes, make sure starts
            # within fileDims, set sizes to go to end
            if userSizes == []:
                self.__checkStartsInFileDims( userStarts, fileDims)
                starts = userStarts
                sizes = [ (dim - start) for (dim, start) in \
                          zip( fileDims, userStarts)]
            else:
                # if user specifies both, make sure
                # starts[i] + size[i] <= fileDim[i]
                # (<= because index should run from start to (start + size - 1)
                self.__checkStartsSizesInFileDims( userStarts, userSizes,
                                                   fileDims)
                starts = userStarts
                sizes = userSizes
        return starts, sizes
        

    def __checkSizes( self, sizes, dims): checkShape( sizes, dims )

    def __checkStartsInFileDims( self, starts, fileDims):
        checkShape( starts, fileDims )
        return
        
    def __checkStartsSizesInFileDims( self, starts, sizes, fileDims):
        from numpy import array
        ends = array(starts) + array(sizes)
        checkShape( ends, fileDims )
        return 
        
# End of class Reader

    
# Version
__id__ = "$Id: VectorReader.py 139 2007-11-05 18:40:05Z linjiao $"

# End of file
