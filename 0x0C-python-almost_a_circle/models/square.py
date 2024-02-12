#!/usr/bin/python3
'''Defines a Square child class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents a square'''

    def __init__(self, size, x=0, y=0, id=None):
        """Same as rect with size is either height or width"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representation of square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """Access the size of Square"""
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __updateDetail(self, id=None, size=None, x=None, y=None):
        '''Updates a square using *args or **kwargs'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates a square

        Args:
            *args: the update values in order:
                id / size / x / y
            **kwargs: a dict (key/value) of the attrs
        """
        if args:
            self.__updateDetail(*args)
        elif kwargs:
            self.__updateDetail(**kwargs)

    def to_dictionary(self):
        """Returns the dict representation of a square"""
        return {'id': self.id, 'width': self.width,
                'x': self.x, 'y': self.y}
