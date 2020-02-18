"""
This file contains the main function of E-Fuzzer. 
Functions for checking the environment to make sure 
the program runs properly are also defined here.
Functions not related to the actual fuzzing can be
found here. 

Refer to sqlmap's sqlmap.py
"""

import inspect
import os
import sys
from inputParser import cmdParser
from UserInput import UserInput
from payload import Payload
from request import Request

"""
Check Python version
"""
def checkPyVer():
    # Must be using at least Python 3
    if sys.version_info[0] < 3:
        print("Must be using Python 3")
        return False
    
    return True

"""
Check if all dependencies are installed. If not, provide an 
instruction to install the missing dependencies.
"""
def checkDependencies():
    pass

"""
Print E-Fuzzer's description
"""
def printFuzzerDescription():
    print('E-Fuzzer is a fuzzer specializing in XSS and SQL injection. \
        This is a project by J. Magbanua, N. Sontillano and N. Tubis \
        for an undergraduate class. \n \n \
        Use --help or --h to view available options.')


def main():
    """
    Main function of E-Fuzzer when running from command line.
    """
    if checkPyVer():
        items, values = cmdParser()

        data = UserInput(items, values)
        if data.checkOptions():
            payload = Payload(data.file)
            request = Request()

            request.forgeHeaders(data.cookie, data.basicAuth)
            request.setData(data.data, data.static)
            request.setMethod(data.method)
            
            _ = payload.getNextPayload() 
            while _:
                if data.isUrlWildcard():
                    request.setUrl(data.url, _)
                else:
                    request.setUrl(data.url)

                request.setWildcardData(_)
                request.sendRequest()
                _ = payload.getNextPayload() 

if __name__ == "__main__":
    main()