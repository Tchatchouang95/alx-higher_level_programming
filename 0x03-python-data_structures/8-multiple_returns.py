#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    else:
        size = len(sentence)
        first = sentence[0]
        return size, first
