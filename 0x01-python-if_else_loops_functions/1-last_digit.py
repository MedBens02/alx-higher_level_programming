#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10 if number > 10 else number % -10
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
