#!/usr/bin/python3
"""
    Fetches status of a site
"""

import requests

if __name__ == "__main__":
    resp = requests.get('https://intranet.hbtn.io/status')
    body = resp.content.decode('utf8')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(body), body))
