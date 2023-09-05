#!/usr/bin/python3

for x in range(0,100):
    if x in range(1, 10):
        print(f"0{x}, ",end="")
    elif x in range(10, 99):
        print(f"{x}, ",end="")
    else:
        print(x)
