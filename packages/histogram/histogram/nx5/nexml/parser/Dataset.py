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


import urllib
from AbstractNode import AbstractNode, debug


class Dataset(AbstractNode):


    tag = "Dataset"


    def content(self, content):
        debug.log( "content=%s" % content )
        content = content.strip()
        if len(content)==0: return
        self.element.data_description =  urllib.unquote(content).strip() 
        self.locator = self.document.locator
        return


    def _makeElement(self, attributes):
        consumedAttributes = ['rank', 'datatype', 'name']

        try:
            rank = int( attributes['rank'])
            dimensions = []
            for j in range(1, rank+1):
                key = 'dimension%i' % j
                dimensions.append( int(attributes[key]))
                consumedAttributes.append( key)
            datatype = int(attributes['datatype'])
            
        except KeyError, msg:
            error = "%s: %s" % (msg.__class__.__name__, msg)
            error += '\nmalformed nexml document: dataset tag missing'
            error += ' necessary attribute'
            raise TypeError, error

        klass = attributes.get('class') or "NXDataset"
        consumedAttributes.append( 'class' )

        name = attributes['name']
        
        from nx5.nexml.elements.Dataset import Dataset 
        rt = Dataset(name, klass, None, '', dimensions, datatype, None)
        
        attrs = attributes.copy()
        for k in ['class', 'name']: del attrs[k]
        rt.setAttributes( attrs )

        return rt
    
    
    pass # end of Dataset


# version
__id__ = "$Id$"

# End of file 
