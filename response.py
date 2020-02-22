"""
This file contains the processing of the HTTP response.
"""

import os
from Directory import Directory
from datetime import datetime

SQLIFILENAME = "sqli.txt"
XSSFILENAME = "xss.txt"


def outputCmd():
    pass

def logToFile():
    sqliFile = open(SQLIFILENAME, 'a+')
    sqliFile.write(datetime.datetime.now())

    xssFile = open(XSSFILENAME, 'a+')
    xssFile.write(datetime.datetime.now())

    # code here to write successful payloads to file

def createDirectory(dirName):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)

def createFile():
    path = os.getcwd()

    createDirectory(path + '/logs')
    createDirectory(path + '/logs/' + datetime.today().strftime('%Y-%m-%d'))

    