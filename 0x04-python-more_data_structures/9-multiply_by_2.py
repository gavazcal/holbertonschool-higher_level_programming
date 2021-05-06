#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    result = {key: x*2 for key, x in a_dictionary.items()}
    return result
