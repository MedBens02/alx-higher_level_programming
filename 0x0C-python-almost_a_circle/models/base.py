#!/usr/bin/python3
'''Defines a Base class'''
import json
import csv
import turtle


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

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from  file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return [cls.create(**dic)
                        for dic in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV and saves it in a file"""
        filename = cls.__name__ + ".csv"

        if list_objs is not None:
            if cls.__name__ == "Rectangle":
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            elif cls.__name__ == "Square":
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = []

        else:
            list_objs = []

        with open(filename, "w", newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="", encoding='utf-8') as f:
                inst = []
                reader = csv.reader(f)
                for row in reader:
                    row = [int(i) for i in row]
                    if cls.__name__ == "Rectangle":
                        dic = {'id': row[0], 'width': row[1], 'height': row[2],
                               'x': row[3], 'y': row[4]}
                    elif cls.__name__ == "Square":
                        dic = {'id': row[0], 'size': row[1],
                               'x': row[2], 'y': row[3]}
                    inst.append(cls.create(**dic))
            return inst
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rects and squares uing turtle"""
        t = turtle.Turtle()
        t.screen.bgcolor("#4CF78B")
        t.pensize(2)

        t.color("#43B3FA")
        for rect in list_rectangles:
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        t.color("#40E235")
        for square in list_squares:
            t.up()
            t.goto(square.x, square.y)
            t.down()
            for i in range(4):
                t.forward(square.height)
                t.left(90)

        turtle.done()
