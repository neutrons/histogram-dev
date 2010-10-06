# (c) 2003 T. M. Kelley, California Institute of Technology

class NXpath(object):

    def root(self): return self._root

    def path(self): return self._path

    def leaf(self): return self._leaf

    def asString(self):
        if self._simple:
            return '/'.join( self._path)
        else:
            outstr = '/' + '/'.join( [pathEl[1] for pathEl in self._path])
            outstr += '/' + self._leaf[1]
            return outstr
        # end
        

    def compare(self, otherPath, verbose=0):
        same = 1
        if self._root != otherPath.root(): same *= 0
        if self._path != otherPath.path(): same *= 0
        if self._leaf != otherPath.leaf(): same *= 0
        if verbose:
            print "nexus.NXpath.compare(): same =",same
        return same
    
    def __init__(self, NXstack, **kwds):
        # Each element of the stack is expected to consist of
        # ( 'nexus' | 'Group' | 'Dataset', {'name':<name>[, 'class':<class>]})
        # Example: ( 'Group', {'name':'Pharos', 'class':'NXinstrument'})
        
        self._path = []
        if 'nostack' in kwds.keys():
            self._simple = True
            self._root = ''
            self._path = NXstack.split('/')
            self._leaf = ''
        else:
            self._simple = False
            for pathElement in NXstack:
                if (pathElement[0] == 'nexus'):
                    self._root = ( 'nexus', pathElement[1]['name'],\
                                   pathElement[1]['class'])
                elif (pathElement[0] == 'Group'):
                    self._path.append(('Group', pathElement[1]['name'],\
                                       pathElement[1]['class']))
                elif pathElement[0] == 'Dataset':
                    self._leaf = ('Dataset',pathElement[1]['name'])
                else:
                    raise ValueError,"Unrecognized path element"
        return


#version
__id__ = "$Id: NXpath.py 13 2005-02-03 01:09:28Z tim $"

# End of file
