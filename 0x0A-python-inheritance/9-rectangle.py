#!/usr/bin/python3
"""creates a BaseGeometry rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle inheriting basegeometry"""

    def __init__(self, width, height):
        """initializes rectangle"""
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width

    def area(self):
        """defines area"""

        return self.__width * self.__height

    def __str__(self):
        """string"""

        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
