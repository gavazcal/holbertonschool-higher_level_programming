#!/usr/bin/python3
"""defines a square class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """defines size instance"""
        self.__size = size

    def area(self):
        """calculates the square area"""
        return self.__size ** 2

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        try:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def my_print(self):
        """prints square"""
        size = self.__size

        if size == 0:
            print()
        else:
            for x in range(size):
                for y in range(size):
                    print("#", end="")
                print()
