#!/usr/bin/python3
def magic_string():
    magic_string.nbr = getattr(magic_string, 'nbr', 0) + 1
    return "BestSchool, " * (magic_string.nbr - 1) + "BestSchool"
