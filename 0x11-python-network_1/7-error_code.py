#!/usr/bin/python3
"""
    takes a URL, sends a request, displays body of response
"""

import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp.status_code < 400:
        print(resp.content.decoede('utf8'))
    else:
        print("Error code: {}".format(resp.status_code))
