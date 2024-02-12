#!/usr/bin/python3
'''Defines a Base class'''


class Base:
    """This is the base of the upvoming classes.

    Pricate class attr:
        __nb_objects: nbr of Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base.

        Args:
            id: identity of created base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
