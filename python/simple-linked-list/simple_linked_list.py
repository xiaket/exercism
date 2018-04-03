#!/usr/bin/env python
#encoding=utf8


class Node(object):
    def __init__(self, value):
        self.value_ = value
        self.next_ = None

    def value(self):
        return self.value_

    def next(self):
        return self.next_

class LinkedList(object):
    def __init__(self, values=[]):
        self.values = []
        previous = None
        for v in values:
            node = Node(v)
            self.values = [node] + self.values
            if previous is None:
                previous = node
            else:
                node.next_ = previous
                previous = node

    def __len__(self):
        return len(self.values)

    def head(self):
        if not self.values:
            raise EmptyListException("Empty list")
        return self.values[0]

    def push(self, value):
        node = Node(value)
        if self.values:
            node.next_ = self.values[0]
        self.values = [node] + self.values

    def pop(self):
        if not self.values:
            raise EmptyListException("Empty list")
        node = self.values[0]
        self.values = self.values[1:]
        return node.value()

    def reversed(self):
        for i in reversed(self.values):
            yield i.value()

    def __iter__(self):
        for i in self.values:
            yield i.value()

class EmptyListException(Exception):
    pass
