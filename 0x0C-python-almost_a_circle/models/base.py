#!/usr/bin/python3
'''Defines a Base class'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON serialization of a list of dicts

        Args:
            list_dictionaries: a list of dicts.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON serialization of a list of objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Deserialization of a JSON str

        Args:
            json_string: the JSON str
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attrs already set

        Args:
            **dictionary: dict containing attrs
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy
