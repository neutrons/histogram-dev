
import os

package = __import__( "pyre" )
name = package.__name__


class Paths:
  scheme = {
    'bin': 'bin',
    'python': 'python',
    'lib': 'lib',
    'include': 'include',
    'data': 'share',
    'etc': 'etc',
    }
  def __init__(
      self, root, bin = None, python = None, lib = None, 
      include = None, data = None, etc = None):
    self.root = root
    scheme = self.scheme
    from os.path import join

    if bin is None:
      bin = join( root, scheme['bin'] )
    self.bin = bin

    if python is None:
      python = join( root, scheme['python'] )
    self.python = python

    if lib is None:
      lib = join( root, scheme['lib'] )
    self.lib = lib

    if include is None:
      include = join( root, scheme['include'] )
    self.include = include

    if data is None:
      data = join( root, scheme['data'] )
    self.data = data

    if etc is None:
      etc = join( root, scheme['etc'] )
    self.etc = etc
    
    return



try: 
  import install_info as i
  #the following scheme is enforced by distutils-adpt
  #if we are using different installation scheme,
  #this has to be changed
  etc = getattr(i, 'etc', None)
  if etc is None: etc = os.path.join(i.data, 'etc')
  paths = Paths( 
    i.root, bin = i.bin, python = i.python, lib = i.lib,
    include = i.include, data = i.data, etc = etc
    )
except ImportError:
  #here we assume that we are using mm build procedure
  # assume that path_of_pyregui/../.. is the installation root
  root = os.path.abspath( os.path.join( package.__path__[0], '..', '..' ) )
  paths = Paths(root)
  pass


def find_etc_dir():
  "find the installation directory of 'etc/'"
  return paths.etc


etc = find_etc_dir()
