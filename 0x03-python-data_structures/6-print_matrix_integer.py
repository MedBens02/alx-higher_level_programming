#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elt in row:
            print("{:d}".format(elt), end=" " if elt != row[-1] else "")
        print()
