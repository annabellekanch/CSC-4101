# Quote -- Parse tree node strategy for printing the special form quote

from Special import Special

class Quote(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self, list):
        list = None
        self.list = list

    def print(self, t, n, p):
        # TODO: Implement this function.
        print("'", end = '')
        (self.list.getCar()).printQuote(n, False)

    def printQuote(self, t, n, p):
        self.print(t, n, p)