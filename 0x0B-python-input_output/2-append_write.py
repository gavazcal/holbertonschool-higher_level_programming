#!/usr/bin/python3
"""appends to a txt file"""


def append_write(filename="", text=""):
    """appends to a txt file"""

    with open(filename, 'a') as a_file:
        return a_file.write(text)
