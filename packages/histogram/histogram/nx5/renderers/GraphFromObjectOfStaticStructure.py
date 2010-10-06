#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractGraphFromObject import Renderer as Base

class Renderer(Base):

    """This renderer can deal with object with a static structure
    For example, a curve is an object of
    
     (name, axis_x, axis_y)
     
    while an axis is an object of
    
     (name, unit, ticks)
     
    We can use a xml file to specify the layout in which the data
    will be saved in a hdf5 file:

    <Group name=curve.name class="curve">
     <Group name=curve.axis_x.name class="axis" unit="meter">
      <Dataset name="ticks">
       curve.axis_x.ticks
      </Dataset>
     </Group>
     ...
    </Group>
    """

    def __init__(self, nexml_template, template_parser = None, parser = None):
        self.nexml_template = nexml_template
        if template_parser is None:
            from nx5.nexml.template import TemplateParser
            template_parser = TemplateParser()
            pass
        if parser is None:
            from nx5.nexml import default_parser as parser
            pass
        self.template_parser = template_parser
        self.parser = parser
        return


    def render(self, obj):
        nexml_template = self.nexml_template
        locals = {'obj': obj}
        tstream = open (nexml_template)
        stream = self.template_parser.parse( tstream, locals )
        tstream.close()
        graph = self.parser.parse( stream )
        stream.close()
        DataPropagator(obj).render( graph )
        from nx5.renderers.SetPath import Renderer as SetPath
        SetPath().render( graph )
        return graph

    pass # end of Renderer




from nx5.renderers.HDFVisitor import HDFVisitor as Base

class DataPropagator( Base ):


    def __init__(self, obj):
        self.obj = obj
        return


    def render(self, graph):
        graph.identify(self)
        return graph


    def onGroup( self, group):
        # descend
        for child in group.children():
            child.identify( self)
            continue
        return
        

    def onDataset( self, dataset):
        if dataset.storage() :
            raise "this renderer expect to render data from data description"
        data_description = dataset.data_description
        obj = self.obj
        dataset._storage = eval( data_description )
        return

    pass # end of DataPropagator



def test():
    nexml_template_str = """
<!DOCTYPE nexus>

<nexus class="NXroot" name="nexus">
  <Group name="test" class="NXentry">
% write( '''<Dataset name="x" class="SDS" rank="1" dimension1="%s" datatype="%s">
%       obj.x
%     </Dataset>''' % (obj.x.size(), obj.x.datatype()) )
  </Group>
</nexus>
"""
    import tempfile
    h, path = tempfile.mkstemp()
    stream = open( path, 'w' )
    print >>stream, nexml_template_str
    stream.close()

    class Obj: pass
    obj = Obj()
    from stdVector import vector
    obj.x = vector( 5, range(20) )

    graph = Renderer(path).render( obj )
    
    from HDFPrinter import HDFPrinter
    HDFPrinter().render( graph )
    
    import os
    os.remove( path )
    return



if __name__ == "__main__": test()


# version
__id__ = "$Id$"

# End of file 
