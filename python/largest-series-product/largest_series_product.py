#!/usr/bin/env python
#encoding=utf8

from operator import mul


def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError("Invalid size")
    series = [int(ch) for ch in series]
    prod = 0
    for i in range(len(series) - size + 1):
        _prod = reduce(mul, [series[j] for j in range(i, i+size)], 1)
        if _prod > prod:
            prod = _prod
    return prod
