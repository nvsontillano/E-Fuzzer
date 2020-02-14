"""
Class for the arguments entered by the user
"""
class UserInput():
    def __init__(self, items, values):
        for item, value in zip(items, values):
            setattr(self, item, value)

    def checkURL(self):
        """
        Check URL stability
        """
        pass

    def checkOptions(self):
        """
        Check GET, POST, Cookie parameters
        """
        pass