#!/usr/bin/env python
#encoding=utf8


class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        if self.properties != other.properties:
            return False
        if len(self.children) != len(other.children):
            return False
        return all(a == b for a, b in zip(self.children, other.children))


def parse_prop(prop):
    if not prop:
        return {}
    name = prop[:prop.index("[")]
    if not name.isupper():
        raise ValueError("Invalid property name")
    value = prop[len(name):].replace("\n", " ").replace("\t", " ")
    value = value.replace('\]', ';')
    values = value.split("][")
    values[0] = values[0].lstrip('[')
    values[-1] = values[-1].rstrip(']')
    values = [v.replace(';', ']') for v in values]
    return {name: values}


def parse_node(desc):
    if not desc:
        return SgfTree(None, None)

    desc = desc.lstrip(';')
    if ';' not in desc:
        return SgfTree(parse_prop(desc), None)

    start, end = desc.split(";", 1)
    if '(' not in start:
        desc = end
    else:
        start = start[:start.index('(')]
        desc = desc[desc.index('('):]
    prop = parse_prop(start)
    if not desc:
        return SgfTree(prop, None)

    children = desc.split(")(")
    children[0] = children[0].lstrip('(')
    children[-1] = children[-1].rstrip(')')
    return SgfTree(prop, [parse_node(c) for c in children])


def parse(input_):
    if not input_ or input_[0] != "(" or input_[-1] != ")":
        raise ValueError("Invalid")
    input_ = input_[1:-1]
    if not input_ or input_[0] != ";":
        raise ValueError("Invalid")
    return parse_node(input_[1:])
