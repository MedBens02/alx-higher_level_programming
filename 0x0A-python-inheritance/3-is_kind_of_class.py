#!/usr/bin/python3
'''Checks if an obj is an instance of class or inherited class'''


def is_kind_of_class(obj, a_class):
    '''Returns True if instance'''
    if isinstance(obj, a_class):
        return True
    return False
