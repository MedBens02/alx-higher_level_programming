#!/usr/bin/python3
'''Defines a Student class.'''


class Student:
    '''Represents a Student.'''

    def __init__(self, first_name, last_name, age):
        """Initialize nes Student.

        Args:
            first_name: His first name.
            last_name: His last name.
            age: his age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a Student'''
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student'''
        for key, value in json.items():
            setattr(self, key, value)
