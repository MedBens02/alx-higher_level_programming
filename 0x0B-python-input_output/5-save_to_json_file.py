#!/usr/bin/python3
'''Defines a JSON obj writting fct'''
import json


def save_to_json_file(my_obj, filename):
    """Writes obj to file using JSON.

    Args:
        my_obj: the obj to write.
        filename: the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
