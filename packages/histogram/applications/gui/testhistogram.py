
def create(noerror = False):
    from histogram import createContinuousAxis, createDiscreteAxis, arange
    #create axis E
    axisE = createContinuousAxis( 'E', 'meter', arange( 0.5, 3.5, 1.0 ) )
    
    #create axis "tubeId"
    axisTubeId = createDiscreteAxis( "tubeId", [1, 3, 99], 'int')
    
    #create histogram
    from histogram import createDataset
    from ndarray.StdVectorNdArray import NdArray
    dataStorage = NdArray( 'double', range(9) ); dataStorage.setShape( (3,3) )
    errorsStorage = NdArray( 'double', range(9) ); errorsStorage.setShape( (3,3) )
    
    data = createDataset('data', '', storage = dataStorage )
    if noerror: errors = None
    else: errors  = createDataset('errors', '', storage = errorsStorage )
    from histogram.Histogram import Histogram
    histogram = Histogram( name = 'I(E, TubeId)', data = data, errors = errors,
                           axes = [axisE, axisTubeId])
    return histogram
    
