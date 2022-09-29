#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if isinstance(key, str):
        for k in a_dictionary.keys():
            if key == k:
                a_dictionary[k] = value
            elif a_dictionary[k] == value:
                a_dictionary[key] = value
            a_dictionary[key] = value
    return a_dictionary
