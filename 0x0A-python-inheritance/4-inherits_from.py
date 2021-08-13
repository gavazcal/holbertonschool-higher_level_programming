#!/usr/bin/python3
"""boolean check for if an obj is an instance"""


def inherits_from(obj, a_class):
    """boolean func"""
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
