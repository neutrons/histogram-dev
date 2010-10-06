from Disambiguator import Disambiguator

class ConsoleDisambiguator(Disambiguator):

    def presentAlternatives(self):
        if len(self._alternatives.keys() ) == 0:
            return
        altKeys = self._alternatives.keys()
        print self._prePrompt
        for item in altKeys:
            print item,'.....',self._alternatives[item]
        choice = None
        while choice not in altKeys:
            choice_str = raw_input(self._postPrompt)
            #Convert string input to whatever type the keys are
            #Again, this is a weakpoint in that it presumes the
            # keys are all the same type
            try:
                choice = altKeys[0].__class__.__new__(type(altKeys[0]), \
                                                      choice_str)
            except ValueError: choice = None
        self._choice = choice
        return
    
    def __init__(self, promptString = None, alternativesDict = None):
        Disambiguator.__init__(self, promptString, alternativesDict)



# version
__id__ = "$Id: ConsoleDisambiguator.py 8 2005-01-20 23:09:19Z tim $"

# End of file
