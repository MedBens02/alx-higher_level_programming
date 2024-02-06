#!/usr/bin/python3
'''Empty class BaseGeometry'''


class BaseGeometry:
    '''BaseGeometry class'''

    def area(self):
        '''area method'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates param as int.

        Args:
            name: param name.
            value: the value to validate.
        Raises:
            TypeError: If value is not int.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
