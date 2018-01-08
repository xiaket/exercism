#!/usr/bin/env python
#encoding=utf8

def is_isogram(string):
    stripped = string.replace("-", "").replace(" ", "").lower()
    return len(stripped) == len(set(stripped))
