#!/usr/bin/env python
#encoding=utf8


def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError("Invalid input")
    series = [int(ch) for ch in series]
    return [series[i:i+length] for i in range(len(series) - length + 1)]
