#!/usr/bin/python3
'''Defines a deserialization fct'''
import json


def from_json_string(my_str):
    '''Returns a deserialized representation of my_str'''
    return json.loads(my_str)
