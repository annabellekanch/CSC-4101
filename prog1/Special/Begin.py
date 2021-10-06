# Begin -- Parse tree node strategy for printing the special form begin

import sys
from Special import Special

class Begin(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for r in range (0, n):
            sys.stdout.write(' ')
        sys.stdout.write("(begin")
        if(t.getCdr().isPair()):
            t.getCdr().print(n + 2, p)
        else:
            raise Exception("Syntax Error")
        for i in range (0, n):
            sys.stdout.write(" ")
        sys.stdout.write(")")
        pass
