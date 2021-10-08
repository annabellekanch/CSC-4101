# Set -- Parse tree node strategy for printing the special form set!

from Special import Special

class Set(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self, cons):
        cons = None
        self.cons = cons
    
    def print(self, t, n, p):
        # TODO: Implement this function.
        if not p:
            print("(", end = '')

        if isinstance(self.cons.getCar(), Cons):
            self.cons.getCar().print(n, False)
        else:
            self.cons.getCar().print(n, False)
        if self.cons.getCdr() is not None:
            print(" ", end = '')
        if self.cons.getCdr() is not None:
            self.cons.getCdr().print(n, True)
        else:
            print(")")

    def printQuote(self, t, n, p):
        self.print(t, n, p)

