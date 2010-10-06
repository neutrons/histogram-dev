#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved


from hdf5typeUtils import nativeTypeCode_from_h5Type, makeNativeH5Type, getH5Type
from vectorShapeUtils import volume, checkLength, checkShape


import journal
debug = journal.debug("nx5.file")


from Writer import Writer as WriterBase
class Writer( WriterBase):
    """writes data from stdVectors to datasets in files """


    def write( self, selector, vector, starts=[], sizes=[]):
        """write( selector, vector, starts=[], sizes=[]) -> None
        write contents of vector to selected dataset, starting at indices
        indicated in starts, writing as many elements in each dimension as
        indicated in sizes.
        Inputs:
            selector: Selector object carrying the selected node info
            vector: vector to write
            starts: optional starting offset
            sizes: optional lengths to write in each dimension.
        Output:
            None
        Exceptions: FIX ME: find out
        Notes: (1) starts and sizes must have appropriate lengths and
        values."""

        # open dataset:
#        fs = self._nx5file.fs()
        fs = selector.fs()
        selection = self.__getSelection( selector)
        dataset = fs.open( selection)

        # type
        fileType = self.__getFileType( dataset)

        # file space: prefer user specified size, default to what's in the file
        fileSpace = dataset.getSpace()
        fileDims = fileSpace.info()['dims']

        userStarts, userSizes = self.__setStartsSizes( fileDims, starts, sizes)

        writeSize = volume(userSizes)

        import hdf5fs.h5space
        fileSpace = hdf5fs.h5space.H5space( fileDims)
        fileSpace.selectHyperslab( "set", tuple( userStarts),
                                   tuple( userSizes))
        self.__checkVectorLength( vector, userSizes)
        self.__checkVectorType( fileType, vector.datatype())

        # memory space (delightfully flat!)
        memSpace = hdf5fs.h5space.H5space( (writeSize,) )

        # write
        buff = vector.voidPtr().handle()
        dataset.write( buff, fileType, memSpace, fileSpace)
        return 


    def __init__( self, **kwds):
        WriterBase.__init__( self, **kwds)
        return

# ______________________ end of public interface ______________________


    def __checkSizes( self, sizes, dims): checkShape( sizes, dims )

    def __checkStartsInFileDims( self, starts, fileDims): checkShape( starts, fileDims )
        
    def __checkStartsSizesInFileDims( self, starts, sizes, fileDims): 
        from Numeric import array
        ends = array(starts) + array(sizes)
        checkShape( ends, fileDims )
        return 
    
    def __checkVectorType( self, fileType, vecType):
        typeCode = self.__getTypeCode( fileType)
        if typeCode != vecType:
            msg = "vector type (%s) does not match code (%s) from file type (%s)" % \
                  ( vecType, typeCode, fileType.info())
            raise TypeError, msg
        return
    

    def __checkVectorLength( self, vector, sizes): checkLength( vector, volume(sizes))

    def __getFileType( self, dataset):
        fileType = dataset.getType()
        return fileType


    def __getSelection( self, selector):
        # check selector (make sure same file)
#        self.__checkSelector( selector)

        # get selection from Selector, selection should be a path
        selection = selector.selection()

        # check that selection is a dataset
        # self.__checkDataset( selection)

        return selection
    

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
        

# version
__id__ = "$Id: VectorWriter.py 108 2005-10-28 00:21:07Z linjiao $"

# End of file
