# NeXus status flags
NX_OK = 1
NX_EOD = -1
NX_ERROR = 0

# NeXus data types
# codes to string:
nx_types = { 4:'NX_CHAR', 5:'NX_FLOAT32',  6:'NX_FLOAT64', 20:'NX_INT8',\
            21:'NX_UINT8', 22:'NX_INT16', 23:'NX_UINT16', 24:'NX_INT32',\
            25:'NX_UINT32'}

# string to code
NX_CHAR    =  4
NX_FLOAT32 =  5
NX_FLOAT64 =  6
NX_INT8    = 20
NX_UINT8   = 21
NX_INT16   = 22
NX_UINT16  = 23
NX_INT32   = 24
NX_UINT32  = 25

# NeXus/HDF compression codes
NX_COMP_NONE = 100
NX_COMP_LZW  = 200
NX_COMP_RLE  = 300
NX_COMP_HUF  = 400

NX_UNLIMITED = -1

NX4_GROUP = 1965
NX5_GROUP = 1000000
