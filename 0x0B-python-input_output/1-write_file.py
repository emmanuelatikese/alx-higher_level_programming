#!/usr/bin/python3
"""this function writes in files"""


def write_file(filename="", text=""):
    """this thing continue to write from here"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
