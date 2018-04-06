#!/usr/bin/env python
#encoding=utf8

import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real, self.imaginary + other.imaginary,
        )

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary,
        )

    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real, self.imaginary - other.imaginary,
        )

    def __truediv__(self, other):
        base = (other.real ** 2 + other.imaginary ** 2)
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) // base,
            (self.imaginary * other.real - self.real * other.imaginary) // base
        )

    def __eq__(self, other):
        delta = 10 ** -8
        return self.real - other.real < delta and \
            self.imaginary - other.imaginary < delta

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """
        exp(a + i * b) = exp(a) * exp(i * b)
                       = exp(a) * (cos(b) + i * sin(b)).
        """
        return ComplexNumber(
            math.cos(self.imaginary) * (math.e ** self.real),
            math.sin(self.imaginary) * (math.e ** self.real),
        )
