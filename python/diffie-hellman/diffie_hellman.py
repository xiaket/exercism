#!/usr/bin/env python
#encoding=utf8
import math

from sympy.ntheory import randprime



def private_key(limit):
    return randprime(2, limit)


def public_key(p, g, private):
    return (g ** private) % p


def secret(p, public, private):
    return (public ** private) % p


def secret(p, a, b, mul=1):
    RANGE = 20

    if b < RANGE:
        return (mul * (a**b)) % p
    rem = {(a ** i) % p: i for i in range(2, RANGE + 1)}
    min_ = min(rem)
    divider = rem[min_]
    div, mod = divmod(b, divider)
    return (mul * secret(p, min_, div, (a ** mod) % p)) % p
