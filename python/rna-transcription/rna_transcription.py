#!/usr/bin/env python
#encoding=utf8


TRANSCRIPT = {
    'G': 'C',
    'C': 'G',
    'A': 'U',
    'T': 'A',
}


def to_rna(dna_strand):
    if any (ch.upper() not in TRANSCRIPT for ch in dna_strand):
        raise ValueError("Invalid input")
    return ''.join(TRANSCRIPT[ch.upper()] for ch in dna_strand)
