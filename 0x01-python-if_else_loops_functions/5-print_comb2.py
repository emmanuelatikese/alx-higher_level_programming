#!/usr/bin/python3

for x in range(0, 99):
    if x in range(1, 10):
        x = "0{}".format(x)
    print("{}, ".format(x), end="")
print(99)
