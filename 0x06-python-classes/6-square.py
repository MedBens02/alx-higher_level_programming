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

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints square using #."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
