#!/usr/bin/python3
"""Add function for ints"""

def add_integer(a, b=98):
    """Return a + b.

    Floats are casted to ints.

    Raises:
        TypeError: if a or b not int or float.
    """
     if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
