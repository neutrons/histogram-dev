#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class HistogramContainer:

    def __init__(self):
        self._store = {}
        self._seq = []
        return


    def get(self, name):
        return self._store.get(name)


    def set(self, name, hist):
        if name in self._seq: self._store[name] = hist
        else: self.append( name, hist )
        return


    def delete(self, name):
        if name not in self._seq: raise ValueError , "%s not in this hitogram container" % name
        del self._seq[ self._seq.index(name) ]
        del self._store[ name ]
        return
    

    def append(self, name, hist):
        if name in self._seq :
            raise ValueError , "%s already in this histogram container" % name
        self._store[name] = hist
        self._seq.append( name )
        return


    def keys(self): return self._seq


    def assign(self, d):
        "assign myself with a dictionary of {name: histogram}"
        changed = False
        #remove everything not in 'd'
        for key in self.keys():
            if key not in d.keys():
                self.delete( key )
                changed = True
                pass
            continue
        #add new items in 'd'
        for key in d.keys():
            value = d[key]
            if key in self.keys():
                if value != self.get(key):
                    self.set(key, d[key])
                    changed = True
                    pass
                pass
            else:
                self.append( key, d[key] )
                changed = True
                pass
            continue
        return changed
            

    __getitem__ = get
    

    pass # end of HistogramContainer



# version
__id__ = "$Id$"

# End of file 
