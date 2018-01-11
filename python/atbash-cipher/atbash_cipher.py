#!/usr/bin/env python
#encoding=utf8

from string import punctuation, ascii_lowercase as LOWER

SUM = ord('a') + ord('z')
PUNC = punctuation + ' '


def encode(plain_text):
    text = [ch for ch in plain_text.lower() if ch not in PUNC]
    encoded = [chr(SUM - ord(ch)) if ch in LOWER else ch for ch in text]
    return (' '.join(''.join(encoded[i*5:i*5+5]) for i in range(1 + len(encoded) / 5))).strip()


def decode(ciphered_text):
    text = [ch for ch in ciphered_text if ch != " "]
    return ''.join(chr(SUM - ord(c)) if 'z' >= c >='a' else c for c in text)
