from Unambiguous import Unambiguous

class NXUnambiguous(Unambiguous):

    def _disambiguate(self, listOfNXPaths, promptPreString, \
                      promptPostString):
        dimbig = self._disambiguator
        dimbig.setPrePrompt(promptPreString)
        dimbig.setPostPrompt(promptPostString)
        alternatives = {}
        for i in range( len( listOfNXPaths)):
            alternatives[i+1] = _NXpathAsString( listOfNXPaths[i].NXpath())
        dimbig.updateAlternatives( alternatives)
        dimbig.presentAlternatives()
        #risky--does client know that choice has to be an integer
        #greater than 0?
        choice = dimbig.choice()
        return listOfNXPaths[choice - 1]
        

    def __init__(self, disambiguator = None):
        Unambiguous.__init__(self, disambiguator)
        return

#helper
def _NXpathAsString(nxpath):
        retstr = ''
        retstr += nxpath.root()[0]+'/'
        for pathEl in nxpath.path():
            retstr += pathEl[1]+'/'
        retstr += nxpath.leaf()[1]
        return retstr

# version
__id__ = "$Id: NXUnambiguous.py 8 2005-01-20 23:09:19Z tim $"

# End of file

