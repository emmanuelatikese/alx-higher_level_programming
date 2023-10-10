#!/usr/bin/python3
"""this is another function """
import json


def save_to_json_file(my_obj, filename):
    """ok this function is doing a lot """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
