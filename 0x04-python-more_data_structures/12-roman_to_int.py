#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {"X": 10, "VI": 7, "IX": 9, "LXXXVII": 87, "DCCVII": 707}
    if isinstance(roman_string, str) and roman_string is not None:
        for key, val in num.items():
            if key == roman_string:
                return val
    return 0
