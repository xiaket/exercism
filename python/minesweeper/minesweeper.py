#!/usr/bin/env python
#encoding=utf8



def validate(array):
    row_len = [len(row) for row in array]
    if not all (row_len[0] == l for l in row_len[1:]):
        raise ValueError("Bad board.")
    if any(ch not in [' ', "*"] for row in array for ch in row):
        raise ValueError("Bad character in board.")

def board(input_board_array):
    array = []
    for row in input_board_array:
        array.append(list(row))
    validate(array)
    rows = len(array)
    columns = len(array[0]) if rows else 0
    for i in range(rows):
        for j in range(columns):
            if array[i][j] == "*":
                continue
            candidates = []
            if i != 0 and j != 0:
                candidates.append(array[i - 1][j - 1])
            if i != 0:
                candidates.append(array[i - 1][j])
            if i != 0 and j != columns - 1:
                candidates.append(array[i - 1][j + 1])
            if j != 0:
                candidates.append(array[i][j - 1])
            if j != columns - 1:
                candidates.append(array[i][j + 1])
            if i != rows - 1 and j != 0:
                candidates.append(array[i + 1][j - 1])
            if i != rows - 1:
                candidates.append(array[i + 1][j])
            if i != rows - 1 and j != columns - 1:
                candidates.append(array[i + 1][j + 1])
            if candidates.count("*"):
                array[i][j] = str(candidates.count("*"))

    return [''.join(row) for row in array]
