#!/usr/bin/env python
#encoding=utf8


class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        msg = 'TreeNode(data={}, left={}, right={})'
        return msg.format(self.data, self.left, self.right)

    def add(self, number):
        if number <= self.data:
            if not self.left:
                self.left = TreeNode(number, None, None)
            else:
                self.left.add(number)
        else:
            if not self.right:
                self.right = TreeNode(number, None, None)
            else:
                self.right.add(number)

    def flat(self):
        data = []
        if self.left is not None:
            data = [self.left.flat(), self.data]
        else:
            data = [self.data]
        if self.right is not None:
            data += [self.right.flat()]
        return " ".join(data)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.tree_data = tree_data
        self.root = TreeNode(tree_data[0], None, None)
        for num in self.tree_data[1:]:
            self.root.add(num)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.root.flat().split()
