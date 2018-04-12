#!/usr/bin/env python
#encoding=utf8


ANIMALS = {
    8: {
        'animal': 'horse', 'next': 'cow',
        'exclaim': "She's dead, of course!",
    },
    7: {
        'animal': 'cow', 'next': 'goat',
        'exclaim': "I don't know how she swallowed a cow!",
    },
    6: {
        'animal': 'goat', 'next': 'dog',
        'exclaim': "Just opened her throat and swallowed a goat!",
    },
    5: {
        'animal': 'dog', 'next': 'cat',
        'exclaim': "What a hog, to swallow a dog!",
    },
    4: {
        'animal': 'cat', 'next': 'bird',
        'exclaim': "Imagine that, to swallow a cat!",
    },
    3: {
        'animal': 'bird', 'next': 'spider',
        'exclaim': "How absurd to swallow a bird!",
    },
    2: {
        'animal': 'spider',
        'exclaim': "It wriggled and jiggled and tickled inside her.",
    },
    1: {
        'animal': 'fly',
        'exclaim': "I don't know why she swallowed the fly. Perhaps she'll die.",
    },
}

START = "I know an old lady who swallowed a {animal}.{exclaim}"
SPIDER = "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."
END = "She swallowed the spider to catch the fly.I don't know why she swallowed the fly. Perhaps she'll die."
CHASE = "She swallowed the {animal} to catch the {next}."


def verse(order):
    if order in [1, 8]:
        templates = [START]
    elif order == 2:
        templates = [START, END]
    elif 3 <= order < 8:
        middle = "".join(CHASE.format(**ANIMALS[i]) for i in range(order, 3, -1))
        templates = [START, middle, SPIDER, END]
    return "".join([t.format(**ANIMALS[order]) for t in templates])


def recite(start, end):
    return [verse(i) for i in range(start, end + 1)]
