#!/usr/bin/python3
'''Defines a fct that writes a str to a file'''


def write_file(filename="", text=""):
    """Returns the number of chars written

    Args:
        fileneme: the file.
        text: the str to write.
    Return:
        The number of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
