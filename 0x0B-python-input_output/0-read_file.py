#!/usr/bin/python3
"""reads txt files"""


def read_file(filename=""):
    """reads txt files"""
    with open(filename, encoding='UTF8') as a_file:
        for x in a_file:
            print(x, end='')
