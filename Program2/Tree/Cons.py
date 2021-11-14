# Cons -- Parse tree node class for representing a Cons node

from Tree import Node
from Tree import Ident
from Special import *

class Cons(Node):
    util = None

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    def __init__(self, a, d):
        self.car = None
        self.cdr = None
        self.form = None
        self.strCar = None

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
        if not self.car.isSymbol():
            self.form = Regular(self)
        else:
            self.setStrCar( self.car)
            sym = self.getStrCar().getName()

            if sym.equalsIgnoreCase("quote"):
                self.form = Quote(self)
            elif sym.equalsIgnoreCase("lambda"):
                self.form = Lambda(self)
            elif sym.equalsIgnoreCase("begin"):
                self.form = Begin(self)
            elif sym.equalsIgnoreCase("if"):
                self.form = If(self)
            elif sym.equalsIgnoreCase("let"):
                self.form = Let(self)
            elif sym.equalsIgnoreCase("cond"):
                self.form = Cond(self)
            elif sym.equalsIgnoreCase("define"):
                self.form = Define(self)
            elif sym.equalsIgnoreCase("set!"):
                self.form = Set(self)
            else:
                self.form = Regular(self)

    def print(self, n, p=False):
        self.form.print(self, n, p)

    def getCar(self):
        return self.car

    def getCdr(self):
        return self.cdr
    
    def eval(self, env):
        return self.form.eval(self, env)

    def setCar(self, a):
        self.car = a
        self.parseList()

    def setCdr(self, d):
        self.cdr = d
        self.parseList()

    def isPair(self):
        return True

    def getStrCar(self):
        return self.strCar

    def setStrCar(self, strCar):
        self.strCar = strCar

if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
