# Define -- Parse tree node strategy for printing the special form define

import sys
from Special import Special

class Define(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for r in range(0, n):
            sys.stdout.write(" ")
        sys.stdout.write("(define")
        if(t.getCdr().getCar().isSymbol()):
            t.getCdr().getCar().print(0, False)
        else:
            raise Exception("Syntax Error")
        sys.stdout.write(" ")
        if(t.getCdr().getCdr().getCar().isNull != t.getCdr().getCdr().getCar()):
            t.getCdr().getCdr().getCar().print(0, True)
        else:
            raise Exception("Syntax Error")
        sys.stdout.write(")")
        pass
