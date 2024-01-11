#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    n = 0
    d = 0

    for x, y in my_list:
        n += x * y
        d += y

    return n / d
