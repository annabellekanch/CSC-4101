# Let -- Parse tree node strategy for printing the special form let

from Special import Special

class Let(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        for i in range(0,n):
            self.write(" ")

        self.write("(let ")

        if t.getCdr().getCar().isPair():
            t.getCdr().getCar().print(0,False)

        else:
            raise ValueError("Syntax Error")

        self.write()

        if t.getCdr().getCdr().isPair():
            t.getCdr().getCdr.print(n+2, True)
        
        else:
            raise ValueError ("Syntax Error")
        
        self.write()

        for i in range (0,n):
            self.write(" ")

        self.write(" ")
        
        pass
