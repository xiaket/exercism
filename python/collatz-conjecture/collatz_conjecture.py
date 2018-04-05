#!/usr/bin/env python
#encoding=utf8


def collatz_steps(number):
    if number < 1:
        raise ValueError("Invalid input")
    count = 0
    while number != 1:
        count += 1
        number = number * 3 + 1 if number % 2 else number // 2
    return count
