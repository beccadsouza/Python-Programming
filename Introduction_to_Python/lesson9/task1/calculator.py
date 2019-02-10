"""
This module contains Calculator class
"""
import my_module

my_module.hello_world("rebecca")


class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current
