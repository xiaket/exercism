#!/usr/bin/env python
#encoding=utf8


def flatten(iterable):
    result = []
    for i in iterable:
        if (isinstance(i, list) or isinstance(i, tuple)) and i:
            result += flatten(i)
        elif i or i == 0:
            result.append(i)

    return result
