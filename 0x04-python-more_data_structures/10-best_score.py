#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    a = [x for x in a_dictionary.values()]
    for k in a_dictionary.keys():
        if a_dictionary[k] == max(a):
            return k
