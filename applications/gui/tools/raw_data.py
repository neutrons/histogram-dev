
def ExtractHistograms( environ ):
    _startApp( "wxExtractHistogramsFromINSMeasurement.py", environ )
    return


def loadPharosIdpt( environ ):
    try:
        from measurement.ins import createPharosRun
    except ImportError , err:
        new = "This feature needs the 'measurement' package"
        raise ImportError, "%s: %s. \n ** %s" % (
            err.__class__.__name__, err, new )

    controller = environ['controller']
    toolkit = controller.toolkit
    view = controller.view

    parent = None #hack
    
    detdef = toolkit.loadfileDialog(parent, "Please locate PHAROS detector definition file" )
    
    datafile = toolkit.loadfileDialog(parent, "Please locate PHAROS data file" )

    run = createPharosRun( detdef, datafile )
    ret = run.getDetPixTOFData()

    environ.update( {'I_detpixtof': ret} )
    controller = environ['controller']
    controller.addNewHistogram( 'I_detpixtof', ret )
    return 
        
    
    
def loadLrmecsIdpt( environ ):
    try:
        from measurement.ins import createLrmecsRun
    except ImportError , err:
        new = "This feature needs the 'measurement' package"
        raise ImportError, "%s: %s. \n ** %s" % (
            err.__class__.__name__, err, new )

    controller = environ['controller']
    toolkit = controller.toolkit
    view = controller.view

    parent = None #hack
    
    datafile = toolkit.loadfileDialog(parent, "Please locate LRMECS data file" )

    run = createLrmecsRun( datafile )
    ret = run.getDetPixTOFData()

    environ.update( {'I_detpixtof': ret} )
    controller = environ['controller']
    controller.addNewHistogram( 'I_detpixtof', ret )

    ret = ret.sum('pixelID')

    environ.update( {'I_dettof': ret} )
    controller.addNewHistogram( 'I_dettof', ret )
    return 

    
    
from WebAppTools import *


def Web_ExtractHistograms( environ ):
    app = "ExtractHistogramsFromINSMeasurement"
    StartWebApplication( app, environ )
    return


def _startApp( app, environ ):
    thread = _PyreAppThread(app)

    controller = environ['controller']
    controller.threads.append( thread )
    thread.start()
    return



from threading import Thread as _Thread
class _PyreAppThread( _Thread ):

    def __init__(self, pyreexecutable):
        _Thread.__init__(self)
        self.pyreexe = pyreexecutable
        return


    def run(self):
        from pyregui.launchers.spawn import spawn
        from pyregui.utils import findExecutable
        pexe = findExecutable( self.pyreexe )
        spawn( pexe )
        return



__export__ = [
    ("Load histogram from a PHAROS experimental run", loadPharosIdpt),
    ("Load histogram from a LRMECS experimental run", loadLrmecsIdpt),
    #('Extract histograms (usual suspects) from raw data', ExtractHistograms),
    #('Extract histograms (usual suspects) from raw data: Web Edition', Web_ExtractHistograms),
    #('Get Extracted Histograms from Web', GetFilesFromComputingServer),
    ]
