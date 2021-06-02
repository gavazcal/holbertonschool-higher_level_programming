#!/usr/bin/python3
"""boolean check for if an obj is an instance"""


def inherits_from(obj, a_class):
    """boolean func"""
    return issubclass(type(obj), a_class)
