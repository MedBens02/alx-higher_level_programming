#!/usr/bin/python3
"""Defines a fct that prints a square"""


def print_square(size):
    """Prints square using #.

    Args:
        size: side lenght of square.
    Raises:
        TypeError: if size not int.
        ValueError: if size < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
