#!/usr/bin/python3
def best_score(a_dictionary):
    result = 0
    if a_dictionary is None:
        return None
    for val in a_dictionary.values():
        result = result if val < result else val
    for key in a_dictionary.keys():
        if a_dictionary[key] == result:
            return key
