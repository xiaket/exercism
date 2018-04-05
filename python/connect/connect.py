#!/usr/bin/env python
#encoding=utf8

class Point:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    @property
    def neighbours(self):
        return [
            (self.i - 1, self.j), (self.i - 1, self.j + 1),
            (self.i, self.j - 1), (self.i, self.j + 1),
            (self.i + 1, self.j), (self.i + 1, self.j - 1),
        ]

    def is_neighbour(self, other):
        return (other.i, other.j) in self.neighbours

    def __repr__(self):
        return "<Point ({}, {})".format(self.i, self.j)


class ConnectGame:
    def __init__(self, board):
        self.rows = len(board.splitlines())
        self.xpoints = []
        self.opoints = []
        for i, line in enumerate(board.splitlines()):
            for j, ch in enumerate(line.split()):
                if ch == 'X':
                    self.xpoints.append(Point(i, j))
                elif ch == 'O':
                    self.opoints.append(Point(i, j))
        self.rows, self.columns = i + 1, j + 1

    def get_winner(self):
        # X: left to right
        starts = [p for p in self.xpoints if p.j == 0]
        for start in starts:
            cache = [start]
            new = [start]
            while True:
                points = [
                    p for p in self.xpoints for n in new
                    if p.is_neighbour(n) and p not in cache
                ]
                cache += points
                if any(p.j == self.columns -1 for p in cache):
                    return 'X'
                new = points
                if not points:
                    break

        # O: top to bottom
        starts = [p for p in self.opoints if p.i == 0]
        for start in starts:
            cache = [start]
            new = [start]
            while True:
                points = [
                    p for p in self.opoints for n in new
                    if p.is_neighbour(n) and p not in cache
                ]

                cache += points
                if any(p.i == self.rows -1 for p in cache):
                    return 'O'
                new = points
                if not points:
                    break

        return ""
