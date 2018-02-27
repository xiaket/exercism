#!/usr/bin/env python
#encoding=utf8
from copy import deepcopy


def encode(message, rails):
    message = "".join(ch for ch in message if ch.isalnum())
    fence = []
    for i in range(rails):
        fence.append(deepcopy([""] * len(message)))
    for i, ch in enumerate(message):
        order = i % (2 * (rails - 1))
        row = order if order < rails else 2 * (rails -1) - order
        fence[row][i] = ch

    return ''.join(''.join(ch) for row in fence for ch in row if ch)

def decode(message, rails):
    fence = {}
    length = len(message)
    period = 2 * (rails - 1)
    remains = message[-(length % period):] if length % period else None
    last = 0

    for i in range(rails):
        if i == 0 or (i == rails - 1):
            count = length // period
            if remains and len(remains) > i:
                count += 1
        else:
            count = (length // period) * 2
            if remains and len(remains) > i:
                count += 1
                if len(remains) > period - i:
                    count += 1
        fence[i] = message[last:last+count]
        last += count

    cycle_ = list(range(rails)) + list(reversed(range(rails)))[1:-1]
    cycles = cycle_ * (length // period + 1)
    decoded = ""
    for i in range(length):
        index = cycles[i]
        decoded += fence[index][0]
        fence[index] = fence[index][1:]

    return decoded
