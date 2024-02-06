#!/usr/bin/python3
'''Defines a file JSON deserialization fct'''
import json


def load_from_json_file(filename):
    '''Creates an obj from a JSON file'''
    with open(filename, "r", encoding="utf*8") as f:
        return json.load(f)
