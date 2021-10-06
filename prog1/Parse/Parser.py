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

import sys
from types import new_class
from Tokens import TokenType
import Tokens

class Parser:
    def __init__(self, s):
        self.scanner = s
    def parseNextExp(self):
        token = self.getNextToken()
        if(token == None):
            return None
        else:
            return self.parseExp(token)

    def parseExp(self):
        if(Token.getType() == TokenType.LPAREN):
            return self.parseRest()
        elif(Token.getType() == TokenType.FALSE):
            return self.BooleanLit(False)
        elif(Token.getType() == TokenType.TRUE):
            return self.BoolLit(True)
        elif(Token.getType() == TokenType.QUOTE):
            return self.Cons(self.Ident("quote"), self.Cons(self.parseNextExp(), self.Nil()))
        elif(Token.getType() == TokenType.INT):
            return self.IntLit(self.getIntVal())
        elif(Token.getType() == TokenType.String):
            return self.StringLit(self.getStrVal())
        elif(Token.getType() == TokenType.IDENT):
            return self.IDENT(self.getName())
        else:
            sys.stdout.write("Something broke parseExp")
        return None

    def parseRest(self):
        if(Token == None):
            return None
        elif(Token.getType() == TokenType.RPAREN):
            return self.Nil()
        elif(Token.getType() == TokenType.DOT):
            return self.Cons(self.parseNextExp(), self.parseRest())
        else:
            return self.Cons(self.parseExp(Token), self.parseRest())
        return None

    # TODO: Add any additional methods you might need

    def __error(self, msg):
        sys.stdout.write("Parse error: " + msg + "\n")
