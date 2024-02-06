#!/usr/bin/python3
'''Defines a search & write fct'''

def append_after(filename="", search_string="", new_string=""):
    """Write a text after a certain str.

    Args:
        filename: the file to edit.
        search_string: the str to write after.
        new_string: the str to write.
    """
    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
