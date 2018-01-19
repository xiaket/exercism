#!/usr/bin/env python
#encoding=utf8

from string import ascii_letters, digits


def get_column_row(size):
    r = int(size ** 0.5)
    if size == r ** 2:
        return r, r
    elif size >= (r + 1) * r:
        return r + 1, r + 1
    else:
        return r + 1, r


def encode(plain_text):
    valid_chs = ascii_letters + digits
    text = ''.join(ch.lower() for ch in plain_text if ch in valid_chs)
    row, column = get_column_row(len(text))
    text += " " * (row * column - len(text))
    return " ".join(["".join(text[j*row+i] for j in range(column)) for i in range(row)])
