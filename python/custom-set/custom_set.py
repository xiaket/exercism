#!/usr/bin/env python
#encoding=utf8


class CustomSet(object):
    def __init__(self, elements=[]):
        self.elements = []
        for ele in elements:
            self.add(ele)
        self.elements.sort()

    def __iter__(self):
        return iter(self.elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return all(ele in other.elements for ele in self)

    def isdisjoint(self, other):
        return len(self.intersection(other)) == 0

    def __eq__(self, other):
        return self.elements == other.elements

    def __len__(self):
        return len(self.elements)

    def add(self, ele):
        if ele not in self:
            self.elements.append(ele)
            self.elements.sort()

    def intersection(self, other):
        return CustomSet([ele for ele in self if ele in other])

    def difference(self, other):
        return CustomSet([ele for ele in self if ele not in other])

    def union(self, other):
        return CustomSet(self.elements + other.elements)

    def __add__(self, other):
        return self.union(other)

    def __sub__(self, other):
        return self.difference(other)
