#!/usr/bin/python3
for x in range(9):
    for y in range(1, 10):
        if x > y or x == y:
            continue
        if y != 5:
            print("{:d}{:d}".format(x, y), end=', ')
        else:
            print("{:d}{:d}".format(x, y), end=', ')
