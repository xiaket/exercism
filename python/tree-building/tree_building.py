#!/usr/bin/env python
#encoding=utf8


class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def check_node_id(self):
        if any(child.node_id < self.node_id for child in self.children):
            raise ValueError("Bad node ID")
        for child in self.children:
            child.check_node_id()
        return self

    def __lt__(self, node):
        return self.node_id < node.node_id


def BuildTree(records):
    if not records:
        return None
    if len([r for r in records if r.parent_id == r.record_id]) != 1:
        raise ValueError("bad records")
    if max(r.record_id for r in records) != len(records) - 1:
        raise ValueError("bad records")
    parents = {record.record_id: record.parent_id for record in records}
    records.sort(key=lambda x: x.record_id, reverse=True)
    records.sort(key=lambda x: x.parent_id, reverse=True)
    root_record = records[-1]
    trunks = {root_record.parent_id: Node(root_record.parent_id)}
    for record in records[:-1]:
        if record.parent_id not in trunks:
            trunks[record.parent_id] = Node(record.parent_id)
        trunks[record.parent_id].children.append(Node(record.record_id))
        trunks[record.parent_id].children.sort()
        if record.record_id in trunks:
            # replace the dummy children in its parent's children record
            p_children = trunks[record.parent_id].children
            same_child = lambda c: c.node_id == record.record_id
            other_child = [c for c in p_children if not same_child(c)]
            children = other_child + [trunks[record.record_id]]
            children.sort()
            trunks[record.parent_id].children = children
            del trunks[record.record_id]
    if len(trunks) != 1:
        raise ValueError("Orphan")

    return trunks[root_record.parent_id].check_node_id()
