#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(c), end="")
    c = c - 1
    if c >= ord('A'):
        print("{:c}".format(c - 32), end="")
