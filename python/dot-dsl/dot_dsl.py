#!/usr/bin/env python
#encoding=utf8


NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        self.parse_data(data)

    def parse_data(self, data):
        if not isinstance(data, list):
            raise TypeError("Bad graph")

        arguments = {NODE: 3, EDGE: 4, ATTR: 3}
        for line in data:
            if not isinstance(line, tuple) or len(line) in [0, 1]:
                raise TypeError("Bad data")
            klass = line[0]
            if arguments.get(klass, -1) != len(line):
                raise ValueError("Bad data")
            if klass == NODE:
                self.nodes.append(Node(line[1], line[2]))
            elif klass == EDGE:
                self.edges.append(Edge(line[1], line[2], line[3]))
            elif klass == ATTR:
                self.attrs[line[1]] = line[2]
