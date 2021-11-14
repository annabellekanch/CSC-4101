# Define -- Parse tree node strategy for printing the special form define

from Tree import Ident
from Tree import Nil
from Tree import Cons
from Tree import *
#from Tree import Void
from Print import Printer
from Special import Special

class Define(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printDefine(t, n, p)
        
    def eval(self, t, env):
        id = None
        val = None

        id = t.getCdr().getCar()
        val = t.getCdr().getCdr().getCar()

        if id.isSymbol():
            env.define(id, val)
        else:
            func = Closure(Cons(t.getCdr().getCar().getCdr(), t.getCdr().getCdr()), env)
            env.define(id.getCar(), func)

        return StrLit("; no values returned")

    
