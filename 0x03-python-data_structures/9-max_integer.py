#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list:
        x = my_list[0]
        for n in my_list:
            if n > x:
                x = n
        return x
    else:
        return None

