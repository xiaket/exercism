#!/usr/bin/env python
#encoding=utf8


def verify(isbn):
    isbn = [ch for ch in isbn if ch != '-']
    if len(isbn) != 10:
        return False
    if not all(ch.isdigit() for ch in isbn[:9]):
        return False

    check = 11 - sum(int(isbn[i]) * (10 - i) for i in range(9)) % 11
    return isbn[-1] == str(check) if isbn[-1] != 'X' else check == 10
