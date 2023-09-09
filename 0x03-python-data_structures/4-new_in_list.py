#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = [y for y in my_list]
    i = 0
    while i < len(new_list):
        if i == idx:
            new_list[i] = element
            return new_list
        i += 1
    return 
