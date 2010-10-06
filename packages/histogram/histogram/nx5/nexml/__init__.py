#!/usr/bin/env python
# (c) Copyright 2005 T. M. Kelley, California Institute of Technology

def hello():
    print 'hello from nexus.nexml.elements'
    return

def search(XMLString, targetName, targetAttrs, \
           parentName=None, parentClass=None):

    import xml.sax, Searcher
    
    contentHandler = Searcher.Searcher(targetName, targetAttrs)
    xml.sax.parseString( XMLString, contentHandler)
    
    results = contentHandler.results()

    datasets = []
    if parentName is None:
        paths =  _makeNXpaths(results)
        for i in range(len(results)):
            result = results[i]
            path = paths[i]
            datasets.append( _makeDataset(result, path))
        return datasets
    else:
        filteredResults = _filterResults(results, parentName, parentClass)
        paths =  _makeNXpaths( filteredResults)
        for i in range(len(filteredResults)):
            result = filteredResults[i]
            path = paths[i]
            datasets.append(_makeDataset(result,path))
        return datasets
    raise


from Parser import Parser
default_parser = Parser()


def parse( stream ): return default_parser.parse( stream )

def parse_file( filename ): return parse( open( filename ) )


# helpers
def _makeDataset(result, path):
    resAtts = result[-1][1]
    from  elements.Dataset import Dataset
##     print '------------------nexus.nexml.search():-------------------'
##     print resAtts.keys()
    dimensions = []
    datatype = None
    rank = int(resAtts['rank'])
#    print '\n\n-----nexus.nexml.search::_makeDataset():---'
    for i in range(1,rank+1):
        dimstr = 'dimension'+str(i)
        if dimstr in resAtts.keys():
            dimensions.append( int(resAtts[dimstr]))
    if 'datatype' in resAtts.keys():
        datatype = int(resAtts['datatype'])
#    print rank,dimensions,datatype
    ds = Dataset(path.leaf()[1], 'Dataset', path, path.asString(), dimensions, datatype)
    resAttdict = _copyAttrs( resAtts, rank)
    ds.setAttributes( resAttdict)
    return ds

def _copyAttrs(resAtts, rank):
    """Copy attributes from XML node thingy to dictionary"""
    resdict = {}
    excluded = ['rank','datatype']
    for i in range(1,rank+1):
        excluded.append('dimension'+str(i))
    for key in resAtts.keys():
        if key not in excluded:
            resdict[key] = resAtts[key]
    return resdict

def _filterResults(results, parentName, parentClass):
    filteredResults = []
    for result in results:
        parentNodeAttrs = result[-2][1]
        try:
            parentNodeName = parentNodeAttrs['name']
            parentNodeClass = parentNodeAttrs['class']
        except KeyError,val:
            print val
            exStr = 'Ill-formed NeXML: Groups must have name & class'
            raise IllFormedNeXML,exStr
        if (parentNodeName == parentName) and \
           (parentNodeClass == parentClass):
            filteredResults.append(result)
    return filteredResults


def _makeNXpaths(listOStacks):
    from nx5.NXpath import NXpath
    nxpaths = []
    for stack in listOStacks:
        nxpaths.append( NXpath(stack))
    return nxpaths


# version
__id__ = "$Id: __init__.py 116 2007-03-09 14:25:21Z linjiao $"

#End of file

