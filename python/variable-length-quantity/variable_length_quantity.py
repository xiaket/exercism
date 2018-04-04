#!/usr/bin/env python
#encoding=utf8


def encode(numbers):
    encoded = []
    for number in numbers:
        start = len(encoded)
        div, mod = divmod(number, 128)
        encoded.append(mod)
        if not div:
            continue
        plus = True
        while True:
            div, mod = divmod(div, 128)
            encoded.insert(start, mod + 128)
            if not div:
                break
    return encoded


def decode(bytes_):
    decoded = []
    number = 0
    need_more = False
    for byte in bytes_:
        need_more = byte >= 128
        if need_more:
            number = number * 128 + byte - 128
        else:
            number = number * 128 + byte
            decoded.append(number)
            number = 0
            continue
    if need_more:
        raise ValueError("Bad input bytes")
    return decoded
