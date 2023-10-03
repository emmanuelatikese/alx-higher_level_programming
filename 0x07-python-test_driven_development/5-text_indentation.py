#!/usr/bin/python3
"""this function split sentence base on character"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    result = ""
    for x in text:
        result += x
        if x == "." or x == ":" or x == "?":
            print(result)
            print("\n")
            result = ""
