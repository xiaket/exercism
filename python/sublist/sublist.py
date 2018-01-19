#!/usr/bin/env python
#encoding=utf8

SUBLIST = "A<B"
SUPERLIST = "A>B"
EQUAL = "A=B"
UNEQUAL = "A!=B"


def is_sublist(a, b):
    """check if a is a sublist of b."""
    if len(b) < len(a):
        return False
    if len(a) == len(b):
        return a == b

    for i in range(len(b) - len(a) + 1):
        if a == b[i:i+len(a)]:
            return True
    else:
        return False


def check_lists(first_list, second_list):
    if is_sublist(first_list, second_list):
        return EQUAL if is_sublist(second_list, first_list) else SUBLIST
    else:
        return SUPERLIST if is_sublist(second_list, first_list) else UNEQUAL
