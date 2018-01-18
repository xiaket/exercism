#!/usr/bin/env python
#encoding=utf8

SCRABBLE = {
    1: list('AEIOULNRST'),
    2: list('DG'),
    3: list('BCMP'),
    4: list('FHVWY'),
    5: list('K'),
    8: list('JX'),
    10: list('QZ'),
}


def score(word):
    chars = {ch: score for score in SCRABBLE for ch in SCRABBLE[score]}
    return sum(chars[ch.upper()] for ch in word)
