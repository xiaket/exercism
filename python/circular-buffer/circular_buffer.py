#!/usr/bin/env python
#encoding=utf8


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def write(self, item):
        if len(self.storage) == self.capacity:
            raise BufferFullException("No space")
        self.storage.append(item)

    def read(self):
        if len(self.storage) == 0:
            raise BufferEmptyException("No item")
        result = self.storage[0]
        self.storage = self.storage[1:]
        return result

    def clear(self):
        self.storage = []

    def overwrite(self, item):
        if len(self.storage) != self.capacity:
            return self.write(item)

        self.storage = self.storage[1:] + [item]
