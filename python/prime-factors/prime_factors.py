#!/usr/bin/env python
#encoding=utf8

from copy import deepcopy
from itertools import chain


def sieve(limit):
    numbers = range(2, limit +1)
    div = 2
    while div <= int(limit ** 0.5) + 1:
        if div in numbers:
            numbers = [i for i in numbers if not (i % div == 0 and i != div)]
        div += 1
    return numbers

COMMON = sieve(100)

def is_prime(number):
    for i in range(101, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False, i
    return True, None

def prime_factors(natural_number):
    if natural_number < 2:
        return []
    factors = []
    for prime in COMMON:
        if natural_number % prime != 0:
            continue
        while natural_number % prime == 0:
            factors.append(prime)
            natural_number = int(natural_number / prime)
        if natural_number in COMMON:
            factors.append(natural_number)
            return sorted(factors)
        elif natural_number == 1:
            return sorted(factors)

    status = False
    while not status:
        status, factor = is_prime(natural_number)
        if not status:
            natural_number = int(natural_number / factor)
            factors.append(factor)
    return sorted(factors + [natural_number])
