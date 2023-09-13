#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary.copy()
    new_dict.pop(str(key))
    return new_dict
