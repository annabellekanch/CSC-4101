# Cond -- Parse tree node strategy for printing the special form cond

from Tree import BoolLit
from Tree import *
from Tree import Nil
#from Tree import Unspecific
from Print import Printer
from Special import Special

class Cond(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printCond(t, n, p)

    def eval(self, t, env):
        exp = None
        exp = t.getCdr()

        while (not(exp.getCar()).getCar().eval(env).getBoolean()) and ((not exp.isNull())):
            exp = exp.getCdr()

        if exp.isNull():
            return Nil()
        else:
            return (exp.getCar().getCdr().getCar().eval(env))
