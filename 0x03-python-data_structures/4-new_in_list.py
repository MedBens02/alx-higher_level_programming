#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    newlist = my_list

    if idx < 0 or idx > len(newlist) - 1:
        return newlist
    else:
        newlist[idx] = element
        return newlist
