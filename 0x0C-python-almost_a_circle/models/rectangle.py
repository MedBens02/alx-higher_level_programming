#!/usr/bin/python3
'''Defines a Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''Represents a rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle.

        Args:
            width: Rect's width
            height: its height
            x, y: the coordinates of a new rect
            id: its identity
        Raises:
            TypeError: w, h, x or y not ints
            ValueError: one of them is < 0 with x and y not 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Access the width of rectange"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Access the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self, value):
        """access the x coor of the new rect."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self, value):
        """access the y coor of the new rect."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
