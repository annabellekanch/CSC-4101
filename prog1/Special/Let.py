# Let -- Parse tree node strategy for printing the special form let

import sys
from Special import Special

class Let(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for i in range(0,n):
            sys.stdout.write(" ")

        sys.stdout.write("(let ")

        if t.getCdr().getCar().isPair():
            t.getCdr().getCar().print(0,False)

        else:
            raise Exception("Syntax Error")

        sys.stdout.write()

        if t.getCdr().getCdr().isPair():
            t.getCdr().getCdr.print(n+2, True)
        
        else:
            raise Exception("Syntax Error")
        
        self.write()

        for i in range (0,n):
            sys.stdout.write(" ")

        self.write(" ")
        
        pass
