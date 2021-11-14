# Ident -- Parse tree node class for representing identifiers

from Tree import Node
from Print import Printer
from Tree import *

class Ident(Node):
    def __init__(self, n):
        self.name = n
    def eval(self, t, env):
        args = None
        a = Cons(Ident(t.getName()), Nil())
        args = self.eval_list(a, env)
        if not args.isNull():
            if args.getCar().isPair():
                if Environment.errorMessages.size() == 0:
                    Printer.printQuoted(args, 0, True)
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
            elif args.getCar().isNumber():
                return IntLit(args.getCar().getVal())
            elif args.getCar().isString():
                return StrLit(args.getCar().getStrVal())
            elif args.getCar().isBoolean():
                return BoolLit(args.getCar().getBoolean())
            else:
                print("placeholder")
                return Nil()
        else:
            return None
        return StrLit("")

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
                return Nil()
            list = Cons(arg1.eval(env), self.eval_list(rest, env))
            return list


    def print(self, n, p=False):
        Printer.printIdent(n, self.name)

    def getName(self):
        return self.name

    def isSymbol(self):
        return True

if __name__ == "__main__":
    id = Ident("foo")
    id.print(0)
