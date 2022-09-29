#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = list(set_1)
    b = list(set_2)
    for i in a:
        if i in b:
            b.remove(i)
            continue
        b.append(i)
    return b
