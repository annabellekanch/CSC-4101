# Begin -- Parse tree node strategy for printing the special form begin

from Special import Special

class Begin(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for r in range (0, n):
            self.write(' ')
        self.write("(begin")
        if(t.getCdr().isPair()):
            t.getCDR().print(n + 2, p)
        else:
            raise ValueError("Syntax Error")
        for r in range (0, n):
            self.write(" ")
        self.write(")")
        pass
