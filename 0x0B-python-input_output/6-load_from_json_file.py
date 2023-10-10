#!/usr/bin/python3
"""this function is different"""
import json


def load_from_json_file(filename):
    """it quite different"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
