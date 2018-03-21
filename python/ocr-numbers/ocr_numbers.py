#!/usr/bin/env python
#encoding=utf8

LOOKUP = {
    " _ \n| |\n|_|\n   ": "0",
    "   \n  |\n  |\n   ": "1",
    " _ \n _|\n|_ \n   ": "2",
    " _ \n _|\n _|\n   ": "3",
    "   \n|_|\n  |\n   ": "4",
    " _ \n|_ \n _|\n   ": "5",
    " _ \n|_ \n|_|\n   ": "6",
    " _ \n  |\n  |\n   ": "7",
    " _ \n|_|\n|_|\n   ": "8",
    " _ \n|_|\n _|\n   ": "9",
}


def convert(grid):
    if len(grid) % 4:
        raise ValueError("Bad grid")
    if not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Irrgular grid")
    if len(grid[0]) % 3:
        raise ValueError("Bad grid")
    numbers = []
    for i in range(len(grid) // 4):
        line_numbers = ""
        for j in range(len(grid[0]) // 3):
            items = [grid[i*4+k][j*3:j*3+3] for k in range(4)]
            line_numbers += LOOKUP.get("\n".join(items), "?")
        numbers.append(line_numbers)
    return ",".join(numbers)
