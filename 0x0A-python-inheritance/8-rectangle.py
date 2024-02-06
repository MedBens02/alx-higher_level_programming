#!/usr/bin/python3
'''Defines a Rectangle class that inherites form BaseGeometry'''
BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    '''A rectangle with BG'''
    def __init__(self, width, height):
        """Intialize a rectangle.

        Args:
            width: its width.
            height: its height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
