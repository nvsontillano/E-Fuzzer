import re
import os

"""
Class for the arguments entered by the user
"""
class UserInput():
    argsCtr = 0

    def __init__(self, items, values):
        for item, value in zip(items, values):
            setattr(self, item, value)
            if value: self.argsCtr+=1

    """
    Check HTTP(s) Basic authentication 
    username and password format 
    """
    def checkBasicAuth(self):
        if not self.basicAuth:
            return True

        regExp = "^(.*?):(.*?)$"

        if not re.search(regExp, self.basicAuth):
            print("HTTP Basic authentication credentials \
                value must be in format 'username:password'")
            return False

        return True

    """
    Check the data format
    """
    def checkData(self):
        if not self.data:
            return True

        dataList = []

        for _ in self.data.split(';'):
            dataList.append(_.strip())

        regExp = "^(.*?)=(.*?)$"

        for _ in dataList:
            if not re.search(regExp, _):
                print("The data must be in format 'var1=value1;var2=value2'")
                return False
        
        return True
    
    """
    Check the cookie format
    """
    def checkCookie(self):
        if not self.cookie:
            return True

        cookieList = []

        for _ in self.cookie.split(';'):
            cookieList.append(_.strip())

        regExp = "^(.*?)=(.*?)$"

        for _ in cookieList:
            if not re.search(regExp, _):
                print("Cookies should must be in format 'name1=value1;name2=value2'")
                return False
        
        return True

    """
    Check the file format
    """
    def checkFile(self):
        if not self.file:
            return True

        if not os.path.isfile(self.file):
            print("File does not exist.") 
            return False

        return True

    """
    Check the method format
    """
    def checkMethod(self):
        if not self.method:
            return True
        
        _ = self.method.lower()
        if not _ =="get" and not _=="post":
            print("Method should be either 'GET' or 'POST'")
            return False
        
        return True

    """
    Check for URL wildcard (if URL contains '<>')
    """
    def isUrlWildcard(self):
        regExp = r"((http|https):\/\/|www.)?.+\/<>\/?.?"

        if not re.search(regExp, self.url):
            return False
        
        return True

    """
    Check if the user inputs were properly formed
    """
    def checkOptions(self):
        if self.isUrlWildcard() or self.argsCtr>1:
            if self.checkBasicAuth() and self.checkData() and self.checkCookie() and self.checkFile() and self.checkMethod():
                return True
                    
        return False


