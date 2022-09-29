#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key, value in zip(a_dictionary.keys(), a_dictionary.values()):
        a_dictionary[key] = value*2
    return a_dictionary
