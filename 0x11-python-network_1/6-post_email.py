#!/usr/bin/python3
"""
    sends a POST request to a url with and displays response
"""

import requests
import sys

if __name__ == "__main__":
    resp = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(resp.content.decode('utf8'))
