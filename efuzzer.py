"""
This file contains the main function of E-Fuzzer. 
Functions for checking the environment to make sure 
the program runs properly are also defined here.
Functions not related to the actual fuzzing can be
found here. 

Refer to sqlmap's sqlmap.py
"""

from inputParser import cmdParser
from UserInput import UserInput

def getProgramPath():
    """
    Get E-Fuzzer's directory
    """
    pass

def checkEnvironment():
    """
    Check if system properly handles non-ASCII paths and 
    runtime environment is not broken.
    """
    pass

def printFuzzerDescription():
    """
    Print E-Fuzzer's description
    """
    pass

def main():
    """
    Main function of E-Fuzzer when running from command line.
    """
    items, values = cmdParser()
    data = UserInput(items, values)
    print("ARGUMENTS: ", items, values)
    print('data.url', data.url, 'data.data', data.data)

if __name__ == "__main__":
    main()