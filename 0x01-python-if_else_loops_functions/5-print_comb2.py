#!/usr/bin/python3

for x in range(0, 100):
    if x in range(1, 10):
        print("0{}, ".format(x), end="")
    elif x in range(10, 99):
        print("{}, ".format(x), end="")
    else:
        print(x)
