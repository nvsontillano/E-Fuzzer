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

from dependency import checkPyVersion
from cmd import parser
from Input import Input
from request import Request
# from inputParser import cmdParser
# from UserInput import UserInput
# from payload import Payload
# from request import Request
# from payload import getList


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
    Main function of E-Fuzzer.
    """
    checkPyVersion()
    args = parser()
    inputs = Input(args)
    inputs.checkOptions()

    request = Request()
    request.forgeHeaders(inputs.cookie, inputs.basicAuth)
    request.setData(inputs.data, inputs.static)
    request.setMethod(inputs.method)

    stringList = Payload(data.file)
    responses = {}

    for string in stringList:
        if input.isUrlWildcard():
            request.setUrl(inputs.url, string)
        else:
            request.setUrl(inputs.url)

        request.setWildcardData(string)
        response = request.sendRequest()
        # code here to output other info 
        responses[string] = response


if __name__ == "__main__":
    main()