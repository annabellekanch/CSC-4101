# Regular -- Parse tree node strategy for printing regular lists

from Tree import Nil
from Print import Printer
from Tree import *
from Special import Special

class Regular(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printRegular(t, n, p)
        if Environment.errorMessages.size() == 0:
            Printer.printQuoted(t, n, True)
            print(")", end = '')
            print()
        else:
            newErr = ""
            for s in Environment.errorMessages:
                tmp = s
                if tmp != newErr:
                    print(s)
                else:
                    newErr = tmp

    def eval(self, t, env):
        first = None
        args = None

        first = t.getCar()
        args = self.eval_list(t.getCdr(), env)

        while first.isSymbol():
            first = env.lookup(first)

        if first is None or first.isNull():
            return None
        if first.isProcedure():
            return first.apply(args)
        else:
            return first.eval(env).apply(args)


    def eval_list(self, t, env):
        if t is None or t.isNull():
            list = Cons(Nil(), Nil())
            return list
        else:
            arg1 = None
            rest = None
            arg1 = t.getCar()
            rest = t.getCdr()

            if arg1.isSymbol():
                arg1 = env.lookup(arg1)
            if arg1 is None or arg1.isNull():
                return None
            list = Cons(arg1.eval(env), self.eval_list(rest, env))
            return list

