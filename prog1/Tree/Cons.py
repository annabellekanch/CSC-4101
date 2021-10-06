# Cons -- Parse tree node class for representing a Cons node

from typing import Set
from Special.Begin import Begin
from Special.Cond import Cond
from Special.Define import Define
from Special.If import If
from Special.Lambda import Lambda
from Special.Let import Let
from Special.Quote import Quote
from Special.Regular import Regular
from Tree import Node
from Tree import Ident

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
        if self.car.isSymbol == True:
            name = self.car.getName()

            if name == "quote":
                return Quote()
            
            elif name == "lambda":
                return Lambda()

            elif name == "begin":
                return Begin()

            elif name == "if":
                return If()
            
            elif name == "cond":
                return Cond()
            
            elif name == "let":
                return Let()

            elif name == "set!":
                return set()

            elif name == "define":
                return Define()
            
            else:
                return Regular()

        else:
            return Regular()


    def print(self, n, p=False):
        self.form.print(self, n, p)
    
    def getCar(self):
        return super().getCar()

    def getCdr(self):
        return super().getCdr()


if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
