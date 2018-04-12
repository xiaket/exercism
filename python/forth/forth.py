#!/usr/bin/env python
#encoding=utf8


class StackUnderflowError(Exception):
    pass


class ForthStack:
    def __init__(self):
        self.stack = []
        self.register = {}

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        if not self.stack:
            raise StackUnderflowError("stack empty")

        item = self.stack[-1]
        if isinstance(item, int):
            self.stack = self.stack[:-1]
            return item

    def add(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(v1 + v2)

    def minus(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(v2 - v1)

    def mul(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(v1 * v2)

    def div(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(v2 // v1)

    def dup(self):
        number = self.pop()
        self.push(number)
        self.push(number)

    def swap(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(v1)
        self.push(v2)

    def over(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(v2)
        self.push(v1)
        self.push(v2)


def parse(stack, data):
    if data.startswith(": ") and data.endswith(" ;"):
        name, definition = data[2:-2].split(" ", 1)
        if name.isdigit():
            raise ValueError("cannot redefine number")
        stack.register[name] = definition
        return

    if stack.register:
        for name in stack.register:
            data = data.replace(name, stack.register[name])

    operations = {
        "+": "add", "-": "minus", "*": "mul", "/": "div",
        "drop": "pop", "dup": "dup", "swap": "swap", "over": "over",
    }

    for trunk in data.split():
        if trunk.isdigit():
            stack.push(int(trunk))
        elif trunk in operations:
            getattr(stack, operations[trunk])()
        else:
            raise ValueError("unknown operation")
    return stack.stack


def evaluate(input_data):
    stack = ForthStack()
    for data in input_data:
        value = parse(stack, data.strip().lower())
    return value
