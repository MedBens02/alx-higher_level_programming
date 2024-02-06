#!/usr/bin/python3
'''Defines a fct that adds attributes to objs'''


def add_attribute(obj, att, value):
    """Adds new atts to objs when possible.

    Args:
        obj: Object to add atts to.
        att: Attributes to add.
        value: value of att.
    Raises:
        TypeError: If att can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
