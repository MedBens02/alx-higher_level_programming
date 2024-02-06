#!/usr/bin/python3
'''Defines a subclass of rectangle: Square'''
Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    '''A Square'''

    def __init__(self, size):
        """Initialize a Square.

        Args:
            size: size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Area method'''
        return self.__size ** 2
