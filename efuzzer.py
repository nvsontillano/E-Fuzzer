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
#from request import Request, HTTP_HEADER

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
        print("ARGUMENTS: ", items, values)

        data = UserInput(items, values)
        if data.checkOptions():
            print("proceed to forming request")

if __name__ == "__main__":
    main()