# Lambda -- Parse tree node strategy for printing the special form lambda

import sys
from Special import Special

class Lambda(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for r in range(0, n):
            sys.stdout.write(" ")
        sys.stdout.write("(lambda ")
        if(t.getCdr().getCar().isPair()):
            t.getCdr().getCar().print(0, False)
        else:
            raise Exception("Syntax Error")
        sys.stdout.write()
        if(t.getCdr().getCdr().getCar().isPair()):
            t.getCdr().getCdr().getCar().print(n + 2, False)
        else:
            raise Exception("Syntax Error")
        sys.stdout.write()
        for i in range(0, n):
            sys.stdout.write(" ")
        sys.stdout.write(") ")
        pass
    def printQuote(self, c, n ,p):
        pass
