#!/usr/bin/python3
for x in range(122, 96, -1):
    if (x + 1) % 2 == 0:
        print(f"{chr(x).upper()}", end="")
    else:
        print(f"{chr(x)}", end="")
