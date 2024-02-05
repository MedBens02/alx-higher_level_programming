#!/usr/bin/python3
"""Defines an inherited class"""


class Mylist(list):
    """custom class"""
    def print_sorted(self):
        """Method to print sorted list"""
        print(sorted(self))
