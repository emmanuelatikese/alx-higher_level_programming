#!/usr/bin/python3
"""This function just read files"""


def read_file(filename=""):
    """this is where the function initialize"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
