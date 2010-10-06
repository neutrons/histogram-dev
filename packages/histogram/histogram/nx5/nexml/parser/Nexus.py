#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode


class Nexus(AbstractNode):


    tag = "nexus"
    
    onGroup = onDataset = AbstractNode.onElement


    def content(self, content):
        content = content.strip()
        if len(content)==0: return
        raise SyntaxError , "NXGroup cannot handle content: %r" % content
    

    def _makeElement(self, attributes):
        consumedAttributes = ['class', 'name']
        self._checkRequiredAttributes( attributes, consumedAttributes )
        
        klass = attributes.get( 'class' ) 
        if klass != "NXroot": raise "root node: class should be NXroot"

        name = attributes.get('name')

        from nx5.nexml.elements.Nexus import Nexus
        rt = Nexus( name, klass, None, '' )

        attrs = attributes.copy()
        for k in consumedAttributes: del attrs[k]
        rt.setAttributes( attrs )

        return rt


    pass # end of Nexus
    


# version
__id__ = "$Id$"

# End of file 
