#!/usr/bin/env python
#encoding=utf8

import random
from string import ascii_uppercase, digits


NAMES = set([])


class Robot(object):

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            self._name = self.get_name()
        return self._name

    def get_name(self):
        while True:
            part1 = random.choices(ascii_uppercase, k=2)
            part2 = random.choices(digits, k=3)
            name = ''.join(part1 + part2)
            if name not in NAMES:
                NAMES.add(name)
                break
        return name

    def reset(self):
        self._name = None
