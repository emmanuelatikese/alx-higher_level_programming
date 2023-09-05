#!/usr/bin/python3
def remove_char_at(str, n):
    result = ''
    for x in str:
        if str[n] == x:
            continue
        else:
            result += x
    return result
