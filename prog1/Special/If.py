# If -- Parse tree node strategy for printing the special form if

import sys
from Special import Special

class If(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for r in range(0, n):
            sys.stdout.write(' ')
        sys.stdou.write("(if ")
        if(t.getCdr().getCar().isPair()):
            t.getCdr().getCar().print(0, p)
        else:
            raise Exception("Syntax Error")
        sys.stdout.write()
        if(t.getCdr().getCdr().getCar().isNull != t.getCdr().getCdr().getCar()):
            t.getCdr().getCdr().gerCar().print(n + 2, p)
        else:
            raise Exception("Syntax Error")
        sys.stdout.write()
        if(t.getCdr().getCdr().getCdr().getCar().isNull() != t.getCdr().getCdr().getCdr().getCar()):
            t.getCdr().getCdr().getCdr().getCar().print(n + 2, p)
        else:
            raise Exception("Syntax Error")
        for i in range(0, n):
            sys.stdout.write(' ')
        sys.stdout.write(")" )
        pass
    def printQuote(self, c, n ,p):
        pass
