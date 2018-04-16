#!/usr/bin/env python
#encoding=utf8

from json import dumps


def get_node(tree, name):
    if tree.label == name:
        return True, [tree.label]
    if not tree.children:
        return False, None
    for child in tree.children:
        found, addr = get_node(child, name)
        if found:
            return True, [tree.label] + addr
    return False, None


def goto_node(tree, desc):
    assert tree.label == desc[0]
    node = tree
    for name in desc[1:]:
        nodes = [n for n in node.children if n.label == name]
        if not nodes:
            return False, None
        node = nodes[0]
    return True, node


def recreate_node(orig, desc):
    """Recreate item in orig under desc."""
    tree = Tree(desc[-1], [])
    success, node = goto_node(orig, desc)
    if not node.children:
        return tree

    for child in node.children:
        success, _ = goto_node(orig, desc + [child.label])
        if not success:
            child_node = Tree(child.label, [])
        else:
            child_node = recreate_node(orig, desc + [child.label])
        tree.children.append(child_node)
    return tree


class Tree(object):
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        found, desc = get_node(self, from_node)
        if not found:
            raise ValueError("Node {} not found.".format(from_node))

        last_label = desc[-1]
        node = recreate_node(self, desc)
        last_node = node
        reverse_desc = [last_label]
        for name in reversed(desc[:-1]):
            desc_ = get_node(self, name)[1]
            parent = recreate_node(self, desc_)

            last_node.children.append(parent)
            parent.children = [
                child for child in parent.children
                if child.label != last_label
            ]
            last_label = desc_[-1]
            last_node = parent
        return node

    def path_to(self, from_node, to_node):
        tree = self.from_pov(from_node)
        found, desc = get_node(tree, to_node)
        if not found:
            raise ValueError("Dest node {} not found.".format(to_node))
        return desc
