#!/usr/bin/env python
#encoding=utf8

from copy import deepcopy

def select(books, count):
    after = books[count:] + [books[i] - 1 for i in range(count)]
    after.sort(reverse=True)
    return after

def calculate_total(books):
    # The really thing matters is the sorted number of counts.
    if not books:
        return 0
    books = sorted([books.count(i) for i in range(1, 6)], reverse=True)
    sum_ = 8 * 100 * sum(books)
    for i5 in range(books[-1] + 1):
        remains_5 = list(sorted([i - i5 for i in books], reverse=True))
        for i4 in range(sum(remains_5) // 4 + 1):
            remains_4 = deepcopy(remains_5)
            broken4 = False
            for i in range(i4):
                remains_4 = select(remains_4, 4)
                if any(j < 0 for j in remains_4):
                    broken4 = True
                    break
            if broken4:
                continue
            for i3 in range(sum(remains_4) // 3 + 1):
                remains_3 = deepcopy(remains_4)
                broken3 = False
                for i in range(i3):
                    remains_3 = select(remains_3, 3)
                    if any(j < 0 for j in remains_3):
                        broken3 = True
                        break
                if broken3:
                    continue
                for i2 in range(sum(remains_3) // 2 + 1):
                    broken2 = False
                    remains_2 = deepcopy(remains_3)
                    for i in range(i2):
                        remains_2 = select(remains_2, 2)
                        if any(j < 0 for j in remains_2):
                            broken2 = True
                            break
                    if broken2:
                        continue

                    i1 = sum(books) - 5 * i5 - 4 * i4 - 3 * i3 - 2 * i2
                    _sum = i5 * 8 * 5 * 75 + i4 * 8 * 4 * 80 + \
                        i3 * 8 * 3 * 90 + i2 * 8 * 2 * 95 + i1 * 8 * 100
                    if _sum < sum_:
                        sum_ = _sum
    return sum_
