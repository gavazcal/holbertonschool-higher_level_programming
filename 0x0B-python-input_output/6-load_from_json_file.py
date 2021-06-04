#!/usr/bin/python3
"""loads from json"""


def load_from_json_file(filename):
    """loads from json"""

    import json
    with open(filename) as a_file:
        return json.load(a_file)
