#!/usr/bin/env python
#encoding=utf8

import operator


def append(xs, ys):
    return xs + ys


def concat(lists):
    return [i for l in lists for i in l]


def filter_clone(function, xs):
    return [i for i in xs if function(i)]


def length(xs):
    return sum([1 for i in xs])


def map_clone(function, xs):
    return [function(i) for i in xs]


def foldl(function, xs, acc):
    for i in xs:
        acc = function(acc, i)
    return acc


def foldr(function, xs, acc):
    for i in reverse(xs):
        acc = function(i, acc)
    return acc


def reverse(xs):
    length = len(xs)
    return [xs[length - i - 1] for i in range(length)]

