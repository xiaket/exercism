#!/usr/bin/env python
#encoding=utf8

MAP = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
}

def proteins(strand):
    if isinstance(strand, list):
        codons = strand
    else:
        codons = [strand[i*3:i*3 + 3] for i in range(len(strand) // 3)]
    proteins_ = []
    for codon in codons:
        if MAP[codon] == 'STOP':
            break
        proteins_.append(MAP[codon])
    return proteins_
