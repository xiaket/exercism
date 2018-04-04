#!/usr/bin/env python
#encoding=utf8


def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("invalid base")
    if any(d >= input_base or d < 0 for d in digits):
        raise ValueError("invalid digit")
    value = 0
    for i, digit in enumerate(digits):
        value += digit * input_base ** (len(digits) - i - 1)
    if not value:
        return []
    rebased = []
    while True:
        div, mod = divmod(value, output_base)
        rebased.append(mod)
        if div == 0:
            break
        value = div
    return list(reversed(rebased))
