# If -- Parse tree node strategy for printing the special form if

from Tree import BoolLit
from Tree import Nil
#from Tree import Unspecific
from Print import Printer
from Special import Special
import sys

class If(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printIf(t, n, p)

    def eval(self, t, env):
        cond = None
        exp = None
        cond = t.getCdr().getCar()
        if cond.eval(env).getBoolean():
            exp = t.getCdr().getCdr().getCar()
            return exp.eval(env)
        elif not(t.getCdr().getCdr().getCdr()).isNull():
            exp = t.getCdr().getCdr().getCdr().getCar()
            return exp.eval(env)
        else:
            sys.err.println("No Else Expression")
            return Nil()
