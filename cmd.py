"""
Parse command line arguments
"""

import os
import re
import sys
from argparse import ArgumentParser

"""
List of valid options
"""
OPTIONS = (
    "url",
    "data",
    "cookie",
    "port",
    "basicAuth",
    "method",
    "static",
    "file",
)

"""
This function parses the command line arguments
"""
def parser():
    # Get arguments from command line
    argv = sys.argv

    _ = os.path.basename(argv[0])

    # OS of the machine
    PLATFORM = os.name
    IS_WIN = PLATFORM == "nt"

    # Create the parser    
    usage = "%s%s [options]" % ("%s " % os.path.basename(sys.executable) if not IS_WIN else "", "\"%s\"" % _ if " " in _ else _)
    parser = ArgumentParser(usage=usage)

    # Target options
    target = parser.add_argument_group("Target", "This has to be provided to define the target(s)")

    target.add_argument("-u", "--url", dest="url", help="Target URL (e.g. \"http://www.example.com/index.php?id=1\")")

    # Request options
    request = parser.add_argument_group("Request", "These options can be used to specify how to connect to the target URL")

    request.add_argument("--method", dest="method", help="Force usage of given HTTP method (e.g. PUT)")
    request.add_argument("--data", dest="data", help="Data string to be sent through POST (e.g. \"id=1\")")
    request.add_argument("--static", dest="static", help="Position of static data string (e.g. \"2,4\")")
    request.add_argument("--cookie", dest="cookie", help="HTTP Cookie header value (e.g. \"PHPSESSID=a8d127e..\")")
    request.add_argument("--port", dest="port", help="Port where the target application accepts the input")
    request.add_argument("--basicAuth", dest="basicAuth", help="HTTP Basic authentication credentials (name:password)")

    # Injection options
    injection = parser.add_argument_group("Injection", "These options can be used to provide custom injection payloads")

    injection.add_argument("--file", dest="file", help="Filename of file with input strings")

    # If --url is not used 
    try:
        if re.search(r"\A(http|www\.|\w[\w.-]+\.\w{2,})", argv[1]) is not None:
            argv[1] = "--url=%s" % argv[1]
    except IndexError:
        pass
        # WHAT TO DO HERE
    
    # Call parsing method
    (args, _) = parser.parse_known_args(argv) if hasattr(parser, "parse_known_args") else parser.parse_args(argv)

    _ = {}
    for arg in vars(args):
        _[arg] =  getattr(args, arg)
    
    return _

