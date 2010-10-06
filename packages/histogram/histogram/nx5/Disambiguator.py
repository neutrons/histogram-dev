class Disambiguator(object):

    def presentAlternatives(self):
        raise NotImplementedError,"%s must implement presentAlternatives()"\
              %(self.__class__.__name__)
    

    def choice(self): return self._choice

    def setPrePrompt(self, prePromptString):
        if type(prePromptString) is str:
            self._prePrompt = prePromptString
        else:
            raise TypeError,'prePromptString must be a string'
        return

    def setPostPrompt(self, postPromptString):
        if type(postPromptString) is str:
            self._postPrompt = postPromptString
        else:
            raise TypeError,'postPromptString must be a string'
        return

    def updateAlternatives(self, altsDict):
        if type(altsDict) is dict:
            self._alternatives.update(altsDict)
        else:
            raise TypeError,'altsDict must be a dictionary'
        return
    
    
    def __init__(self, prePromptString=None, postPromptString=None,\
                 alternativesDict=None):
        # prePromptString
        if prePromptString is None:
            self._prePrompt = ''
        elif type( prePromptString) is str:
            self._prePrompt = prePromptString
        else:
            raise TypeError,'prePromptString must be a string'
        # post prompt
        if postPromptString is None:
            self._postPrompt = ''
        elif type( postPromptString) is str:
            self._postPrompt = postPromptString
        else:
            raise TypeError,'postPromptString must be a string'
        # alternatives
        if alternativesDict is None:
            self._alternatives = {}
        elif type(alternativesDict) is dict:
            self._alternatives = alternativesDict
        else:
            raise TypeError,'alternativesDict must be a dictionary'
        return
       
