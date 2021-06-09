#!/usr/bin/python3
"""Rectangle INIT"""


from models.base import Base


class Rectangle(Base):
    """creates rectangle class and inits it with values"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """attributes for rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method width"""
        return self.__width

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @width.setter
    def width(self, width_val):
        """width setter method"""
        if type(width_val) is not int:
            raise TypeError("width must be an integer")
        if width_val <= 0:
            raise ValueError("width must be > 0")
        self.__width = width_val

    @height.setter
    def height(self, height_val):
        """height setter method"""
        if type(height_val) is not int:
            raise TypeError("height must be an integer")
        if height_val <= 0:
            raise ValueError("height must be > 0")
        self.__height = height_val

    @x.setter
    def x(self, x_val):
        """x setter method"""
        if type(x_val) is not int:
            raise TypeError("x must be an integer")
        if x_val < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_val

    @y.setter
    def y(self, y_val):
        """y setter method"""
        if type(y_val) is not int:
            raise TypeError("y must be an integer")
        if y_val < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_val

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints out rectangle"""
        for w_idx in range(self.y):
            print('')
        for idx in range(self.height):
            for h_idx in range(self.x):
                print(" ", end="")
            for hashtag in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates a varying number of attributes"""
        if len(args) != 0:
            atts = ["id", "width", "height", "x", "y"]
            for idx, att, in enumerate(args):
                setattr(self, atts, att)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

