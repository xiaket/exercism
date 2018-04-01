#!/usr/bin/env python
#encoding=utf8


def binary_search(numbers, number, start=0, end=None):
    if not numbers:
        raise ValueError("No data")

    if end == None:
        end = len(numbers) - 1

    if end == 0:
        if numbers[start] == number:
            return start
        raise ValueError("number not in list")
    elif end - start in [2, 3]:
        mapping = {numbers[i]: i for i in range(start, end + 1)}
        if number in mapping:
            return mapping[number]
        raise ValueError("number not in list")

    index = (end - start) // 2 + start
    if numbers[index] >= number:
        return binary_search(numbers, number, start, index)
    else:
        return binary_search(numbers, number, index, end)
