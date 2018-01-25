#!/usr/bin/env python
#encoding=utf8


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def primitive_triplets(number):
    if number % 4:
        raise ValueError("number should be divisible by 4")
    factors = [i for i in range(1, number // 2) if (number // 2) % i == 0]
    triplets = []
    for m in factors:
        n = (number // 2 // m)
        if gcd(m, n) != 1:
            continue

        triplet = tuple(sorted([abs(m * m - n * n), number, m * m + n * n]))
        triplets.append(triplet)

    return set(triplets)

def triplets_in_range(range_start, range_end):
    results = []
    b_square = range_end ** 2
    for a in range(range_start, range_end):
        for b in range(a + 1, range_end):
            if a * a + b * b > b_square:
                break
            c = int((a * a + b * b) ** 0.5)
            if is_triplet((a, b, c)):
                results.append((a, b, c))
    return set(results)

def is_triplet(triplet):
    a, b, c = sorted(list(triplet))
    return a * a + b * b == c * c
