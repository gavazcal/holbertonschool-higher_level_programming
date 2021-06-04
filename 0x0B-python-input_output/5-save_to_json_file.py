#!/usr/bin/python3
"""json save"""


def save_to_json_file(my_obj, filename):
    """json save"""
    import json
    with open(filename, 'w') as a_file:
        json.dump(my_obj, a_file)
