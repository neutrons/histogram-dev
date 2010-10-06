#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                             Michael A.G. Aivazis
#                      California Institute of Technology
#                      (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.xml.Parser import Parser as BaseParser


class Parser(BaseParser):


    def parse(self, stream, parserFactory=None):
        from parser.Document import Document
        return BaseParser.parse(self, stream, Document(stream.name), parserFactory)


    def __init__(self):
        BaseParser.__init__(self)
        return

    pass # end of Parser


def test():
    t = '''

<!DOCTYPE nexus>

<nexus class="NXroot" name="nexus">

  <Group name="g" class="class" > </Group>

</nexus>

    '''
    import tempfile
    h, path = tempfile.mkstemp()
    stream = open( path, 'w' )
    print >>stream, t
    stream.close()
    
    g = Parser().parse( open(path) )

    import os
    os.remove( path )


    from nx5.renderers.HDFPrinter import HDFPrinter
    HDFPrinter().render( g )
    return


if __name__ == "__main__": test()
           

# version
__id__ = "$Id: Parser.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
