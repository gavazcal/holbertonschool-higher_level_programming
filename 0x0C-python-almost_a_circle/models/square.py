#!/usr/bin/python3
"""square class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """initializes a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """populates values"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, size_val):
        """size setter method"""
        if type(size_val) is not int:
            raise TypeError("width must be an integer")
        if size_val <= 0:
            raise ValueError("width must be >= 0")
        self.height = size_val
        self.width = size_val

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates a varying number of args"""
        if not args and not kwargs:
            return
        if len(args != 0):
            atts = ["id", "size", "x", "y"]
            for idx, attribute in enumerate(args):
                setattr(self, atts, attribute)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns as a dict"""
        the_dic = {}
        atts = ["id", "size", "x", "y"]
        for key in atts:
            value = getattr(self, key)
            the_dic[key] = value
        return the_dic
