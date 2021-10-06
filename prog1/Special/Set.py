# Set -- Parse tree node strategy for printing the special form set!

import sys
from Special import Special

class Set(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass
    
    def print(self, t, n, p):
        # TODO: Implement this function.

        if p == False:
            sys.stdout.write("(")
        
        if t.getCar().isPair():
            t.getCar().print(0,False)
        
        else:
            t.getCar().print(0,True)
        
        sys.stdout.write(" ")

        if t.getCdr() == None:
            sys.stdout.write(")")
        
        else:
            t.getCdr().print(0,True)

        pass

