#!/usr/bin/python3
"""this is the append function."""


def append_write(filename="", text=""):
    """this is all about appending"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
