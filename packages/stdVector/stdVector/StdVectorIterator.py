#!/usr/bin/env python
# T. M. Kelley tkelley@caltech.edu (c) 2004


from TemplateCObject import TemplateCObject as Template
import stdVector

class StdVectorIterator( Template):
    """Class that wraps a C++ STL vector. 
    """

    def equal( self, otherIt):
        """equal( otherIter) -> True/False
        Returns true if this iterator points to the same place as the
        other.
        Iterators must be compatible: both must iterate std::vectors of the
        same type.
        Input:
            otherIt (instance of StdVectorIterator)
        Output: True or False
        Exceptions: TypeError, ValueError
        Notes:
        """
        self._isCompatible( otherIt)
        equal = stdVector.iteratorsEqual( self.handle(), otherIt.handle(),
                                          self.datatype())
        self._debug.log("Equals returned " + str(equal))
        return equal

    def incr( self):
        """incr() -> None
        increment your iterator
        input:
            None
        output:
            None
        Exceptions: ValueError
        Notes: None
        """
        stdVector.increment( self.handle(), self.datatype())
        return


    increment = incr

    def __init__( self, vect, **kwds):
        """StdVectorIterator( StdVector)
        inputs:
            1. StdVector instance
        outputs:
            New StdVectorIterator instance
        Exceptions: 
        Notes:
            recognized datatypes are
               float.......5
               double......6
               int........24
               unsigned...25
        """
        self.__journals()

        if "handle" in kwds.keys():
            handle = kwds['handle']
            self._debug.log( "handle = "+str( handle))
        elif 'offset' in kwds.keys():
            handle = stdVector.iterator( vect.handle(), vect.datatype(),
                                         kwds['offset'])
            self._debug.log( "handle = "+str( handle))
        else:
            msg = 'Must specify handle of iterator or offset into vector'
            raise RuntimeError, msg 

        Template.__init__( self, vect.datatype(), handle,
                           "StdVectorIterator")
        
        return


    def __journals(self):
        if '_debug' not in dir(self):
            import journal
            self._debug = journal.debug("StdVectorPy")
        return


# End class StdVectorIterator

# version
__id__ = "$Id: StdVectorIterator.py 49 2005-04-06 14:36:46Z tim $"

# End of file
