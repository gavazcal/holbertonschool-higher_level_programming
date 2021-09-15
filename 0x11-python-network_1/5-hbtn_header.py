#!/usr/bin/python3
"""
    takes a url, sends a request and prints out a variable
"""

import sys
import requests

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    resp_dict = resp.headers
    print(resp_dict.get('X-Request-Id'))
