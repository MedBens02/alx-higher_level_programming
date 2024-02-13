#!/usr/bin/python3
'''Tests for Base class'''
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests Base class.'''

    def setUp(self):
        '''Instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test.'''
        pass

    def test_is_nb_objects_private(self):
        '''Tests if nb_objects is private.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_is_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as err:
            Base.__init__()
        mssg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), mssg)

    def test_constructor_args_2(self):
        '''Tests constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as err:
            Base.__init__(self, 1, 2)
        mssg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(err.exception), mssg)

    def test_consecutive_ids(self):
        '''Tests consecutive ids.'''
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_id_synced(self):
        '''Tests sync between class and inst id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_id_synced_extra(self):
        '''Tests sync between class and inst id.'''
        b = Base()
        b = Base("Test")
        b = Base(12)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_custom_id_int(self):
        '''Tests custom int id.'''
        i = 12
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_custom_id_str(self):
        '''Tests custom str id.'''
        i = "Test"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_id_keyword(self):
        '''Tests id as keyword arg.'''
        i = 124
        b = Base(id=i)
        self.assertEqual(b.id, i)

    # ----------------- Tests for #15 ------------------------
    def test_to_json_string(self):
        '''Tests to_json_string().'''
        with self.assertRaises(TypeError) as err:
            Base.to_json_string()
        st = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(err.exception), st)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 101, 'y': 20123, 'width': 24668, 'id': 244366,
             'height': 34244}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{"testmore": 121212}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"testmore": 121212}]')

        d = [{"testmore": 121212}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"testmore": 121212}, {"abc": 123}, {"HI": 0}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 24668, 'id': 244366,
             'height': 34244}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    # ----------------- Tests for #17 ------------------------
    def test_test_from_json_string(self):
        '''Tests to_json_string()'''
        with self.assertRaises(TypeError) as err:
            Base.from_json_string()
        s = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(err.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 24668, "id": 244366, "height": 34244}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 24668, 'id': 244366,
             'height': 34244}]
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"testmore": 121212}, {"abc": 123}, {"HI": 0}]
        s = '[{"testmore": 121212}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"testmore": 121212}]
        s = '[{"testmore": 121212}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 101, 'y': 20123, 'width': 24668, 'id': 244366,
             'height': 34244}]
        s = '[{"x": 101, "y": 20123, "width": 24668, "id": 244366, \
"height": 34244}]'
        self.assertEqual(Base.from_json_string(s), d)

        list_in = [
            {'id': 12, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_out = Rectangle.from_json_string(
            Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)

        # ----------------- Tests for #16 ------------------------
    def test_save_to_f(self):
        '''Tests save_to_f() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_f([r1, r2])

        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 105)

        Rectangle.save_to_f(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_f([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_f([r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 52)

        Square.save_to_f(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_f([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        r2 = Square(1)
        Square.save_to_f([r2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 38)

        # ----------------- Tests for #18 ------------------------
    def test_create(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        # ----------------- Tests for #19 ------------------------
    def test_load_from_f(self):
        '''Tests load_from_f() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_f(list_in)
        list_out = Rectangle.load_from_f()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_f(list_in)
        list_out = Square.load_from_f()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

if __name__ == "__main__":
    unittest.main()
