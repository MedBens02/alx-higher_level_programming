#!/usr/bin/python3
'''Defines a Square child class'''
from models.rectangle import Rectanglei


class Square(Rectangle):
    '''Represents a square'''

    def __init__(self, size, x=0, y=0, id=None):
        """Same as rect with size is either height or width"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representation of square"""
        return "[Square] ({}) {}/{} - {}"format(
                self.id, self.x, self.y, self.height)
