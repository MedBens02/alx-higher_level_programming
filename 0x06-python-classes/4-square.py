#!/usr/bin/python3

"""This is a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """New Square.

        Args:
            size: The size of a square.
        """
        self.__size = size

    @property
    def size(self):
        """Access the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of square"""
        return self.__size ** 2
