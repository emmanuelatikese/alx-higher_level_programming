#!/usr/bin/python3
"""looking for the peak in a list"""

def find_peak(list_of_integers):
    """This is thing is all about peaks"""
    if list_of_integers is None:
        return None
    for x in range(len(list_of_integers)):
            a = list_of_integers[x - 1]
            b = list_of_integers[x + 1]
            curr = list_of_integers[x]
            if a <= curr and b <= curr:
                return curr
