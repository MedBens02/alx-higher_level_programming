#!/usr/bin/python3
'''Checks if obj is instance of inherited class'''


def inherits_from(obj, a_class):
    '''Returns True if instance'''
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
