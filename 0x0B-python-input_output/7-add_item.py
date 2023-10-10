#!/usr/bin/python3
"""this is another funciton """
from sys import argv

ld = __import__("6-load_from_json_file").load_from_json_file
sav = __import__("5-save_to_json_file").save_to_json_file
name_file = "add_item.json"


if __name__ == "__main__":
    sav(argv[1:], name_file)
    ld(name_file)
