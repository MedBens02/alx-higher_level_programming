#!/usr/bin/python3
'''Defines a fct that appends text to a file'''


def append_write(filename="", text=""):
    """Returns the nbr of appended chars.

    Args:
        filename: the file.
        text: the str to append.
    Return:
        nbr of chrs appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
