#!/usr/bin/python3
"""returns JSON representation of a string"""

def to_json_string(my_obj):
    """returns JSON"""

    import json
    return json.dumps(my_obj)
