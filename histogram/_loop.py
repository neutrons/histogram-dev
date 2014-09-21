def loop( axes, f ):
    '''loop over all values on a grid defined by axes
    
    axes: a list of axes

    loop( [ ['a','b','c'], [1,5] ], f ) --> f('a',1); f('a',5); ...; f('c',5)
    '''
    shape = [ len(axis) for axis in axes ]
    indexes = [ 0 for axis in axes ]
    for i in range(volume(shape) ):
        vertex = tuple( [ axis[i] for i,axis in zip(indexes,axes) ] )
        f( *vertex )
        increment(indexes, shape)
        continue
    return


def increment( indexes, limits ):
    """increase indexes up to limits
    increment( [1,4,3], [3,10,8] ) --> indexes becomes [1,4,4]
    increment( [1,4,7], [3,10,8] ) --> indexes becomes [1,5,0]
    """
    n = len(limits)
    for i in range(n-1, -1, -1):
        index = indexes[i]
        if index < limits[i]-1:
            indexes[i] += 1
            break
        else :
            indexes[i] = 0
        continue

    return


def volume(shape):
    from operator import mul
    return reduce(mul, shape)
        


def test_increment():
    limits = [3,10,8]
    indexes = [1,4,3]
    increment( indexes, limits )
    assert indexes[0] == 1
    assert indexes[1] == 4
    assert indexes[2] == 4
    
    indexes = [1,4,7]
    increment( indexes, limits )
    assert indexes[0] == 1
    assert indexes[1] == 5
    assert indexes[2] == 0

    return


def test_loop():
    axes = [
        ['a','b'],
        [1,2,3],
        ]
    def f(x,y): print x,y
    loop( axes, f )
    return


def main():
    test_increment()
    test_loop()
    return


if __name__== '__main__': main()
                                
                                                    
