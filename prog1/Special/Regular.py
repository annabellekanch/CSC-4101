# Regular -- Parse tree node strategy for printing regular lists

from Special import Special

class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.

        for i in range (0,n):
            self.write(" ")

        if not p:
            self.write("(")

        t.getCar().print(0)

        self.write(" ")

        t.getCdr().print(0,True)
        pass
