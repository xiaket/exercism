#!/usr/bin/env python
#encoding=utf8


HEADER = "{start} bottles of beer on the wall, {start} bottles of beer."
TAIL = "Take one down and pass it around, {remains} bottles of beer on the wall."
TWOTAIL = "Take one down and pass it around, 1 bottle of beer on the wall."

ONEHEADER = "1 bottle of beer on the wall, 1 bottle of beer."
ONETAIL = "Take it down and pass it around, no more bottles of beer on the wall."
NOHEADER = "No more bottles of beer on the wall, no more bottles of beer."
NOTAIL = "Go to the store and buy some more, 99 bottles of beer on the wall."


def recite(start, take=1):
    verses = []
    while take > 0:
        if start > 1:
            header = HEADER
        elif start == 1:
            header = ONEHEADER
        else:
            header = NOHEADER

        if start > 2:
            tail = TAIL
        elif start == 2:
            tail = TWOTAIL
        elif start == 1:
            tail = ONETAIL
        else:
            tail = NOTAIL

        if verses:
            verses.append("")
        verses.append(header.format(start=start))
        verses.append(tail.format(remains=start -1))
        start -= 1
        take -= 1
    return verses
