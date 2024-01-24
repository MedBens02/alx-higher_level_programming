#!/usr/bin/python3

"""This is a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """New Square.

        Args:
            size: The size of a square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
