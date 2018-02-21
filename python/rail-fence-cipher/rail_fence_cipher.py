#!/usr/bin/env python
#encoding=utf8
from copy import deepcopy
from string import ascii_lowercase


def encode(message, rails):
    message = "".join(ch for ch in message if ch.isalnum())
    period = 2 * (rails - 1)
    periods = len(message) // period
    if len(message) % period:
        remains = message[-(len(message) % period):]
    else:
        remains = None
    encoded = ""
    for i in range(rails):
        if i == 0 or (i == rails - 1):
            # a single ch in a period should be added to the encoded message
            encoded += ''.join(message[period * j + i] for j in range(periods))
            if remains and len(remains) > i:
                encoded += remains[i]
        else:
            encoded += ''.join([
                message[period * j + i] + message[period * (j + 1) - i]
                for j in range(periods)
            ])
            if remains and len(remains) > i:
                encoded += remains[i]
                if len(remains) > period - i:
                    encoded += remains[period - i]
    return encoded

def encode_visual(message, rails):
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
    pass


"""
x 0 x 0 x 0 x 0 x 0 x 0 x 0 x 0 x 0
0 y 0 y 0 y 0 y 0 y 0 y 0 y 0 y 0 y
"""
