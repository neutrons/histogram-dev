from WebAppTools import *
def Web_GetDOS( environ ):
    app = "GetDOS"
    StartWebApplication( app, environ )
    return


def Web_LrmecsReductionApp( environ ):
    app = "LrmecsReductionApp"
    StartWebApplication( app, environ )
    return


def Web_PharosReductionApp( environ ):
    app = "PharosReductionApp"
    StartWebApplication( app, environ )
    return




def GetDOS( environ ):
    _startApp( 'wxGetDOS.py', environ )
    return


def LRMECS( environ ):
    exe = "wxLrmecsReductionApp.py"
    _startApp( exe, environ )
    return


def PHAROS( environ ):
    exe = "wxPharosReductionApp.py"
    _startApp( exe, environ )
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
    ('LRMECS Reduction', LRMECS),
    ('LRMECS Reduction: Web Edition (Need ssh tunneling)', Web_LrmecsReductionApp),
    ('PHAROS Reduction', PHAROS),
    ('PHAROS Reduction: Web Edition (Need ssh tunneling)', Web_PharosReductionApp),
    ('Compute DOS from S(Q,E)', GetDOS),
    ('Compute DOS from S(Q,E): Web Edition (Need ssh tunneling)', Web_GetDOS),
    ]
