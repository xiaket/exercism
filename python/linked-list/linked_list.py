#!/usr/bin/env python
#encoding=utf8


class Node(object):
    def __init__(self, value, _next=None, previous=None):
        self.value = value
        self.next = _next
        self.previous = previous


class LinkedList(object):
    def __init__(self):
        self.values = []

    def __len__(self):
        return len(self.values)

    def head(self):
        if not self.values:
            raise EmptyListException("Empty list")
        return self.values[0]

    def push(self, value):
        node = Node(value)
        if self.values:
            node.next = self.values[0]
            self.values[0].previous = node
        self.values = [node] + self.values

    def pop(self):
        node = self.values[0]
        if node.previous:
            node.previous.next = None
        self.values = self.values[1:]
        return node.value

    def shift(self):
        node = self.values[-1]
        if node.next:
            node.next.previous = None
        self.values = self.values[:-1]
        return node.value

    def unshift(self, value):
        node = Node(value)
        if self.values:
            node.previous = self.values[-1]
            self.values[-1].next = node
        self.values = self.values + [node]

    def __iter__(self):
        for i in reversed(self.values):
            yield i.value
