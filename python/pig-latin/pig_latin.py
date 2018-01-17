#!/usr/bin/env python
#encoding=utf8

# This problem sucks.
# To those who want to solve this problem without the use of patch work.
# Getting pronounciations from public APIs does not work.


from string import ascii_lowercase


VOWELS = set(list('aeiou'))

SOUNDS = [
    ((), ('sch', 'squ', 'thr', 'spl', 'str')),
    ((), ('ch', 'sh', 'qu', 'tr', 'th', 'rh')),
    (tuple(VOWELS), tuple(set(ascii_lowercase) - VOWELS)),
]

def translate_word(word):
    if word.startswith('x') or word.startswith('y'):
        return word[1:] + word[:1] + 'ay' if word[1] in VOWELS else word + 'ay'

    for tier in SOUNDS:
        vowels, consonants = tier
        if any(word.startswith(s) for s in vowels):
            return word + 'ay'
        elif any(word.startswith(s) for s in consonants):
            return word[len(consonants[0]):] + word[:len(consonants[0])] + 'ay'

def translate(text):
    return ' '.join(translate_word(word) for word in text.split())
