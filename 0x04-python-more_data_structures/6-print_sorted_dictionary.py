#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = a_dictionary.copy()
    new_dict = sorted(new_dict)
    for k in new_dict:
        print("{}: {}".format(k, a_dictionary[k]))
