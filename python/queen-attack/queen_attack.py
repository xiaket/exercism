#!/usr/bin/env python
#encoding=utf8


class Queen(object):
    def __init__(self, row, column):
        if (row < 0 or row >= 8 or column < 0 or column >= 8):
            raise ValueError("Bad start position for queen.")

        self.row = row
        self.column = column
        self.possessed = []
        for i in range(8):
            self.possessed.append((self.row, i))
            self.possessed.append((i, self.column))

        if row >= column:
            # lower-left
            for i in range(0, 8 - row + column):
                self.possessed.append((i, row - column + i))
            for i in range(0, abs(row + column - 8) + 1):
                self.possessed.append((8 - row - column - i, i))
        else:
            # top-right
            for i in range(0, 8 + row - column):
                self.possessed.append((i, column - row + i))
            for i in range(0, column - row):
                self.possessed.append((i + column - row, i))

    def can_attack(self, alt_queen):
        if self.row == alt_queen.row and self.column == alt_queen.column:
            raise ValueError("Badly positioned alternative queen.")
        return (alt_queen.row, alt_queen.column) in set(self.possessed)
