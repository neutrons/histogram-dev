#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from types import *
import sys


import journal
debug = journal.debug( 'nx5.pickle' )


class Renderer:


    def __init__(self):
        return
    

    def render(self, objHierarchy):
        self.clean_up()
        return objHierarchy.identify(self)


    def clean_up(self):
        self.memo = {}
        self.pathstack = []
        return


    def memoize(self, pathstack, obj):
        """Store an object in the memo."""
        path = '/'.join(pathstack)
        self.memo[path] = obj
        return


    def onInstance(self, instance):
        self.pathstack.append( instance.name )
        construction, state = instance.leaves

        inst = construction.identify(self)
        self.memoize( self.pathstack, inst )
        state = state.identify(self)

        debug.log( "state is %s" % (state,) )
        try: setstate = getattr(inst, '__setstate__')
        except: setstate = None
            
        if setstate:
            try: setstate( state ); self.pathstack.pop(); return inst
            except Exception, err:
                msg = "Unable to set state %s of instance %s. %s: %s" % (
                    state, instance.name, err.__class__.__name__, err)
                raise RuntimeError , msg
        
        slotstate = None
        if isinstance(state, tuple) and len(state) == 2:
            state, slotstate = state
        if state:
            try:
                inst.__dict__.update(state)
            except RuntimeError:
                # XXX In restricted execution, the instance's __dict__
                # is not accessible.  Use the old way of unpickling
                # the instance variables.  This is a semantic
                # difference when unpickling in restricted
                # vs. unrestricted modes.
                # Note, however, that cPickle has never tried to do the
                # .update() business, and always uses
                #     PyObject_SetItem(inst.__dict__, key, value) in a
                # loop over state.items().
                for k, v in state.items():
                    setattr(inst, k, v)
        if slotstate:
            for k, v in slotstate.items():
                setattr(inst, k, v)
                continue
            pass
        self.pathstack.pop()
        return inst


    def onConstruction(self, construction):
        constructor, args = construction.leaves

        self.pathstack.append( construction.name )
        
        ctor = constructor.identify(self)
        args = args.identify(self)

        instantiated = 0
        if (not args and
                type(ctor) is ClassType and
                not hasattr(ctor, "__getinitargs__")):
            try:
                value = _EmptyClass()
                value.__class__ = ctor
                instantiated = 1
            except RuntimeError:
                # In restricted execution, assignment to inst.__class__ is
                # prohibited
                pass
        if not instantiated:
            try:
                value = ctor(*args)
            except TypeError, err:
                raise TypeError, "in constructor for %s: %s" % (
                    ctor.__name__, str(err)), sys.exc_info()[2]
            pass
        debug.log( 'ctor = %s, args = %s' % (ctor, args ) )
        self.pathstack.pop()
        return value


    def onTuple(self, t):
        contents = t.leaves
        self.pathstack.append( t.name )
        rt = []
        self.memoize( self.pathstack, rt )
        for item in contents: rt.append( item.identify(self) )
        rt = tuple(rt)
        self.memoize( self.pathstack, rt )
        self.pathstack.pop()
        return rt


    def onList(self, l):
        contents = l.leaves
        self.pathstack.append(l.name)
        rt = []
        self.memoize( self.pathstack, rt )
        for item in contents: rt.append( item.identify(self) )
        self.memoize( self.pathstack, rt )
        self.pathstack.pop()
        return rt


    def onDict(self, d):
        self.pathstack.append( d.name )
        rt = {}
        self.memoize( self.pathstack, rt )
        for leaf in d.leaves:
            k,v = leaf.identify(self)
            rt[k] = v
            continue
        self.memoize( self.pathstack, rt )
        self.pathstack.pop()
        return rt


    def onGlobal(self, g):
        module = g.data
        name = g.name
        klass = self.findClass(module, name)
        self.pathstack.append( name )
        self.memoize( self.pathstack, klass )
        self.pathstack.pop()
        return klass


    def onBuiltin(self, b):
        rt = b.data
        name = b.name
        self.pathstack.append( name )
        self.memoize( self.pathstack, rt )
        self.pathstack.pop()
        return rt


    def onLink(self, link):
        return self._getLinkedObject( link.data )
        

    def findClass(self, module, name):
        # Subclasses may override this
        __import__(module)
        mod = sys.modules[module]
        klass = getattr(mod, name)
        return klass


    def _getLinkedObject(self, link):
        memo = self.memo
        rt = memo.get( link )
        if rt is not None: return rt
        rt = memo.get( '/' + link )
        if rt is not None: return rt
        raise ValueError, "Cannot resolve link %s in memo %s" % (link, memo)

    pass # end of Renderer


class _EmptyClass:
    pass



def test():
    debug.activate()
    from ObjectHierarchyFromObject import Renderer as O2OH, testobject
    a = testobject()
    graph = O2OH().render( a )
    
    from Printer import Printer
    print '\n'.join( Printer().render( graph ) )

    b = Renderer().render( graph )
    print b
    for k in dir(b): print k, getattr(b, k)
    return



if __name__ == "__main__": test()


# version
__id__ = "$Id$"

# End of file 
