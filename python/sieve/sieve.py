#!/usr/bin/env python
#encoding=utf8


def sieve(limit):
    numbers = range(2, limit +1)
    div = 2
    while div <= int(limit ** 0.5) + 1:
        if div in numbers:
            numbers = [i for i in numbers if not (i % div == 0 and i != div)]
        div += 1
    return numbers
