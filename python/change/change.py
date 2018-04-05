#!/usr/bin/env python
#encoding=utf8


def find_minimum_coins(total_change, coins):
    if total_change < min(coins) and total_change != 0:
        raise ValueError("Invalid change")
    if total_change == 0:
        return []
    cache = {c: [c] for c in coins}
    while True:
        new_v = {}
        for v in cache:
            for c in coins:
                if v + c in cache:
                    continue
                new_v[v + c] = cache[v] + [c]
        if not any(v < total_change for v in new_v):
            raise ValueError("Invalid change")
        cache.update(new_v)
        if total_change in cache:
            return list(sorted(cache[total_change]))



