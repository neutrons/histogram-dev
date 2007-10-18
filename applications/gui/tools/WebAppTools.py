#computingServer = "upgrayedd.danse.us"
#computingServer = "arcscluster.caltech.edu"
computingServer = "sbo"
localproxy = "http://localhost:8888/pyreapp"
localproxy = "http://localhost:5001/pyreapp" # for test


menutext_retrieve_files = "Retrieve results of web application (needs ssh tunneling to computing cluster)"

def StartWebApplication( app,  environ ):
    link = "%s/%s" % (localproxy, app)
    
    controller = environ['controller']
    toolkit = controller.toolkit
    view = controller.view

    message = """This will start the web applicatoin of %s. A browser will pop up and please follow instructions there to run the web application.

    The web application runs on the data analysis server, not your local machine. To retrieve results of a web application, please come back here when you are done with your web application, and select the menu 'Tools->Web->%s'.
    """ % (app, menutext_retrieve_files )
    parent = None #hack
    toolkit.messageDialog(parent, "Note", message)

    import webbrowser
    webbrowser.open( link )
    return


def GetFilesFromComputingServer( environ ):
    message = """This starts the procedure of retrieving results of a web application that has been run on the data analysis server. I will copy those files to a local directory in your machine. When you hit <enter>, a dialog will pop up for you to choose the local directory to which those data files will be copied, and then a dialog will pop up to ask you to input the link in your web browser when your web application successfully finished."""
    
    controller = environ['controller']
    toolkit = controller.toolkit
    view = controller.view

    view = None #hack
    
    toolkit.messageDialog(view, "Note", message)

    outdir = toolkit.dirDialog( view, "output directory" )

    if outdir is None: return

    resultlink = toolkit.textentryDialog( view, "Result link", "Please input the link to the result here", "%s/browser/browse/|/path/to/outputdirectory" % localproxy )

    print resultlink

    if resultlink is None: return

    signature = '/browser/browse/'

    pos = resultlink.find(signature)
    if pos == -1: raise "Unable to find signature %r in link %r" % (signature, resultlink)
    encodedPath = resultlink[  pos + len(signature ) : ]
    path = decodePath( encodedPath )
    
    files = runShellCmd( 'ssh %s ls %s' % ( computingServer, path ) ).split('\n')

    print files

    for f in files:
        if f and len(f)>0:
            runShellCmd( 'scp %s:"%s/%s" "%s"' % (
                computingServer, _norm(path), _norm(f), _norm(outdir) ) )
        continue

    toolkit.messageDialog(
        view, "Succeed!",
        "Files have been retrieved from the computing server %s" % computingServer)
    
    return


def _norm( path ):
    import string
    rt = ''
    for i in path:
        if i not in string.letters + string.digits + '/' + '-':
            rt += '\\'
            pass
        rt += i
        continue
    return rt


#copied froom web/ARCS/arcs/controllers/browser
def decodePath(path):
    rt = path[1:]
    if not rt.startswith('/'): rt = '/' + rt
    return rt


def runShellCmd( cmd ):
    import tempfile
    f = tempfile.mktemp()
    cmd = "%s > %s" % (cmd, f)
    import os
    print "WebAppTools: executing %s" % cmd
    if os.system( cmd ): raise "%s failed" % str(cmd)
    rt = open(f).read()
    os.remove(f)
    return rt


__export__ = [
    (menutext_retrieve_files, GetFilesFromComputingServer),
    ]
