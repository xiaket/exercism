#!/usr/bin/env python
#encoding=utf8
from itertools import chain


def make_diamond(letter):
    diff = ord(letter) - ord('A')
    if not diff:
        return 'A\n'
    first = ' ' * diff + 'A' + ' ' * diff
    lines = [first]
    for i in chain(range(0, diff), range(diff - 2, -1, -1)):
        ch = chr(ord('A') + i + 1)
        space = " " * (diff - i - 1)
        line = space + ch + (2 * i + 1) * " " + ch + space
        lines.append(line)
    lines.append(first)

    return '\n'.join(lines) + '\n'
