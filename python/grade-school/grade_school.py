#!/usr/bin/env python
#encoding=utf8


class School(object):
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add(self, name, grade):
        if grade not in self.grades:
            self.grades[grade] = (name, )
        else:
            _students = list(self.grades[grade]) + [name]
            self.grades[grade] = tuple(sorted(_students))

    def grade(self, grade):
        return self.grades.get(grade, ())

    def sort(self):
        return [(grade, self.grades[grade]) for grade in sorted(self.grades.keys())]
