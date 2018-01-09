#!/usr/bin/env python
# encoding=utf8

from string import ascii_uppercase, ascii_letters, digits


YELL = set(ascii_uppercase + digits)
MEANINGFUL = set(ascii_letters + digits)


def hey(phrase):
    phrase = phrase.strip()
    chars = ''.join(ch for ch in phrase if ch in MEANINGFUL)

    if chars and all(ch in YELL for ch in chars) and any(ch in ascii_uppercase for ch in chars):
        return 'Whoa, chill out!'
    elif phrase.endswith("?") and (chars or all(ch in YELL for ch in chars)):
        return 'Sure.'
    elif not chars or not any(ch in MEANINGFUL for ch in chars):
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
