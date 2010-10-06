#!/usr/bin/env python
# Copyright (c) 2004 T. M. Kelley

from NexusElement import NexusElement

import journal

debug = journal.debug("nexml.Group")

class Group(NexusElement):
    """Group( name, className, parent) """
        
    def identify(self, inspector):
        return inspector.onGroup(self)


    def addChild( self, child):
        self._children[ child.name()] = child
        self._sorted.append( child.name() )
        if issubclass( child.__class__, Group):
            self._subgroups.append( child)
        return
            

    def getChild( self, name):
        """getChild(name) -> Node: return child with name"""
        try:
            node = self._children[name]
        except KeyError:
##             node = None
            raise KeyError, "no child named %s in this Group" % name
        return node
    

    def children(self):
        children = self._children
        t = [ children[ n ] for n in self._sorted ]
        return tuple(t)


    def subgroups(self):
        return tuple(self._subgroups)


    def update( self, children, subgroups, sorted = None):
        """group.update( children, subgroups) -> None
        Update the group with a dictionary of children and a list of
        which children happen to be subgroups.
        """
        for subgroup in subgroups:
            if subgroup not in self._subgroups:
                self._subgroups.append(subgroup)

        self._children.update( children)

        m_sorted = self._sorted
        if sorted is None: sorted = children.keys()
        for child in sorted:
            if child in m_sorted : continue
            m_sorted.append( child )
            continue
        self._sorted = m_sorted

        return
        

    def isDataset( self):
        return False


    def isGroup( self):
        return True


    def __init__(self, name, className, NXpath, pathstr):
        NexusElement.__init__(self, name, className, NXpath, pathstr)
        self._children = {}
        self._sorted = []
        self._subgroups = []
        return


    def _compare( self, other, verbose = False):
        # compare name, classname, NXpath, path, and attributes
        baseSame = NexusElement._compare( self, other, verbose)
        same = baseSame

        # compare children
        mychildren = self.children()
        otherschildren = other.children()
        same = same and ( len(mychildren) == len(otherschildren))
        if not same:
            if verbose:
                print "Group.compare: different  number of children"
                print "this object's (%s) children: %s" %(self.name(), len(mychildren))
                print "other object's (%s) children: %s" % \
                      ( other.name(), len(otherschildren))
        for mychild in mychildren:
            for otherschild in otherschildren:
                if otherschild.name() == mychild.name():
                    same = same and mychild._compare( otherschild, verbose )
                    break
                continue
            continue

        return same

#End of class Group(...

# version
__id__ = "$Id: Group.py 123 2007-03-24 05:09:30Z linjiao $"

# End of file
