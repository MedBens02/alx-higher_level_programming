#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_empty_list(self):
        """Tests an empty list."""
    	self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
	"""Tests a list with a single element."""
	self.assertEqual(max_integer([7]), 7)

    def test_ordered_list(self):
	"""Tests an ordered list of integers."""
	self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
	"""Tests an unordered list of integers."""
	self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_beginning(self):
	"""Tests a list with a beginning max value."""
	self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_floats(self):
	"""Tests a list of floats."""
	self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
	"""Tests a list of ints and floats."""
	self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_string(self):
	"""Tests a string."""
	self.assertEqual(max_integer("Brennan"), 'r')

    def test_list_of_strings(self):
	"""Tests a list of strings."""
	self.assertEqual(max_integer(["Brennan", "is", "my", "name"]), "name")

    def test_empty_string(self):
	"""Tests an empty string."""
	self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
	unittest.main()
