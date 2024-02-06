#!/usr/bin/python3
'''Defines a Pascal triangle fct'''


def pascal_triangle(n):
    '''Returns pascal triangle for n row'''
    if n <= 0:
        return []

    tri = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev = tri[i - 1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
        tri.append(row)

    return tri
