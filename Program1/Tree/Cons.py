# Cons -- Parse tree node class for representing a Cons node

from Tree import Node
from Tree import *
from Tree.IntLit import IntLit
from Special import *

class Cons(Node):
    def __init__(self, a, d):
        self.car = a
        self.cdr = d
        self.parseList()

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.
    def parseList(self):
        # TODO: implement this function and any helper functions
        # you might need
        if isinstance(self.car, Ident):
            ident = self._car
            identName = ident.getIdentName()
            if identName == "quote" or identName == "'":
                self.form = Quote(self.cdr)
            elif identName == "lambda":
                self.form = Lambda()
            elif identName == "begin":
                self.form = Begin()
            elif identName == "if":
                self.form = If()
            elif identName == "let":
                self.form = Let()
            elif identName == "cond":
                self.form = Cond()
            elif identName == "define":
                self.form = Define()
            elif identName == "set!":
                self.form = Set(self)
            else:
                self.form = Regular(self)
        elif isinstance(self.car, IntLit):
            self.form = Regular(self)
        elif isinstance(self.car, StrLit):
            self.form = Regular(self)
        elif isinstance(self.car, BoolLit):
            self.form = Regular(self)
        elif isinstance(self.car, Nil):
            self.form = Regular(self)
        else:
            self.form = Regular(self)
        self.form = None

    def print(self, n):
        self.form.print(self, n, False)
    def print(self, n, p):
        self.form.print(self, n, p)
    def isPair(self):
        return self.car is not None and cdr is not None
    def getCar(self):
        return self.car
    def getCdr(self):
        return self.cdr
    def setCar(self, a):
        self.car = a
    def getCdr(self, d):
        self.car = d
    def printQuote(self, n, p):
        self.form.printQuote(self, n, p)
    

if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
