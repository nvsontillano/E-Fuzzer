SQLIDEFAULTFILE = ''
XSSDEFAULTFILE = ''

"""
Class for the malicious input strings
"""
class Payload():
    sqliStringList = []
    xssStringList = []
    stringList = []

    """
    If user provided a file of input strings, use
    it; if not, use the default file
    """
    def __init__(self, file=None):
        if file:
            self.getListFromFile(file)
        else:
            self.getListFromFile(DEFAULT_FILE)

    """
    Get the contents of the file and store
    them into a list
    """
    def getListFromFile(self, file):
        stringList = [line.rstrip('\n') for line in open(file)]

    def getList(self):
        return self.stringList
