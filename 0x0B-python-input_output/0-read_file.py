#!/usr/bin/python3
'''Defines a fct that reads a tect file'''


def read_file(filename=""):
    '''Opens and reads the file'''
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
