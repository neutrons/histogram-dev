
def group(*args, **kwds):
    from Group import Group
    return Group( *args, **kwds )


def dataset(*args, **kwds):
    from Dataset import Dataset
    return Dataset(*args, **kwds)


# version
__id__ = "$Id: __init__.py 136 2007-10-05 12:54:52Z linjiao $"

#End of file

