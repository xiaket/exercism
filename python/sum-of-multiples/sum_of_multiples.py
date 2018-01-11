#!/usr/bin/env python
#encoding=utf8


def sum_of_multiples(limit, multiples):
    multiple_numbers = {}
    numbers = set()
    for num in multiples:
        numbers = set(i for i in range(limit) if i % num == 0) | numbers

    return sum(numbers)
