#!/usr/bin/python3
"""inheritance exercise"""


class MyList(list):
    """class to inherit from"""
    def print_sorted(self):
        """prints a sorted list"""

        print(sorted(self))

