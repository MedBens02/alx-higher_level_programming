#!/usr/bin/python3

"""This is an empty class Rectangle."""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """New Rectangle.

        Args:
            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Access the width of rectange"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Access the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Prints the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join([
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        ])

    def __repr__(self):
        """Return a representation of rectangle with #"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print msg after deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle in area.

        Args:
            rect_1: rectangle 1.
            rect_2: rectangle 2.
        Raises:
            TypeError: If rect_1 or rect_2 not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """return a new square under rectangle instance

        Args:
            size: width and height
        """
        return cls(size,size)
