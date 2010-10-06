
class StringStream:

    def __init__(self, name, s=None):
        self.name = name
        if s is None: self._lines = []
        else: self._lines = s.splitlines()
        self._read_pos = 0
        return

    def close(self):
        self.write = self.writelines = self.read = self.readline = self.readlines = self._closed
        return

    def write(self, s):
        lines = s.splitlines()
        if len(self._lines) == 0: self._lines = list(lines); return
        self._lines[-1] += lines[0]
        self._lines += lines[1:]
        return

    def writelines(self, ls):
        self._lines += ls
        return

    def read(self, size=None):
        all = '\n'.join(self._lines)
        if size is None:
            self._read_pos = len(all) + 1
            return all+'\n'
        pos = self._read_pos
        rt = all[ pos: pos+size ]
        self._read_pos += size
        return rt

    def readline(self, size = None):
        all = '\n'.join(self._lines)
        pos = self._read_pos
        candidate = all[pos:].splitlines()[0]
        if size is None or size >= len(candidate):
            size = len( candidate ) + 1
            self._read_pos += size
            return candidate+'\n'
        else:
            self._read_pos += size
            return candidate[:size] + '\n'
        raise

    def readlines(self):
        all = '\n'.join(self._lines)
        rt = [ t+'\n' for t in all[ self._read_pos: ].splitlines() ]
        self._read_pos = len(all) + 1
        return rt

    def _closed(self): raise IOError, "%s is closed" % self.name

    pass #end of StringStream
        

def test():
    ss = StringStream( "hello" )
    assert ss.name == "hello"
    ss.write( 'abc' )
    ss.writelines( ['a','b'] )
    ss.readline( )
    ss.readlines()
    ss.read()
    ss.close()
    return


if __name__ == "__main__": test()
