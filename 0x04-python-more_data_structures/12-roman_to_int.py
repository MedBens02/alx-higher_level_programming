#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) != str:
        return 0

    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    tmp = 0
    val = 0

    for R in reversed(roman_string):
        val = romans.get(R, 0)

        if val < tmp:
            result -= val
        else:
            result += val
        tmp = val

    return result
