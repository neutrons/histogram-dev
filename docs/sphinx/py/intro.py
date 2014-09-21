
def test():
    from histogram import histogram, axis, arange, plot
    xaxis = axis('x', arange(5), unit='meter')
    yaxis = axis('y', arange(7), unit='cm')
    axes = [xaxis, yaxis]
    h = histogram( "intensity", axes, fromfunction=lambda x,y: x**2+y**2)
    print h
    plot(h)
    help(h)
    slice = h[3, ()]


test()
