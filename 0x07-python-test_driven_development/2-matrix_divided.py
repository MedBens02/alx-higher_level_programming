#!/usr/bin/python3
"""Defines a matrix div fct."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix: List of lists containing ints or floats.
        div: Dividor of the elts.

    Raises:
        TypeError: Matrix contains non-numbers.
        TypeError: Diff size rows in matrix.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    Returns:
        The result of division as a new matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) \
            or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
