#!/usr/bin/env python
# Jiao Lin Copyright (c) 2005 All rights reserved


from AxisMapper import AxisMapper

class DiscreteAxisMapper(AxisMapper):

    """
    map a value in an Axis to a index 
    """

    def __init__(self, mapdict):
        self._map = mapdict

    def __call__(self, value):
        try: return self._map[value]
        except KeyError :
            for key in self._map.iterkeys():
                if key == value: return self._map[key]
                continue
            raise IndexError , "Cannot map %s to index" % (value,)
        except TypeError : raise IndexError , "Cannot map %s to index" % (value,)

    pass # end of DiscreteAxisMapper
    
