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


from Branch import Branch
from Leaf import Leaf
from Dict import Dict
from Tuple import Tuple
from List import List
from Link import Link
from Construction import Construction
from Instance import Instance
from Global import Global
from Builtin import Builtin

import sys
from types import *
import copy_reg
import warnings

import journal
debug = journal.debug( "nx5.pickle" )


class Renderer:

    def __init__(self):
        return


    def render(self, obj):
        self.clean_up()
        return self.create_graph( obj )


    def clean_up(self):
        self.memo = {}
        self.pathstack = []
        self.curname = None
        return

        
    def create_graph(self, obj):
        debug.log( "now create graph for object %s" % (type(obj),) )
        
        # Check the memo
        x = self.memo.get(id(obj))
        if x:
            debug.log( "create Link for a %s" % (type(obj),) )
            return Link( self._get_name( obj ), x[0] )

        t = type(obj)
        f = self.dispatch.get(t)
        if f :
            debug.log( "call %s for a %s" % (f, type(obj)) )
            return f(self, obj)
        
        # Check for a class with a custom metaclass; treat as regular class
        try:
            issc = issubclass(t, TypeType)
        except TypeError: # t is not a class (old Boost; see SF #502085)
            issc = 0
        if issc:
            debug.log( "call on_global for a %s" % obj.__class.__name__ )
            return self.on_global(obj)

        # Check copy_reg.dispatch_table
        reduce = copy_reg.dispatch_table.get(t)
        if reduce:
            rv = reduce(obj)
        else:
            # Check for a __reduce_ex__ method, fall back to __reduce__
            reduce = getattr(obj, "__reduce_ex__", None)
            if reduce:
                rv = reduce()
            else:
                reduce = getattr(obj, "__reduce__", None)
                if reduce:
                    rv = reduce()
                else:
                    raise PicklingError("Can't pickle %r object: %r" %
                                        (t.__name__, obj))

        # Check for string returned by reduce(), meaning "save as global"
        if type(rv) is StringType:
            return self.on_global(obj, rv)

        # Assert that reduce() returned a tuple
        if type(rv) is not TupleType:
            raise PicklingError("%s must return string or tuple" % reduce)

        # Assert that it returned an appropriately sized tuple
        l = len(rv)
        if not (2 <= l <= 5):
            raise PicklingError("Tuple returned by %s must have "
                                "two to five elements" % reduce)

        # Save the reduce() output and finally memoize the object
        return self.on_reduce(obj=obj, *rv)
    

    def memoize(self, obj, name):
        """Store an object in the memo."""
        assert id(obj) not in self.memo
        curpath = '/'.join( self.pathstack + [name] )
        self.memo[id(obj)] = curpath, obj
        return


    def on_reduce(self, func, args, state=None,
                  listitems=None, dictitems=None, obj=None):
        # This API is called by some subclasses

        # Assert that args is a tuple or None
        if not isinstance(args, TupleType):
            if args is None:
                # A hack for Jim Fulton's ExtensionClass, now deprecated.
                # See load_reduce()
                warnings.warn("__basicnew__ special case is deprecated",
                              DeprecationWarning)
            else:
                raise PicklingError(
                    "args from reduce() should be a tuple")

        # Assert that func is callable
        if not callable(func):
            raise PicklingError("func from reduce should be callable")


        if  getattr(func, "__name__", "") == "__newobj__":
            # A __reduce__ implementation can direct protocol 2 to
            # use the more efficient NEWOBJ opcode, while still
            # allowing protocol 0 and 1 to work normally.  For this to
            # work, the function returned by __reduce__ should be
            # called __newobj__, and its first argument should be a
            # new-style class.  The implementation for __newobj__
            # should be as follows, although pickle has no way to
            # verify this:
            #
            # def __newobj__(cls, *args):
            #     return cls.__new__(cls, *args)
            #
            # Protocols 0 and 1 will pickle a reference to __newobj__,
            # while protocol 2 (and above) will pickle a reference to
            # cls, the remaining args tuple, and the NEWOBJ code,
            # which calls cls.__new__(cls, *args) at unpickling time
            # (see load_newobj below).  If __reduce__ returns a
            # three-tuple, the state from the third tuple item will be
            # pickled regardless of the protocol, calling __setstate__
            # at unpickling time (see load_build below).
            #
            # Note that no standard __newobj__ implementation exists;
            # you have to provide your own.  This is to enforce
            # compatibility with Python 2.2 (pickles written using
            # protocol 0 or 1 in Python 2.3 should be unpicklable by
            # Python 2.2).
            cls = args[0]
            if not hasattr(cls, "__new__"):
                raise PicklingError(
                    "args[0] from __newobj__ args has no __new__")
            if obj is not None and cls is not obj.__class__:
                raise PicklingError(
                    "args[0] from __newobj__ args has the wrong class")
            args = args[1:]
            constructor = cls
        else:
            constructor = func


        name = self._get_name(obj)
        return self._on_obj( obj, name, constructor, args, state,
                             listitems, dictitems )


    dispatch = {}

    def on_inst(self, obj):
        name = self._get_name(obj)

        if hasattr(obj, '__getinitargs__'):
            args = obj.__getinitargs__()
            len(args) # XXX Assert it's a sequence
            _keep_alive(args, memo)
        else:
            args = ()
            pass

        ctor = obj.__class__

        #state is obtained from getstate method or instance dictionary
        try:
            getstate = obj.__getstate__
        except AttributeError:
            stuff = obj.__dict__
        else:
            stuff = getstate()
            _keep_alive(stuff, memo)

        return self._on_obj( obj, name, ctor, args, stuff )
    dispatch[ InstanceType ] = on_inst


    def on_global(self, obj, name=None):
        memo = self.memo

        if name is None:
            name = obj.__name__

        module = getattr(obj, "__module__", None)
        if module is None:
            module = whichmodule(obj, name)

        try:
            __import__(module)
            mod = sys.modules[module]
            klass = getattr(mod, name)
        except (ImportError, KeyError, AttributeError):
            raise PicklingError(
                "Can't pickle %r: it's not found as %s.%s" %
                (obj, module, name))
        else:
            if klass is not obj:
                raise PicklingError(
                    "Can't pickle %r: it's not the same object as %s.%s" %
                    (obj, module, name))
            pass
        
        self.memoize(obj, name)
        return Global( name, module )

    dispatch[ClassType] = on_global
    dispatch[FunctionType] = on_global
    dispatch[BuiltinFunctionType] = on_global
    dispatch[TypeType] = on_global


    def on_tuple(self, obj):
        name = self._get_name( obj )
        pathstack = self.pathstack
        rt = Tuple(name)
        self.memoize( obj, name )

        pathstack.append(name)
        for element in obj:
            rt.addLeaf( self.create_graph(element) )
            continue
        pathstack.pop()

        return rt
    dispatch[TupleType] = on_tuple


    def on_list(self, obj):
        name = self._get_name( obj )
        pathstack = self.pathstack
        rt = List(name)
        self.memoize( obj, name )
        
        pathstack.append(name)
        for element in obj:
            rt.addLeaf( self.create_graph(element) )
            continue
        pathstack.pop()

        return rt
    dispatch[ListType] = on_list


    def on_dict(self, obj):
        name = self._get_name( obj )
        pathstack = self.pathstack
        rt = Dict(name)
        self.memoize( obj, name )
        
        pathstack.append(name)
        for k,v in obj.iteritems():
            rt.addLeaf( self.create_graph( (k,v) ) )
        pathstack.pop()

        return rt
    dispatch[DictionaryType] = on_dict


    def on_builtin(self, builtin):
        return Builtin( self._get_name( builtin ), builtin )
    dispatch[NoneType] \
                       = dispatch[bool] \
                       = dispatch[IntType] \
                       = dispatch[LongType] \
                       = dispatch[FloatType] \
                       = dispatch[StringType] \
                       = dispatch[UnicodeType] \
                       = on_builtin


    def _on_obj(self, obj, name, constructor, args,
                state = None, listitems = None, dictitems = None):
        memo  = self.memo
        create_graph = self.create_graph
        pathstack = self.pathstack
        
        node = Instance( name )

        self.memoize( obj, name )

        #prepare to go deeper in hierarchy
        pathstack.append( name )

        #constructor and args
        construction = Construction( 'construction' )
        pathstack.append( construction.name )

        self.curname = "ctor"
        construction.addLeaf( create_graph( constructor ) )
        self.curname = "args"
        construction.addLeaf( create_graph( args ) )

        pathstack.pop()

        node.addLeaf( construction )

        #create a group to save state
        self.curname = "state"
        state_g = create_graph( state )
        
        #add the state_group to representation of this python
        #instance
        node.addLeaf( state_g )


        # More new special cases (that work with older protocols as
        # well): when __reduce__ returns a tuple with 4 or 5 items,
        # the 4th and 5th item should be iterators that provide list
        # items and dict items (as (key, value) tuples), or None.
        #add listitems and dictitems if necessary
        if listitems is not None:
            self.curname = "listitems"
            node.addLeaf( create_graph( listitems ) )
            pass

        if dictitems is not None:
            self.curname = "dictitems"
            node.addLeaf( create_graph( dictitems ) )
            pass

        pathstack.pop()

        # save a reference in the node. This makes sure that we
        # don't lost the original instance. This could be
        # useful if the default break down of an instance
        # is no good.
        node.instance = obj
        return node


    def _get_name(self, obj):
        
        if self.curname:
            
            rt = self.curname
            
        elif hasattr( obj, 'name'):
            
            try: rt = obj.name()
            except Exception, msg:
                debug.log( "%s:%s" % (msg.__class__.__name__, msg) )
                
                try: rt = obj.__name__
                except Exception, msg: rt = obj.name
                
                pass
            pass
        else:
            rt = uniqueName(obj.__class__.__name__)
            pass
            
        if not isinstance(rt, str):
            msg = "%s is not a string!" % rt
            msg += "\n obj=%s, class=%s, curname=%s" % (obj, type(obj), self.curname)
            debug.log( "%s: %s" % (ValueError, msg) )
            pass

        self.curname = None #curname is a temporary variable. should be set to None.
        return rt


    pass # end of Renderer


from pickle import whichmodule, PicklingError

#helpers

#copied from pickle.py
def _keep_alive(x, memo):
    """Keeps a reference to the object x in the memo.

    Because we remember objects by their id, we have
    to assure that possibly temporary objects are kept
    alive by referencing them.
    We store a reference at the id of the memo, which should
    normally not be used unless someone tries to deepcopy
    the memo itself...
    """
    try:
        memo[id(memo)].append(x)
    except KeyError:
        # aha, this is the first one :-)
        memo[id(memo)]=[x]



_uniqueID = 0
def uniqueID():
    global _uniqueID
    _uniqueID += 1
    return _uniqueID

def uniqueName( type ):
    return "%s%d" % (type, uniqueID())


from testobject import testobject

def test():
    a = testobject()
    graph = Renderer().render( a )
    
    from Printer import Printer
    print '\n'.join( Printer().render( graph ) )
    return



if __name__ == "__main__": test()


# version
__id__ = "$Id$"

# End of file 
