#!/usr/bin/env python
#encoding=utf8


def rotate_ch(ch, key):
    if ch > 'z' or 'a' > ch > 'Z' or 'A' > ch:
        return ch

    _ord = ord(ch)
    if (ch >= 'a' and _ord + key > ord('z')) or ('Z' >= ch and _ord + key > ord('Z')):
        key = key - 26
    return chr(_ord + key)

def rotate(text, key):
    return ''.join(rotate_ch(ch, key) for ch in text)
