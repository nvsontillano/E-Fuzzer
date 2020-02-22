"""
Check if all dependencies are installed or are have the required version.
"""

import sys

"""
Check Python version
"""
def checkPyVersion():
    if sys.version_info[0] < 3:
        print("Python version should be at least 3.0")
        # raise exception
        