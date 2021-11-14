# Set -- Parse tree node strategy for printing the special form set!

from Tree import Nil
#from Tree import Unspecific
from Print import Printer
from Special import Special
from Tree import *

class Set(Special):
    def __init__(self):
        pass
    
    def print(self, t, n, p):
        Printer.printSet(t, n, p)

    def eval(self, t, env):
        id = None
        exp = None
        id = t.getCdr().getCar()
        exp = t.getCdr().getCdr().getCar()
        env.define(id, exp.eval(env))
        return StrLit("")
