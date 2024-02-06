#!/usr/bin/python3
'''Defines a JSON representation fct'''
import json

def to_json_string(my_obj):
    """Returns the JSON representation of object.

    Args:
        my_obj: obj to serialize.
    Return:
        its JSON representation.
    """
    return json.dumps(my_obj)
