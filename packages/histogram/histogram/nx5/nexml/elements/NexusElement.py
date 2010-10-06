# (c) 2003 T. M. Kelley California Institute of Technology

mod_string = "nexus.nexml.elements.NexusElement"

class NexusElement(object):

    def attributes(self):
        return self._attributes


    def className(self):
        return self._className


    def getAttribute( self, name):
        return self._attributes[name]


    def identify(self, inspector):
        msg = "class '%s' must override 'identify'" % self.__class__.__name__
        raise NotImplementedError, msg

##     def id( self, inspector):
##         print "Deprecated: use identify"
##         return self.identify( inspector)


    def isDataset( self):
        msg = "class %s must override isDataset" % self.__class__.__name__
        raise NotImplementedError, msg


    def isGroup( self):
        msg = "class %s must override isGroup" % self.__class__.__name__
        raise NotImplementedError, msg


    def name(self):
        try:
            return self._attributes['name']
        except KeyError:
            print "node class: %s" % self.__class__.__name__
            print "attributes: %s" % str( self._attributes)
            print "path: %s" % self.path()
            raise

    def NXpath(self):
        return self._NXpath


    def path( self):
        return self._pathstr


    def setAttributes( self, attrDict):
        """1 arg: dictionary of name:value pairs for attributes"""
        if type(attrDict) is not dict:
            raise TypeError, "argument must be a dictionary"
        self._attributes.update(attrDict)
        return


    def __init__(self, name, className, NXpath=None, pathstr = ''):
        self._className = className
        self._NXpath = NXpath
        self._pathstr = pathstr
        self._attributes = {}
        self._attributes['name'] = name
        return


    def _compare(self, otherNexusElement, verbose=0):
        """Compare name, classname, NXpath, path, and attributes"""
        other = otherNexusElement
        same = True
        if self.name() != other.name():
            same = False
            if verbose:
                print mod_string+".compare():"
                print "names differ. self:",self.name(),"; other:",other.name()
        if self._className != other.className():
            same = False
            if verbose:
                print mod_string+".compare():"
                print "class names differ. self:",self._className,\
                      "; other:",other.className()
        try:
            if self._NXpath.compare(other.NXpath(), verbose) == 0:
                same = False
                if verbose:
                    print mod_string+".compare():"
                    print "paths differ. self:"
                    print self._NXpath.asString()
                    print "other:"
                    print other.NXpath().asString()
        except AttributeError:
            if self._NXpath is None:
                if other.NXpath() is not None:
                    same = False
            else:
                raise TypeError, 'Unable to compare paths'
##         from nexus.Helpers import dictComp
##         sameAtts = dictComp(self._attributes, other.attributes())

        if self._pathstr != other.path():
            same = False
            if verbose:
                print mod_string+".compare() paths differ: "
                print "self._path = %s" % self._path
                print "other.path() = %s" % other.path()
        sameAtts = self._compareAttributes( other, verbose)[0]

        same = same and sameAtts
        if verbose:
            print "nexus.nexml.elements.NexusElement._compare(): same =",same
        return same




    def _compareAttributes( self, other, verbose = False):
        """Compare attribute dictionaries"""
        
        myAttrs = self.attributes()
        otherAttrs = other.attributes()

        if len(myAttrs) != len(otherAttrs):
            if verbose:
                print "Different number of attributes: " + str((len(myAttrs), len(otherAttrs)))
            return False, [], []

        myKeys, myVals = myAttrs.keys(), myAttrs.values()
        otherKeys, otherVals = otherAttrs.keys(), otherAttrs.values()

        passed = True

        mismatchedKeys = []
        mismatchedVals = []

        for i,key in enumerate(myKeys):
            if key != otherKeys[i]:
                passed = False
                mismatchedKeys.append( (i, key, otherKeys[i]))
                if verbose:
                    print "attr key mismatch: " + str( (i, key, otherKeys[i]))
            elif myAttrs[key] != otherAttrs[key]:
                passed = False
                mismatchedVals.append( ( key, myAttrs[key], otherAttrs[key]))
                if verbose:
                    print "attr val mismatch: "+str( ( key, myAttrs[key], otherAttrs[key]))
                
        return passed, mismatchedKeys, mismatchedVals



# version
__id__ = "$Id: NexusElement.py 98 2005-08-02 19:37:56Z tim $"

# End of file
