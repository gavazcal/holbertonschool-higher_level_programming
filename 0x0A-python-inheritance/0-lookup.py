#!/usr/bin/python3
"""function to print all available attributes of an object"""


def lookup(obj):
    """lookup function"""
    return list(dir(obj))
