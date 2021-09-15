#!/usr/bin/python3
"""
    takes a URL sends request and prints the body of the response
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('utf8'))
    except urllib.error.HTTPError as errorcode:
        print("Error code: {}".format(errorcode.code))
