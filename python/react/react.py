#!/usr/bin/env python
#encoding=utf8


class Cell(object):
    def __init__(self, reactor):
        self.reactor = reactor
        self.value = None
        self.callback = None
        self.dependencies = None
        self.watchers = []
        self.known = None

    def set_value(self, value):
        self.reactor.unknown()
        changed = value != self.value
        old_value = self.value
        self.value = value
        if not changed:
            return
        self.notify(old_value)
        for cell in self.reactor.registry:
            if cell.dependencies and self in cell.dependencies:
                old_value = cell.value
                cell.update()
                cell.notify(old_value)

    def update(self):
        values = [d.value for d in self.dependencies]
        self.value = self.callback(values)
        for cell in self.reactor.registry:
            if cell.dependencies and self in cell.dependencies:
                old_value = cell.value
                cell.update()
                cell.notify(old_value)

    def notify(self, old_value):
        if old_value == self.value:
            return
        if self.known:
            return
        for watcher in self.watchers:
            watcher(self, self.value)
        self.known = True

    def add_watcher(self, watcher_callback):
        self.watchers.append(watcher_callback)

    def remove_watcher(self, watcher_callback):
        self.watchers.remove(watcher_callback)


class Reactor(object):
    def __init__(self):
        self.registry = []

    def create_input_cell(self, value):
        cell = Cell(self)
        cell.set_value(value)
        self.registry.append(cell)
        return cell

    def create_compute_cell(self, dependencies, updater_callback):
        cell = Cell(self)
        cell.dependencies = list(dependencies)
        cell.callback = updater_callback
        cell.update()
        self.registry.append(cell)
        return cell

    def unknown(self):
        for cell in self.registry:
            cell.known = False
