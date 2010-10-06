
import journal
debug = journal.debug("nx5.renderers")


from HDFVisitor import HDFVisitor

class Renderer( HDFVisitor):
    
    """Visitor that extracts data from a nexus file into a given graup"""


    def render( self, doc):
        return doc.identify( self)
    

    def __init__( self, filename):
        import nx5.file
        self._nxf = nx5.file.file( filename, 'r')

        from nx5.file.VectorReader import Reader
        self._reader = Reader()

        self._selector = self._nxf.selector()
        return


    def onGroup(self, group):
        # descend
        for child in group.children():
            child.identify( self)
            pass
        return


    def onDataset( self, dataset):
        reader = self._reader
        selector = self._selector
        path = dataset.path()
        selector.select( path )
        #read and assign
        dataset._storage = reader.read( selector )
        return


    pass # end of Renderer
