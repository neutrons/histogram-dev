import nx5
import os
nx5path = os.path.split(nx5.__file__)[0]
etcpath = os.path.join( nx5path, "..", "..", "etc"  )
nexmlpath = os.path.join( etcpath, "hdf_pickle" )
nexmlpath = os.path.abspath( nexmlpath )
