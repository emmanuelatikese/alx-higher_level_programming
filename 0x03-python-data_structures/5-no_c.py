#!/usr/bin/python3
def no_c(my_string):
    c = ""
    for i in my_string:
        if "C" in i or "c" in i:
            continue
        else:
            c = c + i
    return c
