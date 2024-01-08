#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if my_list:
        newlist = my_list.copy()

        if idx < 0 or idx > len(newlist) - 1:
            return newlist
        else:
            newlist[idx] = element
            return newlist
