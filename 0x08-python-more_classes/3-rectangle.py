#!/usr/bin/python3
"""defines a rectangle class"""


class Rectangle:
    """initiates rectangle class with width and height"""
    def __init__(self, width=0, height=0):
        """initializes width and height"""
        self.width = width
        self.height = height

    def __str__(self):
        """printing method"""
        if self.area() == 0:
            return ("")
        return (("#" * self.width + "\n") * self.height)[0:-1]

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Defines perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2
