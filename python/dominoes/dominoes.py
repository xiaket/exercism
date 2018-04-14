#!/usr/bin/env python
#encoding=utf8

from copy import deepcopy
from collections import Counter


def extend(desirable, chain, remains):
    choices = [domino for domino in remains if desirable in domino]
    if len(choices) == 0:
        return []

    solutions = []
    for choice in choices:
        remains_ = deepcopy(remains)
        chain_ = deepcopy(chain)
        remains_.remove(choice)
        choice = choice if choice[0] == desirable else (choice[1], choice[0])
        chain_.append(choice)
        if len(remains_) == 0:
            # only item in remains, no need to finish the loop, just return
            return [[choice]]

        subsolutions = extend(choice[1], chain_, remains_)
        for sol in subsolutions:
            if len(sol) == len(remains_):
                solutions.append([choice] + sol)
    return solutions


def chain(dominoes):
    all_numbers = [i for t in dominoes for i in t]
    counter = Counter(all_numbers)
    if any(value % 2 for value in counter.values()):
        return None

    if not counter.most_common():
        return []
    start_number = counter.most_common()[0][0]
    solutions = extend(start_number, [], dominoes)
    validated = []
    for sol in solutions:
        if sol[0][0] != sol[-1][-1] or sol in validated:
            continue
        validated.append(sol)
    return validated[0] if len(validated) else None
