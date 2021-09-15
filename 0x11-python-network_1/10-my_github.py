#!/usr/bin/python3
"""
    prints my github id
"""

import requests
import sys

if __name__ == "__main__":
    site = 'https://api.github.com/user'
    uid = sys.argv[1]
    pw = sys.argv[2]
    resp = requests.get(site, auth=(uid, pw))
    acc = resp.json()
    print(acc.get('id'))
