#!/usr/bin/python3
"""
    takes a URL and email and sends a POST request
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    URL = sys.argv[1]
    email = urllib.parse.urlencode({'email': sys.argv[2]})
    email = email.encode('utf8')
    with urllib.request.urlopen(URL, email) as resp:
        print(resp.read().decode('utf8'))
