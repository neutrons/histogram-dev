#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class SlicingInfo:


    def __init__(self, inputs ):
        """
        SlicingInfo( (3.0, 5.5) )
        SlicingInfo( (,) )
        SlicingInfo( (1,99) )
        SlicingInfo( SlicingInfo( (3,5) ) )
        SlicingInfo( front, 33 )
        """
        
        #convert inputs from list to tuple
        if isinstance(inputs, list): inputs = tuple(inputs)
        
        #tuple
        if isinstance(inputs, tuple):
            if len(inputs)==0: 
                #inputs is (,)
                self.start, self.end = front, back
            elif len(inputs)==2:
                #inputs is (a,b)
                start, end = inputs
                if start is None: start = front
                if end is None: end = back
                self.start = start; self.end = end
            else:
                #unknown inputs
                raise ValueError , "Don't know how to get slicing info from %s" % (inputs,)
            
        elif isinstance(inputs, SlicingInfo):
            #copy ctor
            self.start, self.end = inputs.start, inputs.end
            
        else:
            #unknown inputs
            raise ValueError , "Don't know how to get slicing info from %s" % (inputs,)
        return


    def __str__(self):
        return "%s:%s" % (self.start, self.end)


    __repr__ = __str__


    class SpecialPosition:

        def __init__(self, name):
            self.name = name
            return


        def __str__(self): return "%s" % self.name

        pass # end of SpecialPosition


    pass # end of SlicingInfo


front = SlicingInfo.SpecialPosition( "front" )
back = SlicingInfo.SpecialPosition( "back" )
all = SlicingInfo( (front, back) )


# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Sat Jul  8 08:20:17 2006

# End of file 
