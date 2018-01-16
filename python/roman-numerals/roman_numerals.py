#!/usr/bin/env python
#encoding=utf8

CHARS = {
    1: 'IV',
    10: 'XL',
    100: 'CD',
    1000: 'M',
}


def numeral(number):
    roman = ""
    for i, ch in enumerate(reversed(str(number))):
        if 0 <= int(ch) <= 3:
            roman += int(ch) * CHARS[10**i][0]
        elif ch == '4':
            roman += CHARS[10**i][::-1]
        elif 5 <= int(ch) <=8:
            roman += ((int(ch) - 5) * CHARS[10**i][0] + CHARS[10**i][1])
        else:
            roman += (CHARS[10**(i + 1)][0] + CHARS[10**i][0])
    return ''.join(reversed(roman))


