#!/usr/bin/python3
def multiple_returns(sentence):
    return (None, 0) if sentence == "" else (len(sentence), sentence[0])
