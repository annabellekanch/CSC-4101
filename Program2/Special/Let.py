# Let -- Parse tree node strategy for printing the special form let

from Tree import Nil
from Tree import Environment
from Print import Printer
from Special import Special
from Tree import *

class Let(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printLet(t, n, p)

    def eval(self, t, env):
        args = None
        exp = None
        local = Environment(env)
        args = t.getCdr().getCar()
        exp = t.getCdr().getCdr().getCar()
        args = self.eval_body(args, local)
        return exp.eval(local)

    def eval_body(self, t, env):
        if t is None or t.isNull():
            list = Cons(Nil(), Nil())
            return list
        else:
            arg = None
            exp = None
            rest = None
            arg = t.getCar().getCar()
            exp = t.getCar().getCdr().getCar()
            rest = t.getCdr()

            if arg.isSymbol():
                env.define(arg, exp.eval(env))
                return self.eval_body(rest, env)
            elif arg.isPair():
                return arg.eval(env)
            elif arg is None or arg.isNull():
                return Nil()
        return None

