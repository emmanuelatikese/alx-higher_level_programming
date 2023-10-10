#!/usr/bin/python3
"""this is another funciton """
from sys import argv
import os

ld = __import__("6-load_from_json_file").load_from_json_file
sav = __import__("5-save_to_json_file").save_to_json_file
name_file = "add_item.json"


if __name__ == "__main__":
    if os.path.exists(name_file):
        d = ld(name_file)
        for x in argv[1:]:
            d.append(x)
        sav(d, name_file)
    else:
        sav(argv[1:], name_file)
    ld(name_file)
