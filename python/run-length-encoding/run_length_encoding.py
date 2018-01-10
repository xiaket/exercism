#!/usr/bin/env python
# encoding=utf8

from string import digits


def decode(string):
    decoded = ""
    multiplier = None
    for ch in string:
        if multiplier is None:
            if ch not in digits:
                decoded += ch
            else:
                multiplier = int(ch)
        else:
            if ch not in digits:
                decoded += multiplier * ch
                multiplier = None
            else:
                multiplier = multiplier * 10 + int(ch)
    return decoded

def encode(string):
    last = None
    count = 0
    encoded = ""
    for ch in string:
        if ch == last:
            count += 1
        else:
            if count == 0:
                count = 1
            elif count == 1:
                encoded += last
            else:
                encoded += (str(count) + last)
                count = 1
            last = ch

    if count > 1:
        encoded += (str(count) + last)
    elif count == 1:
        encoded += last
    return encoded


#encode("aabbbcccc")
