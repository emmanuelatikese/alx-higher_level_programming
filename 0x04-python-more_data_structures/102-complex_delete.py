#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    a = a_dictionary.copy()
    for k in a.keys():
        if a[k] == value:
            a_dictionary.pop(k)
    return a_dictionary
