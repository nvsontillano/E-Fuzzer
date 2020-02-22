import re
import os

"""
Class for the arguments entered by the user
"""
class Input():
    # Keep track how many arguments the user provided
    argsCtr = 0

    def __init__(self, args):
        for arg in args.keys():
            setattr(self, arg, args[arg])
            if args[arg]: self.argsCtr+=1

    """
    Check URL 
    """
    def checkUrl(self):
        if not self.url:
            print("URL is required")
            # raise exception

    """
    Check HTTP(s) Basic authentication 
    username and password format 
    """
    def checkBasicAuth(self):
        if self.basicAuth: 
            regExp = "^(.*?):(.*?)$"

            if not re.search(regExp, self.basicAuth):
                print("HTTP Basic authentication credentials \
                    value must be in format 'username:password'")
                # raise exception

    """
    Check the data format
    """
    def checkData(self):
        if self.data:
            dataList = []

            for _ in self.data.split(';'):
                dataList.append(_.strip())

            regExp = "^(.*?)=(.*?)$"

            for _ in dataList:
                if not re.search(regExp, _):
                    print("The data must be in format 'var1=value1;var2=value2'")
                    # raise exception
    
    """
    Check the cookie format
    """
    def checkCookie(self):
        if self.cookie:
            cookieList = []

            for _ in self.cookie.split(';'):
                cookieList.append(_.strip())

            regExp = "^(.*?)=(.*?)$"

            for _ in cookieList:
                if not re.search(regExp, _):
                    print("Cookies should must be in format 'name1=value1;name2=value2'")
                    # raise exception

    """
    Check the file format
    """
    def checkFile(self):
        if self.file:
            if not os.path.isfile(self.file):
                print("File does not exist.") 
                # raise exception

    """
    Check the method format
    """
    def checkMethod(self):
        if self.method:
            _ = self.method.lower()
            if not _ =="get" and not _=="post":
                print("Method should be either 'GET' or 'POST'")
                # raise exception

    """
    Check the values for static data
    """
    def checkStatic(self):
        if self.static:
            dataCount = len(re.findall(";", self.data)) + 1

            for _ in self.static.split(','):
                if int(_.strip()) >= dataCount:
                    print("Values for '--static' should be \
                    less than or equal to the number of value in '--data'")
                    # raise exception 

    """
    Check for URL wildcard (if URL contains '<>')
    """
    def isUrlWildcard(self):
        if self.url:
            regExp = r"((http|https):\/\/|www.)?.+\/<>\/?.?"

            if not re.search(regExp, self.url):
                return False

        return True

    """
    Check if the user inputs were properly formed
    """
    def checkOptions(self):
        if self.isUrlWildcard() or self.argsCtr>1:
            if self.checkUrl() and self.checkBasicAuth() and self.checkData() and self.checkCookie() and self.checkFile() and self.checkMethod() and self.checkStatic():
                return

        print("Not enough arguments")
        # raise exception
                    
    

