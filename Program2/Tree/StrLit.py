# StLit -- Parse tree node class for representing string literals

import sys
from Tree import Node
from Print import Printer

class StrLit(Node):
    def __init__(self, s, b):
        self.strVal = s
        self.printQuotes = b

    def print(self, n, p=False):
        if not self.printQuotes:
            print(self.strVal)
            return
        Printer.printStrLit(n, self.strVal)

    def isString(self):
        return True

if __name__ == "__main__":
    id = StrLit("foo")
    id.print(0)
