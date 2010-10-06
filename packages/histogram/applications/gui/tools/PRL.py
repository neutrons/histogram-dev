def TexInstalled():
    "test whether tex is usable"
    import pylab
    pylab.rcParams['text.usetex'] = 1
    pylab.rcParams['backend'] = 'ps'
    try:
        pylab.plot( [1,2,3])
        pylab.xlabel( '$\alpha$' )
        import tempfile
        pylab.savefig( tempfile.mktemp() )
    except:
        print 'latex not installed'
        return 0
    return 1



def S_QE(environ):
    '''
    A nice plot of S(Q,E)

    After loading a sqehist.pkl file, run the following 
    command will give you a very nice plot ready to
    be sent to PRL :)
    '''

    import pylab
    
    #change color palette
    pylab.hot()
    
    #show color bar
    pylab.colorbar()
    
    #change axis limits
    pylab.xlim(0,10)
    pylab.ylim(-50, 50)
    
    #use latex
    pylab.rcParams['text.usetex'] = TexInstalled()
    
    #change labels, title
    pylab.xlabel( r"$Q {\rm(\AA^{-1})}$" )
    pylab.ylabel( r"$E {\rm(eV)}$" )
    pylab.title( r"$S(Q,E)$" )
    
    #save picture
    pylab.savefig( "sqe.png" )
    return



def diffraction_pattern(environ):
    '''
    Get diffraction pattern
    
    After loading a spehist.pkl file (Please note this time 
    we are working on "spehist.pkl" instead of "sqehist.pkl"),
    '''
    import pylab
    SPhiEData = environ['SPhiEData']
    sliced = SPhiEData[ (4,120), (-5,5) ]
    i_phi = sliced.sum( 'energy' )
    
    environ.update( {'i_phi': i_phi} )
    controller = environ['controller']
    controller.addNewHistogram( 'i_phi', i_phi )
    
    pylab.rcParams['text.usetex'] = TexInstalled()
    pylab.xlabel( r"$\phi {\rm (deg)}$" )
    pylab.ylabel( r"Intensity" )
    pylab.title( r"Diffraction pattern" )
    pylab.savefig( "diffraction_pattern.png" )
    return


__export__ = [
    ('S(Q,E)', S_QE),
    ('Diffraction pattern from S(phi,E)', diffraction_pattern),
    ]
