#!/usr/bin/python3
"""defines a square class"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square:
    """inherits from rectangle"""
    def __init__(self, size):
        """size instantiation"""
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(self, size)
        self.__size = size
