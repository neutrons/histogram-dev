def usecolormap( filename, name = None ):
    if name is None:
        import os
        name = os.path.splitext( filename )[0]
        pass
    mymap = makecolormap( filename, name )
    import pylab
    #pylab.rc( 'image', cmap = name )
    gci = pylab.gci()
    gci.set_cmap( mymap )
    return

use = usecolormap
    

def makecolormap( filename, name = 'mycolormap' ):
    d = makecolordict( filename )
    import matplotlib as mp
    return mp.colors.LinearSegmentedColormap(name, d, 256)

        
def makecolordict( filename ):
    lines = open(filename).readlines()
    line2rgb = lambda line: [ eval(x) for x in line.split() ]
    colors = [ line2rgb(line) for line in lines ]
    colors = filter( lambda color: len(color)==3, colors )
    
    n = len(colors)
    red = []; green = []; blue = []
    for i, color in enumerate( colors ):
        x = 1. * i/(n-1)
        c = float(color[0])/255; red.append( (x, c, c) )
        c = float(color[1])/255; green.append( (x, c, c) )
        c = float(color[2])/255; blue.append( (x, c, c) )
        continue

    return {
        'red': red,
        'green': green,
        'blue': blue,
        }


