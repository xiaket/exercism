#!/usr/bin/env python
#encoding=utf8
from __future__ import division

from fractions import gcd


class Rational(object):
    def __init__(self, numer, denom):
        _gcd = abs(gcd(numer, denom))
        if denom < 0:
            numer, denom = -numer, -denom

        self.numer = numer / _gcd
        self.denom = denom / _gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(
            self.numer * other.denom + self.denom * other.numer,
            self.denom * other.denom,
        )

    def __sub__(self, other):
        neg = Rational(-other.numer, other.denom)
        return self.__add__(neg)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ZeroDivisionError
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __pow__(self, power):
        if not isinstance(power, int):
            return (self.numer ** power) / (self.denom ** power)
        if power == 0:
            return Rational(1, 1)
        elif power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            power = abs(power)
            return Rational(self.denom ** power, self.numer ** power)

    def __rpow__(self, base):
        return pow(base ** self.numer, 1/self.denom)
