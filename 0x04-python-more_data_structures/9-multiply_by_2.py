#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for key, val in new.items():
        new[key] = val*2
    return new
