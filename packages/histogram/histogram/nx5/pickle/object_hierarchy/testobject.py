class TestObject(object):
    def __init__(self, name, data ):
        self.name = name
        self.data = data
        return
    pass


def testobject(kls=None):
    if kls is None:
        #from nx5.pickle.object_hierarchy.Leaf import Leaf
        #kls = Leaf
        kls = TestObject
    a = kls( 'a', 1 )
##     t = [1]
##     t.append( t )
##     l = t
##     t = tuple(l)
##     a.t = t
##     a.t1 = [1]
##     a.t2 = a.t1
##     a.d = {tuple():a, 3: "hello"}
##     a.n = None
##     a.b = True
    import numpy
    a.npa = numpy.array( range(100), float )

##     from stdVector import vector
##     v = vector( 'double', [1,2,3] )
##     a.v = v
    return a


