#!/usr/bin/python3
"""
    Displays the value of a variable
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as content:
        print(content.getheader('X-Request-Id'))
