#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

import xml.sax
from nx5.nexml.elements.Group import Group
from nx5.nexml.elements.Dataset import Dataset
from nx5.nexml.elements.NexusElement import NexusElement

# logic: when a start element comes along, make the corresponding object.
# If the element is a dataset, set the _datasetPending flag, meaning
# that we'd better get endElement as the very next call: if not,
# the next startElement will raise an exception.  Add the object to
# the tail member of openGroups as a child. Push the object onto 
# the openGoups stack. When end element comes along, pop the
# openGroups stack.

class Renderer(xml.sax.ContentHandler):

    def result( self):
        return self._root


    def startElement( self, elementName, attributes):

        # make sure we're not being asked to append to a dataset
        self.__nonePending()
        
        name = self.__name( attributes)

        if elementName != 'nexus':
            self._path.append('/' + name)

#        print ''.join( self._path)

        # make node object
        if self.__isGroup( elementName, attributes):
            node = self.__makeGroup( name, attributes)
        elif self.__isDataset( elementName, attributes):
            node = self.__makeDataset( name, attributes)
            self._datasetPending = True
        else:
            return  # ignore unknown
            
        # attach to parent
        if name != 'nexus':
            self._openGroups[-1].addChild( node)
        else:
            self._root = node
            
        # push object onto stack
        self._openGroups.append( node)

        self._rep += "Element: %s %s\n" % (name, str(attributes))

        return


    def endElement( self, elementName):
        if self._datasetPending:
            self._datasetPending = False
            
        try:
            self._path.pop()
        except IndexError, msg:
            if 'pop from empty list' in msg:
                pass
        self._openGroups.pop()

        self._rep += "End of element %s\n" % elementName

        return


    def __isDataset( self, elementName, attributes):
        if elementName == 'Dataset': return True
        if 'class' in attributes.keys():
            if 'SDS' in attributes['class']: return True
            elif 'Dataset' in attributes['class']: return True
        return False


    def __isGroup( self, elementName, attributes):
        if elementName == 'Group': return True
        if 'NX' == elementName[:2]: return True
        if 'class' in attributes.keys():
            if 'NX' in attributes['class']: return True
        return False


    def __makeDataset( self, name, attributes):
        copiedAttrKeys = ['rank', 'datatype', 'class', 'name']
        # obtain necessary attributes
        try:
            rank = int( attributes['rank'])
            dimensions = []
            for j in range(1, rank+1):
                key = 'dimension%i' % j
                dimensions.append( int(attributes[key]))
                copiedAttrKeys.append( key)
            datatype = int(attributes['datatype'])
        except KeyError, msg:
            error = str( msg)
            error += '\nmalformed nexml document: dataset tag missing'
            error += ' necessary attribute'
            raise TypeError, error

        try:
            klass = attributes['class']
        except KeyError:
            klass = "Dataset"

        path = ''.join( self._path)
        if not path:
            path = '/'

        dataset = Dataset( name, klass, None, path, dimensions, datatype)

        # collect additional attributes
        attrs = {}
        for key in attributes.keys():
            if key not in copiedAttrKeys:
                attrs[key] = attributes[keys]
        dataset.setAttributes( attrs)
        
        return dataset


    def __makeGroup( self, name, attributes):
        copiedAttrKeys = [ 'class', 'name']

        try:
            klass = attributes['class']
        except KeyError:
            klass = "NXunknown"

        path = ''.join( self._path)
        if not path:
            path = '/'

        group = Group( name, klass, None, path)

        attrs = {}
        for key in attributes.keys():
            if key not in copiedAttrKeys:
                attrs[key] = attributes[key]
        group.setAttributes( attrs)
        
        return group


    def __name( self, attributes):
        name = ''
        try:
            name = attributes['name']
        except KeyError, msg:
            error = str( msg)
            error += '\nmalformed nexml document: tag missing "name"'
            error += ' attribute\npath = %s, openGroups = %s' % \
                     ( ''.join(self._path), str( self._openGroups))
            raise TypeError, error
        return name


    def __nonePending( self):
        if self._datasetPending:
            msg = "Dataset (leaf node) on stack must end before node"
            msg += "\n%s begins: path = %s, openGroups = %s" % \
                   (name, str(self._path), str(self._openGroups))
            raise TypeError, msg
        return


    def __init__(self):
        xml.sax.ContentHandler.__init__( self)
        self._rep = ""
        self._path = [] 
        self._datasetPending = False
        self._root = None
        self._openGroups = []
        
        return

    


# version
__id__ = "$Id: Graph_FromXML.py 33 2005-03-29 20:25:27Z tim $"

# End of file
