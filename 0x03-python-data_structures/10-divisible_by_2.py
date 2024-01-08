#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    div = my_list.copy()

    for i in range(len(div)):
        if (my_list[i] % 2) == 0:
            div[i] = True
        else:
            div[i] = False
    return div
