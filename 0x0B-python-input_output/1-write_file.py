#!/usr/bin/python3
"""writes to a txt file"""


def write_file(filename="", text=""):
    """writes to a txt file"""

    with open(filename, 'w') as a_file:
        return a_file.write(text)
