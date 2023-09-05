#!/usr/bin/python3
def remove_char_at(str, n):
    result = ''
    if n >= 0 and n <= len(str):
        for x in str:
            if str[n] == x:
                continue
            else:
                result += x
        return result
    return str
