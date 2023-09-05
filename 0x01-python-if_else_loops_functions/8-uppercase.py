#!/usr/bin/python3
def uppercase(str):
    lower = [chr(r) for r in range(97, 123)]
    upper = [chr(y) for y in range(65, 91)]
    result = ''
    for x in str:
        if x in lower:
            x = upper[lower.index(x)]
        result += x
    print("{}".format(result))
