#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    repeated = []
    for x in set_1:
        for y in set_2:
            if x == y:
                repeated.append(x)
    for a in repeated:
        set_1.remove(a)
        set_2.remove(a)
    result = [x for x in set_1] + [y for y in set_2]
    return result
