# BuiltIn -- the data structure for built-in functions

# Class BuiltIn is used for representing the value of built-in functions
# such as +.  Populate the initial environment with
# (name, BuiltIn(name)) pairs.

# The object-oriented style for implementing built-in functions would be
# to include the Python methods for implementing a Scheme built-in in the
# BuiltIn object.  This could be done by writing one subclass of class
# BuiltIn for each built-in function and implementing the method apply
# appropriately.  This requires a large number of classes, though.
# Another alternative is to program BuiltIn.apply() in a functional
# style by writing a large if-then-else chain that tests the name of
# the function symbol.

import sys
import os
import math
from Parse import *
from Tree import Node
from Tree import BoolLit
from Tree import IntLit
from Tree import StrLit
from Tree import Ident
from Tree import Nil
from Tree import Cons
from Tree import TreeBuilder
#from Tree import Unspecific

class BuiltIn(Node):
    env = None
    util = None

    @classmethod
    def setEnv(cls, e):
        cls.env = e

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    def __init__(self, s):
        self.symbol = s                 # the Ident for the built-in function

    def getSymbol(self):
        return self.symbol

    def isProcedure(self):
        return True

    def print(self, n, p=False):
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write("#{Built-In Procedure ")
        if self.symbol != None:
            self.symbol.print(-abs(n) - 1)
        sys.stdout.write('}')
        if n >= 0:
            sys.stdout.write('\n')
            sys.stdout.flush()

    # TODO: The method apply() should be defined in class Node
    # to report an error.  It should be overridden only in classes
    # BuiltIn and Closure.
    def apply(self, args):
        if args is None:
            return None
        symbolName = self.__symbol.getName()
        arg1 = args.getCar()
        if arg1 is None or arg1.isNull():
            arg1 = Nil()

        arg2 = args.getCdr()
        if arg2 is None or arg2.isNull():
            arg2 = Nil()
        else:
            arg2 = arg2.getCar()
        if symbolName == "b+":
            if arg1.isNumber() and arg2.isNumber():
                x = arg1.getVal()
                y = arg2.getVal()
                return IntLit(x + y)
            else:
                sys.err.println("Error: Bad argument for b+")
                return StrLit("")
        elif symbolName == "b-":
            if arg1.isNumber() and arg2.isNumber():
                x = arg1.getVal()
                y = arg2.getVal()
                return IntLit(x - y)
            else:
                sys.err.println("Error: Bad argument for b-")
                return StrLit("")
        elif symbolName == "b*":
            if arg1.isNumber() and arg2.isNumber():
                x = arg1.getVal()
                y = arg2.getVal()
                return IntLit(x * y)
            else:
                sys.err.println("Error: Bad argument for b*")
                return StrLit("")
        elif symbolName == "b/":
            if arg1.isNumber() and arg2.isNumber():
                x = arg1.getVal()
                y = arg2.getVal()
                return IntLit(math.trunc(x / float(y)))
            else:
                sys.err.println("Error: Bad argument for b/")
                return StrLit("")
        elif symbolName == "b=":
            if arg1.isNumber() and arg2.isNumber():
                x = arg1.getVal()
                y = arg2.getVal()
                return BoolLit(x == y)
            else:
                sys.err.println("Error: Bad argument for b=")
        elif symbolName == "b<":
            if arg1.isNumber() and arg2.isNumber():
                x = arg1.getVal()
                y = arg2.getVal()
                return BoolLit(x < y)
            else:
                sys.err.println("Error: Bad argument for b<")
        elif symbolName == "b>":
            if arg1.isNumber() and arg2.isNumber():
                x = arg1.getVal()
                y = arg2.getVal()
                return BoolLit(x > y)
            else:
                sys.err.println("Error: Bad argument for b>")
        elif symbolName == "car":
            if arg1.isNull():
                return arg1
            return arg1.getCar()
        elif symbolName == "cdr":
            if arg1.isNull():
                return arg1
            return arg1.getCdr()
        elif symbolName == "cons":
            return Cons(arg1, arg2)
        elif symbolName == "set-car!":
            arg1.setCar(arg2)
            return arg1
        elif symbolName == "set-cdr!":
            arg1.setCdr(arg2)
            return arg1
        elif symbolName == "symbol?":
            return BoolLit(arg1.isSymbol())
        elif symbolName == "number?":
            return BoolLit(arg1.isNumber())
        elif symbolName == "null?":
            return BoolLit(arg1.isNull())
        elif symbolName == "pair?":
            return BoolLit(arg1.isPair())
        elif symbolName == "eq?":
            if arg1.isBoolean() and arg2.isBoolean():
                return BoolLit(arg1.getBoolean() == arg2.getBoolean())
            elif arg1.isNumber() and arg2.isNumber():
                return BoolLit(arg1.getVal() == arg2.getVal())
            elif arg1.isString() and arg2.isString():
                return BoolLit(arg1.getStrVal() is arg2.getStrVal())
            elif arg1.isSymbol() and arg2.isSymbol():
                return BoolLit(arg1.getName() is arg2.getName())
            elif arg1.isNull() and arg2.isNull():
                return BoolLit(True)
            elif arg1.isPair() and arg2.isPair():
                frontArgs = Cons(arg1.getCar(), Cons(arg2.getCar(), Nil()))
                backArgs = Cons(arg1.getCdr(), Cons(arg2.getCdr(), Nil()))
                return BoolLit(self.apply(frontArgs).getBoolean() and self.apply(backArgs).getBoolean())
            return BoolLit(False)
        elif symbolName == "procedure?":
            return BoolLit(arg1.isProcedure())
        elif symbolName == "display":
            return arg1
        elif symbolName == "newline":
            return StrLit("", False)
        elif symbolName == "exit" or symbolName == "quit":
            sys.exit(0)
        elif symbolName == "write":
            arg1.print(0)
            return StrLit("")
        elif symbolName == "eval":
            return arg1
        elif symbolName == "apply":
            return arg1.apply(arg2)
        elif symbolName == "read":
            parser = None
            parser = Parser(Scanner(os.system(parser)))
            a = parser.parseExp()
            return a
        elif symbolName == "interaction-environment":
            interaction-environment.print(0)
        else:
            # use "write" by default
            arg1.print(0)
            return Nil()
        return StrLit(">")

    def eval(self, t, env):
        return Nil()

        
        ## The easiest way to implement BuiltIn.apply is as an
        ## if-then-else chain testing for the different names of
        ## the built-in functions.  E.g., here's how load could
        ## be implemented:
 
        # if name == "load":
        #     if not arg1.isString():
        #         self._error("wrong type of argument")
        #         return Nil.getInstance()
        #     filename = arg1.getStrVal()
        #     try:
        #         scanner = Scanner(open(filename))
        #         builder = TreeBuilder()
        #         parser = Parser(scanner, builder)

        #         root = parser.parseExp()
        #         while root != None:
        #             root.eval(BuiltIn.env)
        #             root = parser.parseExp()
        #     except IOError:
        #         self._error("could not find file " + filename)
        #     return Nil.getInstance()  # or Unspecific.getInstance()#