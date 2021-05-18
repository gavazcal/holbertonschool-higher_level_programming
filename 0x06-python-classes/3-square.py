#!/usr/bin/python3
"""defines a square class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """creates size instance"""
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be a integer")

    def area(self):
        """calculates area of square"""
        return self.__size ** 2
