#!/usr/bin/python3
for n in range(0, 10):
    for n2 in range(0, 10):
        if n is 8 and n2 is 9:
            print("{:d}{:d}".format(n, n2))
        elif n < n2:
            print("{:d}{:d}".format(n, n2), end=", ")
