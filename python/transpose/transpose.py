#!/usr/bin/env python
#encoding=utf8


def transpose(input_lines):
    if not input_lines:
        return ""
    lines = input_lines.splitlines()
    max_ = max(len(line) for line in lines)
    transposed = []
    for i in range(max_):
        segment = ""
        terminated = False
        for line in reversed(lines):
            if len(line) > i:
                terminated = True
                segment += line[i]
            elif terminated:
                segment += " "
        transposed.append("".join(list(reversed(segment))))
    return '\n'.join(transposed)
