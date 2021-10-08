# If -- Parse tree node strategy for printing the special form if

from Special import Special

class If(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        if not p:
            print("(", end = '')
        print("if ", end = '')
        if t.getCdr() is not None:
            t.getCdr().getCar().print(n+4, False)
            print()
            if t.getCdr().getCdr() is not None:
                self.Elements(t.getCdr().getCdr(), n+4, False)
        i = 0
        while i<n:
            print(" ", end = '')
            i += 1
        print(")", end = '')

    def Elements(self, t, n, isQuote):
        if isQuote:
            print(" ", end = '')
            t.getCar().printQuote(n, False)
        else:
            i = 0
            while i < n:
                print(" ", end = '')
                i += 1
            t.getCar().print(n)
            print()
        if t.getCdr() is not None:
            self.pElements(t.getCdr(), n, isQuote)

    def printQuote(self, t, n, p):
        if not p:
            print("(", end = '')
        print("if", end = '')
        if t.getCdr() is not None:
            self.Elements(t.getCdr(), 0, True)
        print(")", end = '')
