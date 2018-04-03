#!/usr/bin/env python
#encoding=utf8

from threading import Lock

lock = Lock()


class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.opened = False

    def get_balance(self):
        if not self.opened:
            raise ValueError("account closed")
        return self.balance

    def open(self):
        self.opened = True

    def deposit(self, amount):
        if not self.opened:
            raise ValueError("account closed")
        if amount < 0:
            raise ValueError("Invalid amount")
        with lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.opened:
            raise ValueError("account closed")
        if amount > self.balance or amount < 0:
            raise ValueError("Invalid amount")
        with lock:
            self.balance -= amount

    def close(self):
        self.opened = False
