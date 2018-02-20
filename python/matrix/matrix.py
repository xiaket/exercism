#!/usr/bin/env python
#encoding=utf8


class Matrix(object):
    def __init__(self, matrix_string):
        self.store = []
        for line in matrix_string.splitlines():
            self.store.append([int(i) for i in line.split()])

    def row(self, index):
        return self.store[index]

    def column(self, index):
        return [row[index] for row in self.store]
