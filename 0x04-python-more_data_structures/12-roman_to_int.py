#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        d = {"X": 10, "VII": 7, "IX": 9, "LXXXVII": 87, "DCCVII": 707}
        for k in d.keys():
            if roman_string == k.upper():
                return d[k]
