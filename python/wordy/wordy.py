#!/usr/bin/env python
#encoding=utf8
import tokenize
import io

OPERATORS = {
    "plus": "+",
    "minus": "-",
    "multiplied by": "*",
    "divided by": "/",
}


def calculate(question):
    try:
        assert question.startswith("What is ")
        assert question.endswith("?")
    except AssertionError:
        raise ValueError("Invalid input")
    question = question[len('What is '):-1]
    items = []
    while question:
        for op in OPERATORS:
            if question.startswith(op):
                question = question[len(op):].strip()
                items.append(OPERATORS[op])
                break
        else:
            if " " in question:
                # This should be an int then
                item, question = question.split(" ", 1)
                items.append(int(item))
            else:
                # Last item
                items.append(int(question))
                question = None
            continue

    result = items[0]
    items = items[1:]
    while items:
        op, operand = items[:2]
        if not (isinstance(op, str) and isinstance(operand, int)):
            raise ValueError("Invalid input")
        items = items[2:]
        if op == "+":
            result += operand
        elif op == "-":
            result -= operand
        elif op == "*":
            result *= operand
        elif op == "/":
            result //= operand
    return result
