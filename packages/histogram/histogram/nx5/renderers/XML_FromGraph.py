#!/user/bin/env python 
# (c) 2003 T. M. Kelley California Institute of Technology

from pyre.weaver.mills.XMLMill import XMLMill
from HDFVisitor import HDFVisitor

class Renderer(XMLMill, HDFVisitor):


    def onGroup(self, node):
        
        if node.className() != 'NXroot':
            vgstr = '<Group name="%s" class="%s"'%\
                    (node.name(), node.className() )
            attributes = node.attributes()
            for attribute in attributes.keys():
                if attribute != 'name' and attribute != 'class':
                    vgstr += ' '+str(attribute)+'="'+str(attributes[attribute])+'"'
            vgstr += '>'
        else:
            vgstr = '<nexus name="%s" class="%s"'%\
                    (node.name(), node.className() )
            attributes = node.attributes()
            attrkeys = attributes.keys()
            if attrkeys != []:
                for attribute in attrkeys:
                    if attribute != 'name' and attribute != 'class':
                        vgstr += ' '+str(attribute)+'="'+\
                                 str(attributes[attribute])+'"'
            vgstr += '>'
        self._write(vgstr)
        self._indent()
        for entry in node.children():
            entry.identify(self)
        self._outdent()
        if node.className() == 'NXroot':
            self._write( "</nexus>")
        else:
            self._write("</Group>")
        return


    def onDetectorArray( self, node):
        return self.onGroup( node)


    def onDetectorPack( self, node):
        return self.onGroup( node)


    def onInstrument( self, node):
        return self.onGroup( node)


    def onLPSD( self, node):
        return self.onGroup( node)


    def onLPSDPixel( self, node):
        return self.onGroup( node)
    

    def onModerator( self, node):
        return self.onGroup( node)


    def onMonitor( self, node):
        return self.onGroup( node)


    def onDataset(self, node):
        dsstr = '<Dataset name="%s" class="%s"'%\
                (node.name(), node.className())
        attributes = node.attributes()
        for attribute in attributes.keys():
            if attribute != 'name' and attribute != 'class':
                dsstr += ' '+str(attribute)+'="'+str(attributes[attribute])+'"'
        dims = node.dimensions()
        rank = node.rank()
        datatype = node.datatype()
        dsstr += ' rank="'+str(rank)+'"'
        for i in range(rank):
            dsstr += ' dimension'+str(i+1)+'="'+str(dims[i])+'"'
        dsstr += ' datatype="'+str(datatype)+'"'
        dsstr += '/>'
        self._write(dsstr )
        return


    def __init__(self):
        XMLMill.__init__(self)
        return


    def _renderDocument(self, node, options=None):
        self._rep += ['', '<!DOCTYPE nexus>', '']#, '<nexus>', '' ]
        self.onGroup(node)
        return


# version
__id__ = "$Id: XML_FromGraph.py 89 2005-07-16 16:22:28Z tim $"

# End of file
