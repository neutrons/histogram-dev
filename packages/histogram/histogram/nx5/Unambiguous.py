class Unambiguous(object):

    def __init__(self, disambiguator = None):
        if disambiguator is None:
            try:
                from ConsoleDisambiguator import ConsoleDisambiguator
            except ImportError:
                from nexus.ConsoleDisambiguator import ConsoleDisambiguator
            disambiguator = ConsoleDisambiguator()
        self._disambiguator = disambiguator
        return
    
    def _disambiguate(self, listOfChoices, promptPreString, promptPostString):
        raise NotImplementedError,"%s must implement _disambiguate()"\
              %(self.__class__.__name__)

