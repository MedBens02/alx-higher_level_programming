#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    newT = ()

    T1 = tuple_a + (0, 0)
    T2 = tuple_b + (0, 0)

    newT = T1[0] + T2[0], T1[1] + T2[1]

    return newT
