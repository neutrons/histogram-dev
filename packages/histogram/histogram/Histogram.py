#!/usr/bin/env python

## \package histogram.Histogram
## This package contains the most important class, Histogram.
## For users, it is much easier to use the convenient function
## "histogram"
## in histogram.__init__ package to create histogram.


import journal
debug = journal.debug('ins.histogram.Histogram')
     
import operator
from DictAttributeCont import AttributeCont

class Histogram( AttributeCont):

    """Histogram

  Histogram is the most important data object of the histogram package.
  Public interface:
    h.axes(): return a list of axes
    h.I: return the reference to the data in a numpy array
    h.E2: return the reference to the error bar squares in a numpy array
    h.unit(): return the unit of the data of this histogram
    h.axisNameList(): return a list of names of the axes.
    h.<axis name>: return the bin centers of the axis for the given axis name.
    numeric operators: + - * /
    h.copy: create a deep copy of the given histogram
    slicing: use operator []

  Examples:
    >>> from histogram import histogram, axis, arange
    >>> daxis = axis('dspacing', arange(0,4,0.01))
    >>> h = histogram('h', [daxis])
    >>> print h.axes()
    >>> print h.axisNameList()
    >>> print h.unit()
    >>> print h.dspacing
    >>> print h.I
    >>> print h.E2
    >>> h1 = h.copy()
    >>> h2 = h + h1
    >>> h3 = h2*(2.0, 2.0)
    >>> h4 = h3*h4
    >>> h4 /= (10.0, 0.0)
    >>> h5 = h4[(0,2)]
    >>> h4[2,4] = 0,0
    """

    def __init__( self, name = '', data = None, errors = None,
                  axes = [], attributes = None, unit = '1', **kwds):
        """Histogram( name, data, errors, axes, attributes) -> new Histogram
        Create a new histogram instance.
        Inputs:
            name: name of histogram (string)
            data: dataset (implements DatasetBase)
            errors: dataset (implements DatasetBase)
            axes: list of Axes objects (implements Axis)
            attributes: optional dictionary of user-defined attributes
        Output:
            None
        Exceptions: IndexError, TypeError
        Notes: (1) IndexError if data and errors don't have same shape
        (2) TypeError if data and errors don't have same type"""

        # whether the histogram is a slice (reference not copy) of another histogram
        self._isslice = kwds.get('isslice') or False

        if attributes is None: attributes = dict()
        AttributeCont.__init__( self, attributes)
        self.setAttribute( 'name', name)
        self.setAttribute( 'unit', tounit(unit) )

        from DatasetContainer import DatasetContainer as DC

        self._axisCont = DC()

        for i, axis in enumerate( axes):
            axNum = i + 1 #by default axes ids are 1,2,3,...
            self._axisCont.addDataset( axis.name(), axNum, axis)
            continue
        if len(axes) == 1: self._axis = axes[0]

        self._lastDatasetID = 0
        self._dataCont = DC()
        
        if data is None: raise ValueError, "No data provided"
        self._add_data_and_errors( data, errors )
        return


    def as_floattype(self):
        '''return a copy of this histogram in float type

        Some histograms are created in integer types.
        But integer types are often not good for further data analysis.
        This method creates a new histogram with the
        exact same axes and data and error bars, but in
        float type.
        '''
        if self.typeCode() in integer_typecodes:
            from histogram import histogram
            axescopy = []
            for axis in self.axes():
                axescopy.append( axis.copy() )
                continue
            return histogram( self.name(), axescopy, data = self.I, errors = self.E2)
        
        elif self.typeCode() in float_typecodes :
            return self.copy()
        
        raise TypeError, 'histogram of type %r cannot be converted to float type' % self.typeCode()


    def unit(self): return self.getAttribute( 'unit' )


    def isunitless(self): return isunitless(self.unit())


    def isslice(self): return self._isslice


    def replaceAxis(self, name='', id=None, axis=None):
        self._axisCont.replaceDataset(name=name, id=id, dataset=axis)
        return self


    def __getitem__(self, s):
        """Slicing
        h[ (3.0, 4.0), () ]
        h[ 3.0, () ]
        h[ (), () ]
        h[ (None, 4.0),  (999., None ) ]
        """
        if self.errors() is None:
            raise NotImplementedError , "__getitem__: errors is None"

        # if s is iterable, we should assume that it is trying to do slicing.
        # This also means no axis can use iterables as values.
        if self.dimension() == 1 and '__iter__' not in dir(s): s = (s,)

        # We also allow use of dictionary. This is a convenient and flexible way
        # to get or set a slice.
        if isinstance(s, dict): 
            s = _slicingInfosFromDictionary(s, self.axes())
        else: 
            s = _makeSlicingInfos( s, self.dimension() )
        #at this point, s is a tuple of SlicingInfo instances.

        # check sanity of inputs
        if not isinstance(s, tuple) or len(s) != self.dimension():
            raise NotImplementedError , "Histogram[ %s ]. my dimension: %s" % (
                s, self.dimension())

        # a more meaningful name
        slicingInfos = s

        # slicingInfo tuple --> a tuple of index slices
        indexSlices = self.slicingInfos2IndexSlices( slicingInfos )
        
        #the following line will fail if a dataset is None
        #should define a special NoneDataset to solve this problem
        newdatasets = [dataset[indexSlices] for dataset in self.datasets()]

        #if requested for item instead of slice, return the item now.
        if isNumber(newdatasets[0]) or isDimensional(newdatasets[0]):
            return newdatasets

        #meta data need to be passed to the new histogram
        newAttrs = self._attributes.copy()

        #axes of new histogram
        newAxes = []
        for slicingInfo, name in zip(slicingInfos, self.axisNameList()):
            axis = self.axisFromName( name )
            if not isSlicingInfo( slicingInfo ):
                # if it is not a slicingInfo instance,
                # it must be a value indexable in this axis.
                # This is already tested in method "slicingInfo2IndexSlices"
                value = '%s' % slicingInfo
                name = axis.name()
                newAttrs[name] = value
            else:
                newAxes.append( axis[ slicingInfo ] )
                pass
            continue
            
        #name of new histogram
        newName = "%s in %s" % (
            self.name(),
            ["%s(%s)"%(axisName, slicingInfo) for axisName, slicingInfo \
             in zip(self.axisNameList(), slicingInfos)])

        #new histogram
        new = Histogram( 
            name = newName, unit = self.unit(),
            data = newdatasets[0], errors = newdatasets[1],
            axes = newAxes, attributes = newAttrs, slice = True)

        #addtional datasets. This is not tested yet!!!
        #probably we should really limit histogram to have only two datasets!!!
        for i in range(2, len(newdatasets)):
            ds = newdatasets[i]
            new.addDataset( ds.name(), ds )
            continue

        return new
            

    def __setitem__(self, indexes_or_slice, v):
        if self.errors() is None: raise NotImplementedError , "__setitem__: errors is None"

        # if indexes_or_slice is iterable,
        # we should assume that it is trying to do slicing.
        # This also means no axis can use iterables as values.
        if self.dimension() == 1 and '__iter__' not in dir(indexes_or_slice):
            indexes_or_slice = (indexes_or_slice,)

        # We also allow use of dictionary. This is a convenient and flexible way
        # to get or set a slice.
        if isinstance(indexes_or_slice, dict):
            s = _slicingInfosFromDictionary(indexes_or_slice, self.axes())
        else:
            s = _makeSlicingInfos( indexes_or_slice, self.dimension() )
            pass # end if
        
        #at this point, s is a tuple of SlicingInfo instances.
        slicingInfos = s

        # check sanity of inputs
        if not isinstance(s, tuple) or len(s) != self.dimension():
            raise NotImplementedError , "Histogram[ %s ]. my dimension: %s" % (
                s, self.dimension())

        mydatasets = self.datasets()
        
        # slicingInfo tuple --> a tuple of index slices
        indexSlices = self.slicingInfos2IndexSlices( slicingInfos )
        
        #now we want to know if user is requesting for a real slice
        #or just an element
        #this is done by trying to get a slice of the dataset self._data
        aslice = self._data[indexSlices]
        #1. element, not slice
        if isNumber(aslice) and isNumberList(v) :
            if len(v) == 2:
                self._data[indexSlices] = v[0]
                self._errors[indexSlices] = v[1]
                pass
            elif len(v) == len(mydatasets):
                for i, ds in enumerate(mydatasets): ds[indexSlices] = v[i]
                pass
            else:
                raise RuntimeError , \
                      "shape mismatch in histogram[ indexes ] = value tuple. "\
                      "len(value tuple) = %s, but histogram has %s datasets" \
                      % (len(v), len(mydatasets))
            return v

        #2. slice
        #shape = aslice.shape() #get shape
        # for slice, we would require the right hand side to be a list of datasets
        if isHistogram( v ): v = v.data(), v.errors()

        # try to set slice, defer to dataset's __setitem__
        # but first we must assert length of arrays match
        assert len(v) == len(mydatasets), \
               "rhs must be a %s-tuple of datasets, "\
               "instead of a %s-tuple" % (
            len( mydatasets ), len(v) )
        for lhs, rhs in zip(mydatasets, v):
            if rhs is not None : lhs[ indexSlices ] = rhs
            else: debug.log( 'indefinite behavior: setting to None' )
            continue

        return self[ indexes_or_slice ]


    #numeric operators
    
    def __neg__(self):
        return self * -1


    def __mul__(self, other):
        r = self.copy()
        r *= other
        return r


    __rmul__ = __mul__
        
                
    def __add__(self, other):
        r = self.copy()
        r += other
        return r
        

    __radd__ = __add__


    def __sub__(self, other):
        r = self.copy()
        r -= other
        return r


    def __rsub__(self, other):
        r = self.copy()
        r *= (-1,0)
        r += other
        return r


    def __div__(self, other):
        r = self.copy()
        r /= other
        return r


    def __rdiv__(self, other):
        if isNumberPair(other):
            r = self.copy()
            r.reverse()
            r *= other
            return r

        raise NotImplementedError , "__rdiv__ is not defined for %s and %s" % (
            other.__class__.__name__, self.__class__.__name__, )
            

    def __iadd__(self, other):
        """self += b
        b is a pair of numbers (x, xerr_square) or another histogram
        """
        data = self._data; errs = self._errors
        
        if isNumberPair(other) and self.isunitless():
            
            x, xerr = other
            data += x
            errs += xerr

            pass

        elif isDimensionalPair( other ):

            x, xerr = other
            data += x
            errs += xerr

            pass
        
        elif isHistogram(other):
            
            data +=  other._data;
            if errs is None:
                if other._errors is not None: 
                    self._dataCont.replaceDataset("error", other._errors.copy() )
                    pass
                pass
            else:
                errs +=  other._errors
                pass
            pass
        
        else:
            
            raise NotImplementedError , "__add__ is not defined for %s and %s" % (
                self.__class__.__name__, other.__class__.__name__, )
        
        return self


    def __isub__(self, other):
        """self -= b
        b is a pair of numbers (x, xerr_square) or another histogram
        """
        data = self._data; errs = self._errors
        
        if isNumberPair(other) and self.isunitless():
            
            x, xerr = other
            data -= x; errs += xerr

            pass

        elif isDimensionalPair(other):

            x, xerr = other
            data -= x; errs += xerr

            pass
        
        elif isHistogram(other):
            
            data -=  other._data; errs +=  other._errors 

        else:
            
            raise NotImplementedError , "__sub__ is not defined for %s and %s" % (
                self.__class__.__name__, other.__class__.__name__, )
        
        return self


    def __imul__(self, other):
        """self *= b
        b is a pair of numbers (x, xerr_square) or another histogram
        """
        data = self._data; errs = self._errors
        
        if isNumberPair(other) or isDimensionalPair(other):
            
            y, dy2 = other
            y, dy2 = float(y), float(dy2)

            #B**2*sigmaA**2 + A**2*sigmaB**2
            #term2 = dy2 * data * data
            #term1 = errs * y * y
            errs *= y*y
            errs += dy2*data*data
            
            data *= y
            pass

        
        elif isHistogram(other):
            y = other.data(); dy2 = other.errors()
            #
            errs *= y*y
            errs += dy2 * data*data

            data *= y

            self._setunit( self.unit() * other.unit() )
            
        else:
            
            raise NotImplementedError , "__mul__ is not defined for %s and %s" % (
                self.__class__.__name__, other.__class__.__name__, )

        self._syncUnit()
        return self

    def __idiv__(self, other):
        """self /= b
        b is a pair of numbers (x, xerr_square) or another histogram
        """
        data = self._data; errs = self._errors
        # sigmaA**2/B**2 + A**2*sigmaB**2/B**4
        
        if isNumberPair(other):
            y,  dy2 = other
            y, dy2 = float(y), float(dy2)
            if dy2 == 0 or dy2 == 0.0: #special case
                #ydx/y^2
                self._setunit(1.*self.unit()/y)
                return self

            errs /= y*y
            errs += dy2 * data * data / y**4
            
            data /= y
            pass
        
        elif isDimensionalPair(other):
            y, dy2 = other
            unitlessother = 1, dy2/y/y
            self._setunit( 1.*self.unit()/y )
            self /= unitlessother
            pass
        
        elif isHistogram(other):

            y = other._data; dy2 = other._errors
            
            if dy2 == None: #special case
                #ydx/y^2
                errs /= y; errs /= y
                data /= y
                return self

            errs /= y*y
            errs += dy2 * data * data /y/y/y/y
            
            data /= y

            self._setunit( self.unit()/other.unit() )
            
        else:
            
            raise NotImplementedError , "__div__ is not defined for %s and %s. "\
                  "self=%s, other=%s" % (
                self.__class__.__name__, other.__class__.__name__,
                self, other)

        self._syncUnit()
        return self

    def __getattribute__(self, name):
        try: return object.__getattribute__(self, name)
        except AttributeError:
            if name in self.axisNameList():
                return self.axisFromName(name).binCenters()
            raise
        raise "Should not reach here"

    def clear(self):
        '''set data and errorbars to zero'''
        shape = self.shape()
        d = self.data()
        d *= 0
        e = self.errors()
        if e: e *= 0
        return        
        

    def transpose(self, *axis):
        '''Returns a view of histogram with axes transposed.
        If no axes are given,
        or None is passed, switches the order of the axes. For a 2-d
        histogram, this is the usual matrix transpose. If axes are given,
        they describe how the axes are permuted.
        '''
        name = self.name()
        oldAxisNames = self.axisNameList()
        if axis is None or len(axis) == 0:
            newAxisNames = list(oldAxisNames)
            newAxisNames.reverse()
            indaxis = None
        else:
            if len(axis) != 2:
                raise ValueError , "Cannot transpose axis %s" % (axis, )
            a, b = axis
            newAxisNames = list(oldAxisNames)
            i = newAxisNames.find( a )
            j = newAxisNames.find( b )
            if i == -1 or j == -1:
                raise ValueError , "Cannot transpose axis %s and %s" %(
                    a, b )
            indaxis = i,j
            newAxisNames[i] = oldAxisNames[j]
            newAxisNames[j] = oldAxisNames[i]
            pass

        axes = [ self.axisFromName( n ) for n in newAxisNames ]
        
        data = self.data().transpose(*axis)
        errors = self.errors().transpose(*axis)

        attrs = {}
        for k in self.listAttributes():
            attrs[k] = self.getAttribute( k )
            continue

        h = Histogram(
            name = name, data = data, errors = errors,
            axes = axes, attributes = attrs )
        
        return  h


    def reverse(self):
        err = self._errors
        err/= self._data
        err/= self._data
        err/= self._data
        err/= self._data
        self._data.reverse()
        return


    def average(self):
        dataSum = self._data.sum()
        errsSum = self._errors.sum()
        n = self.size()
        dataAve = dataSum/n
        errsAve = errsSum/n/n
        return dataAve, errsAve


    def sum(self, axisName = None):
        if axisName is None: return self._data.storage().sum(), self._errors.storage().sum()
        axisIndex = self.axisIndexFromName( axisName )
        
        theAxisName = axisName
        
        axes = []
        for axisName in self.axisNameList():
            if axisName == theAxisName: continue
            axes.append( self.axisFromName( axisName ).copy() )
            continue
        
        attrs = self._attributes.copy()

        name = "sum of %s over axis %s" % (self.name(), theAxisName)
        
        newdata = self._data.sum(axisIndex)
        newerrors = self._errors.sum(axisIndex)
        # has to rename the datasets to follow the convention
        # required for histogram
        newdata.setAttribute('name', 'data')
        newerrors.setAttribute('name', 'errors')
        res =  Histogram(
            name = name, unit = self.unit(),
            data = newdata, errors = newerrors,
            axes = axes, attributes = attrs )

        #add all other datasets
        #dss = self.datasets()
        #for i in range(2, len(dss)):
        #    ds = dss[i]
        #    res.addDataset( ds.name(), ds.copy() )
        #    continue
        return res
        
    

    #---

    def name(self): return self.getAttribute('name')
    def rename(self, newname):
        self.setAttribute('name', newname)
        return self
    

    def dimension(self): return self._dimension


    def copy(self):
        axes = []
        for axisName in self.axisNameList():
            axes.append( self.axisFromName( axisName ).copy() )
            continue
        
        attrs = self._attributes.copy()
        
        res =  Histogram(
            name = self.name(), unit = self.unit(),
            data = self._data.copy(), errors = self._errors.copy(),
            axes = axes, attributes = attrs )

        #add all other datasets
        dss = self.datasets()
        for i in range(2, len(dss)):
            ds = dss[i]
            res.addDataset( ds.name(), ds.copy() )
            continue
        
        return res


    def slicingInfos2IndexSlices(self, slicingInfos):
        indexSlices = []
        for slicingInfo, axisName in zip( slicingInfos, self.axisNameList() ):
            
            axis = self.axisFromName( axisName )
            
            #convert slicing info or value to slice or index
            if isSlicingInfo(slicingInfo):
                indexStart, indexEnd = axis.slicingInfo2IndexSlice( slicingInfo )
                s = slice(indexStart, indexEnd)
            else:
                value = slicingInfo 
                s = axis.cellIndexFromValue( value )

            
            indexSlices.append( s )
            continue
        return tuple(indexSlices)

    values2indexes = slicingInfos2IndexSlices
    

    def addDataset( self, name, dataset ):
        self._lastDatasetID += 1
        self._dataCont.addDataset( name, self._lastDatasetID, dataset )
        return


    def datasets(self):
        "return all my datasets. the first two datasets must be 'data' and 'errors'"
        dc = self._dataCont
        ret = [ dc.datasetFromId( id ) for id, name in dc.listDatasets() ]
        assert ret[0] == self._data and ret[1] == self._errors
        return ret


    def axes(self):
        return [ self.axisFromName( name ) for name in self.axisNameList() ]


    def axisNameList(self):
        axisList = self._axisCont.listDatasets()
        return [ item[1] for item in axisList ]


    def axisIndexFromName(self, name):
        names = self.axisNameList()
        try: return names.index(name)
        except: raise UnknownAxis, "%r. Axes: %s" % (name, self.axisNameList())


    def axisFromId( self, number):
        return self._axisCont.datasetFromId( number)


    def axisFromName( self, name):
        return self._axisCont.datasetFromName( name)
        

    def data( self):
        return self._dataCont.datasetFromName( 'data')


    def errors( self):
        return self._dataCont.datasetFromName( 'error')


    def shape( self):
        return self._shape


    def size(self): return reduce(operator.mul, self.shape())


    def typeCode( self):
        """type code"""
        debug.log( 'Histogram %s: typecode = %s' % (self.getAttribute('name'), self._typeCode) )
        return self._typeCode
    

    def assign( self, value, count = 0):
        """assign( value, count=0) -> None
        Erase all elements of data and errors, then insert value into count
        elements of data and errors. If count is 0, uses current size.
        Input:
            value: the value to assign
            count: number of elements to end up with
        Output:
            None
        Exceptions: ValueError, TypeError"""
        data = self._data.storage()
        if count == 0:
            count = data.size()
        data.assign( count, value)
        errors = self._errors.storage()
        errors.assign( count, value)    
        return

    
    def indexes( self, coords ):
        """coordinations --> indexes
        (x,y,z,...) --> (index_x, index_y, index_z, ... )
        """
        indexes = []
        axisList = self._axisCont.listDatasets()
        for i,coord in enumerate(coords):
            axisId, axisName = axisList[i]
            #axis = self.axisFromId( i+1 ) #assumes axe ids are 1,2,3. take a look at __init__
            axis = self.axisFromName( axisName )
            indexes.append( axis.cellIndexFromValue( coord ) )
            continue
        return indexes


    #pickle interface    
    def __getstate__(self):
        attrs = {}
        for attrname in self.listAttributes():
            attrs[attrname] = self.getAttribute( attrname )
            continue
        name = self.name()
        axisCont = self._axisCont
        dataCont = self._dataCont
            
        return name, axisCont, dataCont, attrs
    

    def __setstate__(self, inputs):
        name, axisCont, dataCont, attrs = inputs
        data = dataCont.datasetFromName( "data" )
        errs = dataCont.datasetFromName( "error" )
        axes = [ axisCont.datasetFromId( item[0] ) for item in axisCont.listDatasets() ]
        ctor = Histogram.__init__
        ctor(self, name = name,
             unit = attrs['unit'],
             data = data,
             errors = errs,
             axes = axes,
             attributes = attrs,
             )
        return


    def __str__(self):
        title = "Histogram \"%s\"" %   self.name()

        axes = "- Axes:\n"
        for axisName in self.axisNameList():
            axis = self.axisFromName(axisName)
            axes += "   - Axis %s\n" % (axis,)
            continue

        shape = "- Shape: %s" % (self.shape(),)
        
        attrs = [ (name, self.getAttribute(name)) for name in \
                  self.listAttributes() ]
        meta = "- Metadata: %s" % (attrs,)
        data = "- Data: %s" % (self.data(),)
        errors = "- Errors: %s" % (self.errors(),)

        return '\n'.join( [title, axes, shape, meta, data, errors ] )


    def reduce(self):
        """reduce a histogram's dimension

        A histogram might has a dimension (or dimensions) that has
        only one bin. In that case, we could just remove that dimension.
        """

        ac = self._axisCont
        newAttrs = {}
        newShape = []
        for name in self.axisNameList():
            axis = self.axisFromName( name )
            if axis.size() == 1:
                newAttrs[ name ] = axis.binCenters()[0]
                ac.deleteDataset( name = name )
                pass
            else:
                newShape.append( axis.size() )
            continue

        newShape = tuple(newShape)
        for ds in self.datasets(): ds.setShape( newShape )

        for k, v in newAttrs.iteritems(): self.setAttribute( k, v )

        self._setShape( newShape )
        return


    def _getInpyarr(self): return self.data().storage().asNumarray()
    def _setInpyarr(self, rhs): self.data().storage().asNumarray()[:] = rhs
    I = property( _getInpyarr, _setInpyarr ) # "intensities" as numpy array
    

    def _getErr2npyarr(self):
        if self.errors(): return self.errors().storage().asNumarray()
        return 0
    def _setErr2npyarr(self, rhs):
        if self.errors() is None: raise "cannot set error because the histogram does not have error bars originally"
        self.errors().storage().asNumarray()[:] = rhs
        return
    E2 = property( _getErr2npyarr, _setErr2npyarr ) # square of error bars of "intensities"
    

    def _setShape(self, shape):
        self._shape = shape
        self._dimension = len(self._shape)
        return


    def _add_data_and_errors(self, data, errors ):
        #check sanity

        #1. check shape
        if errors is not None and data.shape() != errors.shape():
            msg = "Incompatible shapes between data (%s) and errors (%s)" % (
                data.shape(), errors.shape())
            raise IndexError, msg

        shape = tuple(self.__shapeFromAxes())
        dshape = tuple(data.shape())
        assert shape == dshape, \
            "shape mismatch: data shape %s, axes shape %s" % (
            dshape, shape )
        self._setShape( shape )

        #2. check type code
        if errors is not None and data.typecode() != errors.typecode():
            msg = "Incompatible type codes between data (%s) and errors (%s)" \
                  % (data.typecode(), errors.typecode())
            raise TypeError, msg
        self._typeCode = data.typecode()

        #3. check unit
        unit = tounit( self.unit() )
        dunit = tounit( data.unit() )
        eunit = dunit*dunit
        if errors: eunit = tounit( errors.unit() )
        if not _equalUnit( unit, dunit) or not _equalUnit( unit*unit, eunit ):
            msg = "Unit mismatch: histogram unit: %r, data unit: %r, "\
                  "errors unit: %r." % (
                unit, dunit, eunit )
            raise ValueError, msg

        self.addDataset( 'data', data )
        self.addDataset( 'error', errors )
        self._data = data; self._errors = errors
        return


    def _setunit(self, unit):
        self.setAttribute( 'unit', unit )
        self._data._setunit( unit )
        self._errors._setunit( unit*unit )
        return


    def _syncUnit(self):
        #synchronize histogram's unit to dataset's unit
        self.setAttribute( 'unit', self._data.unit() )
        return


    def __shapeFromAxes(self):
        return tuple( [ axis.size() for axis in self.axes() ] )

    pass # end of Histogram



class UnknownAxis(Exception): pass


epsilon = 1e-5
def _equalUnit( u1, u2 ):
    try: u1 + u2
    except Exception, err:
        return False
    try:
        diff = u1/u2-1
        return abs(diff) < epsilon
    except:
        try:
            diff = u2/u1-1
            return abs(diff) < epsilon
        except:
            return True
        raise "should not reach here"
    raise "should not reach here"


def _indexFromIndexes( indexes, shape ):
    res = indexes[0]
    for i, index in enumerate(indexes[1:]):
        res = res*shape[i+1] + index
        continue
    return res



def isNumberList( l ):
    return reduce(operator.and_, [isNumber(i) for i in l])


def isDSList( l ):
    return reduce(operator.and_, [isDataset(i) for i in l])


from DatasetBase import DatasetBase
def isDataset(ds):
    return isinstance(ds, DatasetBase)


from SlicingInfo import SlicingInfo
def isSlicingInfo( s ):
    return isinstance(s, SlicingInfo)


from _units import isNumberPair, isDimensionalPair, isDimensional, isNumber, tounit, isunitless

             
def isHistogram(h):
    return isinstance(h, Histogram)



def _makeSlicingInfos(s, dim):
    if len(s) == dim:
        return tuple([ _makeSlicingInfo( i ) for i in s ])
    if dim != 1:
        raise IndexError , "Dimension of slicing parameters does not match dimension of histogram: slice %s (dimension=%s), histogram dimension %s" % (s, len(s), dim)
    return _makeSlicingInfo( s ),


def _makeSlicingInfo( inputs ):
    if isinstance(inputs, SlicingInfo): return inputs
    try: return SlicingInfo( inputs )
    except: return inputs


def _slicingInfosFromDictionary( d, axes ):
    """
    for I(detID, pixID, tof)
    _slicingInfosFromDictionary( {'detID': (2,10), 'pixID': (3,7) } )
      --> SlicingInfo(2,10), SlicingInfo(3,7), SlicingInfo(front, back)
    """
    axisnames = [ axis.name() for axis in axes ]

    for n in d.keys():
        assert n in axisnames, "%s is not a valid axis. axes = %s" % (
            n, axisnames)
        
    ret = []
    for n in axisnames:
        i = d.get(n)
        if i is None: i = ()
        ret.append( i )
        continue

    return _makeSlicingInfos( ret, len(ret) )


def _short_list_str(l):
    if len(l) <  10: return str(l)
    else: return "[ %s, %s, ... %s, %s ]"%(l[0],l[1], l[-2], l[-1])


integer_typecodes = [
    24, 25,
    ]

float_typecodes = [
    5, 6,
    ]


def test_equalUnit():
    assert _equalUnit( 1, 2 ) == False
    assert _equalUnit( 1, 1 ) == True
    assert _equalUnit( 1, 1+1e-10 ) == True
    import _units as units
    meter = units.length.meter
    second = units.time.second
    assert _equalUnit( 1*meter, 1*meter ) == True
    assert _equalUnit( 1*meter, 1) == False
    assert _equalUnit( 1*meter, 1*second) == False
    assert _equalUnit( 1*meter, (1+1e-10)*meter) == True
    assert _equalUnit( 0*meter, 0*meter) == True
    assert _equalUnit( 0*meter, 1*meter) == False
    assert _equalUnit( 1*meter, 0*meter) == False
    return

def main():
    test_equalUnit()
    return


if __name__ == '__main__': main()

# version
__id__ = "$Id$"

# End of file
