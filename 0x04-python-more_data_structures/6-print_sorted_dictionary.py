#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = sorted(a_dictionary)
    for i in k:
        print(f"{i}: {a_dictionary[i]}")
