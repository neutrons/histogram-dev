
def builtin2storage(  type, v  ):
    """create storage from a value of a python builtin

    v --> storage of v
    """
    raise NotImplementedError

from stdVector import vector

def builtin2storage( type, v ):
    if type in ['string', 'char']: return vector( type, v )
    return vector( type, [v] )



import os
from nexmlpath import nexmlpath


storage_nexml = os.path.join( nexmlpath, "vector.nexml" )

from stdVector.StdVector import StdVector
storage_type = StdVector

storage_type_name = '.'.join( [storage_type.__module__ , storage_type.__name__ ] )
