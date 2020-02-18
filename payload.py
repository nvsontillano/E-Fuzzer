DEFAULT_FILE = ''

"""
Class for the malicious input strings
"""
class Payload():
    payloadList = []

    """
    If user provided a file of input strings, use
    it; if not, use the default file
    """
    def __init__(self, file):
        if file:
            self.getListFromFile(file)
        else:
            self.getListFromFile(DEFAULT_FILE)

    """
    Get the contents of the file and store
    them into a list
    """
    def getListFromFile(self, file):
        pass

    """
    Get the next string to be sent from 
    the payload list
    """
    def getNextPayload(self):
        return 1
