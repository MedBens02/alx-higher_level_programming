#!/usr/bin/python3
"""Defines a fct that indentates a text"""


def text_indentation(text):
    """Prints text + 2 new lines after each of these: ., ? and :.

    Args:
        text: txt to print.
    Raises:
        TypeError: If txt not str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
