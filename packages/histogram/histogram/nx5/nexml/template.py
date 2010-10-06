class TemplateParser:

    def __init__(self):
        self._cache = []
        return

    
    def parse( self, instream, locals={} ):
        lines = instream.read().splitlines()
        #temporary file for output stream
##         import tempfile
##         h, path = tempfile.mkstemp( )
##         stream = open(path, 'w')
        from StringStream import StringStream
        stream = StringStream( instream.name + "template" )
        print >>stream, '\n'.join(self._exec(lines, locals ))
##         stream.close()
##         newstream = open(path, 'r')
##         import os
##         os.remove( path )
        return stream
##         return newstream


    def _write( self, t ):
        self._cache.append( t )
        return

    
    def _exec( self, lines, locals ):
        locals['write'] = self._write
        locals['cache'] = self._cache
        rt = []
        code_cache = []
        iscode = False
        for line in lines:
            if line.startswith( '% ' ):
                code = line[2:] 
                code_cache.append( code )
                if not iscode: iscode = True
                pass
            else:
                if iscode:
                    rt += self.onCode(code_cache, locals)
                    code_cache = []
                    pass
                rt.append( line )
                iscode = False
                pass
            continue
        return rt


    def onCode(self, code_cache, locals):
        exec '\n'.join(code_cache) in locals
        rt = self._cache
        self._cache = []
        return rt



def test():
    t  = """
line1
line2
template begin
% write( "hello" )
template end
"""
    parser = TemplateParser()
    print parser._exec( t.splitlines(), {} )

    import tempfile
    h, path = tempfile.mkstemp()
    stream = open( path, 'w' )
    print >>stream, t
    stream.close()
    
    print parser.parse( open(path), {} ).read()

    import os
    os.remove( path )
    return


if __name__ == "__main__" : test()
