#!/usr/bin/env python
#encoding=utf8


def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Invalid input")
    return sum(int(strand_a[i] != strand_b[i]) for i in range(len(strand_a)))
