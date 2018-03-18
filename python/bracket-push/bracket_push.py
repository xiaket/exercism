#!/usr/bin/env python
#encoding=utf8


def is_paired(input_string):
    brackets = '()[]{}'
    parsed = ''.join(ch for ch in input_string if ch in brackets)
    count = 0
    while True:
        for pair in ['()', '[]', '{}']:
            if pair in parsed:
                parsed = parsed.replace(pair, '')
        if parsed == "":
            return True
        count += 1
        if count > 100:
            return False
