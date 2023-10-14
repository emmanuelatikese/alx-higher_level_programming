#!/usr/bin/python3
"""this function is known as safe_print_list"""


def safe_print_list(my_list=[], x=0):
    """this does safe print"""
    number = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            number += 1
        except IndexError:
            break
    print("")
    return number
