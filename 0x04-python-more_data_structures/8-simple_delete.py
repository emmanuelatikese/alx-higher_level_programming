#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if isinstance(key, str):
        a_dictionary.pop(key)
    return a_dictionary
