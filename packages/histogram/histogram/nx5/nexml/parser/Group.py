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


class Group(AbstractNode):

    tag = "Group"

    onDataset = AbstractNode.onElement


    def content(self, content):
        content = content.strip()
        if len(content)==0: return
        raise SyntaxError , "NXGroup cannot handle content"
    

    def _makeElement(self, attributes):
        consumedAttributes = ['name']
        self._checkRequiredAttributes( attributes, consumedAttributes )

        klass = attributes.get( 'class' ) or 'NXunknown'
        consumedAttributes.append( 'class' )

        name = attributes.get('name')
        
        from nx5.nexml.elements.Group import Group 
        rt = Group(name, klass, None, '')
        
        attrs = attributes.copy()
        for k in ['class', 'name']: del attrs[k]
        rt.setAttributes( attrs )

        return rt
    
    
    pass # end of Group

# version
__id__ = "$Id$"

# End of file 
