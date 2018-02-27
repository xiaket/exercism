#!/usr/bin/env python
#encoding=utf8


def saddle_points(matrix):
    if any(len(matrix[0]) != len(row) for row in matrix):
        raise ValueError("Bad matrix")
    points = []
    for i, row in enumerate(matrix):
        max_ = max(row)
        for j, item in enumerate(row):
            if not item == max_:
                continue
            if i == 0:
                if item <= matrix[i + 1][j]:
                    points.append((i, j))
            elif i == len(matrix) - 1:
                if item <= matrix[i - 1][j]:
                    points.append((i, j))
            elif matrix[i + 1][j] >= item and item <= matrix[i - 1][j]:
                points.append((i, j))
    return set(points)
