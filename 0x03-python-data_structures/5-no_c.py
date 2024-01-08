#!/usr/bin/python3

def no_c(my_string):
    newstr = my_string.maketrans('', '', 'cC')
    return newstr
