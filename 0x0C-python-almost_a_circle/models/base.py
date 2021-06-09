#!/usr/bin/python3
"""creates base class"""

import json

class Base():
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON str rep"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
