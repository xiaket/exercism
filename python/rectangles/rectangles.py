#!/usr/bin/env python
#encoding=utf8


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __lt__(self, point):
        return (self.x, self.y) < (point.x, point.y)

    def __eq__(self, point):
        return (self.x, self.y) == (point.x, point.y)

    def __repr__(self):
        return "<Point ({}, {})>".format(self.x, self.y)

    def lines(self, edges):
        return [e for e in edges.values() if e.has_point(self)]

    def h_line(self, edges):
        if len(self.lines(edges)) != 2:
            return None
        return [e for e in self.lines(edges) if e.is_horizontal][0]

    def v_line(self, edges):
        if len(self.lines(edges)) != 2:
            return None
        return [e for e in self.lines(edges) if e.is_vertical][0]

    def below(self, edges, points):
        """Return the points on the same edge under this point"""
        if not self.v_line(edges):
            return []

        _below = []
        for point in points.values():
            if self.v_line(edges).has_point(point) and point > self:
                _below.append(point)
        return _below

    def right(self, edges, points):
        """Return the points on the same edge on the right of this point"""
        if not self.h_line(edges):
            return []

        _right = []
        for point in points.values():
            if self.h_line(edges).has_point(point) and point > self:
                _right.append(point)
        return _right

class Line(object):
    def __init__(self, start_point, end_point):
        self.start = start_point
        self.end = end_point

    @property
    def is_horizontal(self):
        return self.start.x == self.end.x

    @property
    def is_vertical(self):
        return self.start.y == self.end.y

    def has_point(self, point):
        return (
            self.is_horizontal and \
            point.x == self.start.x and \
            self.start.y <= point.y <= self.end.y
        ) or (
            self.is_vertical and \
            point.y == self.start.y and \
            self.start.x <= point.x <= self.end.x
        )

    def __repr__(self):
        return "{}Line: {} -> {}".format(
            'H' if self.is_horizontal else 'V',
            self.start, self.end
        )

def parse(lines):
    points, edges = {}, {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != "+":
                continue
            points[(i, j)] = point = Point(i, j)

            # Looking for lines starting with this point
            # horizontal:
            line = lines[i][j+1:]
            if line:
                for k, ch in enumerate(line):
                    if ch not in ['+', '-']:
                        break
                else:
                    k += 1
                if not any(edge.has_point(point)
                    for edge in edges.values()
                    if edge.is_horizontal and edge.start.x == i
                    ):
                    edges[('H', i, j, j+k)] = Line(point, Point(i, j+k))

            # vertical
            line = ''.join(lines[k][j] for k in range(i+1, len(lines)))
            if line:
                for k, ch in enumerate(line):
                    if ch not in ['+', '|']:
                        break
                else:
                    k += 1
                if not any(edge.has_point(point)
                    for edge in edges.values()
                    if edge.is_vertical and edge.start.y == j
                    ):
                    edges[('V', i, j, i+k)] = Line(point, Point(i+k, j))
    return points, edges

def on_same_line(edges, point1, point2):
    return set(point1.lines(edges)) & set(point2.lines(edges))

def count(lines):
    points, edges = parse(lines)
    count = 0
    for point in points.values():
        for below in point.below(edges, points):
            for right in point.right(edges, points):
                x, y = below.x, right.y
                if (x, y) not in points:
                    # Not a point, not a solution
                    continue
                fourth = points[(x, y)]
                if on_same_line(edges, below, fourth) and \
                    on_same_line(edges, right, fourth):
                    count += 1
    return count
