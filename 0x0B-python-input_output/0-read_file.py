#!/usr/bin/python3
"""This function just read files"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        nw_file = f.read()
    return print(nw_file)
