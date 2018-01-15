#!/usr/bin/env python
#encoding=utf8

NAMES = [
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry',
]

PLANTS = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}


class Garden(object):
    def __init__(self, diagram, students=None):
        self.diagram = [list(line) for line in diagram.splitlines()]
        if students:
            self.students = sorted(students)
        else:
            self.students = NAMES[:(len(self.diagram[0]) / 2)]

    def plants(self, name):
        index = self.students.index(name)
        items = self.diagram[0][index*2:index*2+2] + self.diagram[1][index*2:index*2+2]
        return [PLANTS[ch] for ch in items]
