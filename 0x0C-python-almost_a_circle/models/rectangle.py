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
    def x(self):
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
    def y(self):
        """access the y coor of the new rect."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints a representation of rect using '#'"""
        [print("") for y in range(self.y)]

        for _ in range(self.__height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Overrides the str representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def __updateDetail(self, id=None, width=None, height=None, x=None, y=None):
        '''Updates a rect using *args or **kwargs'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args):
        """Updates a rectangle

        Args:
            *args: the update values in order:
                id / width / height / x / y
        """
        if args:
            self.__updateDetail(*args)
