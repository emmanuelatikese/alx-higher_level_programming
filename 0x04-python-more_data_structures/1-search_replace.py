#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [x for x in my_list]
    if search in my_list:
        for x in range(0, len(new_list)):
            if new_list[x] == search:
                new_list[x] = replace
        return new_list
