#!/usr/bin/env python
#encoding=utf8


class Luhn(object):
    def __init__(self, num):
        num = num.replace(" ", "")
        self.valid = all(ch.isdigit() for ch in num) and len(num) > 1
        self.num = list(reversed(num))

    def is_valid(self):
        if not self.valid:
            return False
        doubles = sum(int(ch) * 2 - 9 if int(ch) * 2 > 9 else int(ch) * 2 for ch in self.num[1::2])
        singles = sum(int(ch) for ch in self.num[::2])
        return (doubles + singles) % 10 == 0
