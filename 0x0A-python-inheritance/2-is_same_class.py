#!/usr/bin/python3
'''Defines a fct that checks if an obj is an instance'''


def is_same_class(obj, a_class):
    '''Returns True is obj is exactly an instance of a class.'''
    if type(obj) == a_class:
        return True
    return False
