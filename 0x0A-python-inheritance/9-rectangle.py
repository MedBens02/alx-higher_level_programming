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


     def area(self):
         '''Returns the area of rectangle'''
         return self.__width * self.__height

     def __str__(self):
         '''Representation method.'''
         pstr = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
         return pstr
