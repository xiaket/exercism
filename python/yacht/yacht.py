#!/usr/bin/env python
#encoding=utf8

def four_of_a_kind(dice):
    counts = {d: dice.count(d) for d in dice}
    if not max(counts.values()) >= 4:
        return 0
    return [d for d in counts if counts[d] == max(counts.values())][0] * 4

ONES = lambda dice: sum(d for d in dice if d == 1)
TWOS = lambda dice: sum(d for d in dice if d == 2)
THREES = lambda dice: sum(d for d in dice if d == 3)
FOURS = lambda dice: sum(d for d in dice if d == 4)
FIVES = lambda dice: sum(d for d in dice if d == 5)
SIXES = lambda dice: sum(d for d in dice if d == 6)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and dice.count(list(set(dice))[0]) in [2, 3] else 0
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = lambda dice: 30 if set(dice) == set(range(1, 6)) else 0
BIG_STRAIGHT = lambda dice: 30 if set(dice) == set(range(2, 7)) else 0
CHOICE = lambda dice: sum(dice)
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0


"""
    Full House      Total of the dice       3 3 3 5 5 scores 19
    Four of a Kind  Total of the four dice  4 4 4 4 6 scores 16
"""


def score(dice, category):
    return category(dice)

#score([6, 6, 4, 6, 6], FOUR_OF_A_KIND)
