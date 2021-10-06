# Cond -- Parse tree node strategy for printing the special form cond

import sys
from Special import Special

class Cond(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for r in range(0, n):
            sys.stdout.write(" ")
        sys.stdout.write("(cond")
        if(t.getCdr().isPair()):
            t.getCDR().print(n + 2, True)
        else:
            raise Exception("Syntax Error")
        pass
