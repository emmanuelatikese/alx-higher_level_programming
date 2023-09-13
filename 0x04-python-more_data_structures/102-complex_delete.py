#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    r = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            r.append(key)
    for x in r:
        del a_dictionary[x]
    return a_dictionary
