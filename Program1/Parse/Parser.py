# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

from Tree import *
from Tokens import *
from Parse import *
from Special import *
import sys


class Parser(object):
    def __init__(self, s):
        self._scanner = s

    def parseExp(self):
        # TODO: write code for parsing an exp
        exp = None
        token = self._scanner.getNextToken()
        if token is None:
            exp = None
        elif token.getType() == TokenType.LPAREN:
            exp = self.parseRest(True)
        elif token.getType() == TokenType.FALSE:
            exp = BoolLit(False)
        elif token.getType() == TokenType.TRUE:
            exp = BoolLit(True)
        elif token.getType() == TokenType.QUOTE:
            exp = Cons(Ident("'"), Cons(self.parseExp(), None))
        elif token.getType() == TokenType.INT:
            exp = IntLit(token.getIntVal())
        elif token.getType() == TokenType.STRING:
            exp = StrLit(token.getStrVal())
        elif token.getType() == TokenType.IDENT:
            exp = Ident(token.getName())
        elif token.getType() == TokenType.RPAREN:
            print("Token Error: )")
            exp = self.parseExp()
        elif token.getType() == TokenType.DOT:
            print("Token Error: .")
            exp = self.parseExp()
        # parsing error
        else:
            print("Token Error Type: " + token.getType())
        return exp

    def parseRest(self, first):
        # TODO: write code for parsing a rest
        token = self._scanner.getNextToken()
        exp = None
        if token is None:
            exp = None
        elif token.getType() == TokenType.RPAREN:
            if first:
                return Nil()
            else:
                return None
        elif token.getType() == TokenType.DOT:
            # look ahead
            token = self._scanner.getNextToken()
            if token.getType() != TokenType.RPAREN:
                self._scanner.pushBackToStream(token)
                exp = Cons(self.parseExp(), None)
            else:
                print("Token Error: unexpected ')'")
                exp = self.parseExp()
        # exp
        else:
            self._scanner.pushBackToStream(token)
            exp = Cons(self.parseExp(), self.parseRest(False))
        return exp

    # TODO: Add any additional methods you might need

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
