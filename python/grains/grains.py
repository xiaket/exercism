#!/usr/bin/env python
#encoding=utf8


def on_square(integer_number):
    if not 0 < integer_number <= 64:
        raise ValueError("Invalid input.")

    return 2 ** (integer_number - 1)


def total_after(integer_number):
    if not 0 < integer_number <= 64:
        raise ValueError("Invalid input.")

    return 2 ** integer_number - 1
