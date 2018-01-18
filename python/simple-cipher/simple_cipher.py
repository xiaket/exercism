#!/usr/bin/env python
#encoding=utf8

import random
from string import ascii_lowercase as lowercase, ascii_letters as letters


class Cipher(object):
    def __init__(self, key=None):
        if hasattr(self, "key"):
            return

        if not key:
            self.key = ''.join(random.choice(lowercase) for i in range(100))
            return

        if not all(ch in lowercase for ch in key):
            raise ValueError("bad key")

        self.key = (int(100 / len(key)) + 1) * key

    def encode(self, text):
        text = [ch.lower() for ch in text if ch in letters]
        en = lambda ch, key: chr((ord(ch) + ord(key) - 2 * ord('a') + 26) % 26 + ord('a'))
        return ''.join(en(ch, self.key[i]) for i, ch in enumerate(text))

    def decode(self, text):
        de = lambda ch, key: chr((ord(ch) + 26 - ord(key)) % 26 + ord('a'))
        return ''.join(de(ch, self.key[i]) for i, ch in enumerate(text))


class Caesar(Cipher):
    key = 'd' * 100
