# Scanner -- The lexical analyzer for the Scheme printer and interpreter

import sys
import io
from Tokens import *
from Parse import *

class Scanner:
    def __init__(self, i):
        self.In = i
        self.buf = [0 for _ in range(1000)]
        self.ch_buf = None

    def read(self):
        if self.ch_buf == None:
            return self.In.read(1)
        else:
            ch = self.ch_buf
            self.ch_buf = None
            return ch
    
    def peek(self):
        if self.ch_buf == None:
            self.ch_buf = self.In.read(1)
            return self.ch_buf
        else:
            return self.ch_buf

    @staticmethod
    def isDigit(ch):
        return ch >= '0' and ch <= '9'
    def isWhiteSpace(self, ch):
        if(ch == ' '):
            return True
        return False

    def getNextToken(self):
        try:
            # It would be more efficient if we'd maintain our own
            # input buffer for a line and read characters out of that
            # buffer, but reading individual characters from the
            # input stream is easier.
            ch = self.read()

            # TODO: Skip white space and comments

            # Return None on EOF
            if(ch == -1):
                return None
            elif(self.isWhiteSpace(ch)):
                return self.getNextToken()
            # TODO: Skip white space and comments

            # Return None on EOF
            if ch == "":
                return None

            # Special characters
            elif ch == '\'':
                return Token(TokenType.QUOTE)
            elif ch == '(':
                return Token(TokenType.LPAREN)
            elif ch == ')':
                return Token(TokenType.RPAREN)
            elif ch == '.':
                #  We ignore the special identifier `...'.
                return Token(TokenType.DOT)

            # Boolean constants
            elif ch == '#':
                ch = self.read()

                if ch == 't':
                    return Token(TokenType.TRUE)
                elif ch == 'f':
                    return Token(TokenType.FALSE)
                elif ch == "":
                    sys.stderr.write("Unexpected EOF following #\n")
                    return None
                else:
                    sys.stderr.write("Illegal character '" +
                                     chr(ch) + "' following #\n")
                    return self.getNextToken()

            # String constants
            elif ch == '"':
                self.buf = []
                # TODO: scan a string into the buffer variable buf

                ch = self.read()
                for i in range(0, ch != '"'):
                    self.buf[i] = chr(ch)
                    ch = self.In.read()
                return StrToken("".join(self.buf))

            # Integer constants
            elif self.isDigit(ch):
                i = ord(ch) - ord('0')
                # TODO: scan the number and convert it to an integer
                pk = self.peek()
                while pk >= '0' and pk <= '9':
                    ch = self.read()
                    i = (i * 10) + int(ch)
                    pk = self.peek()
                # make sure that the character following the integer
                # is not removed from the input stream
                return IntToken(i)
    
            # Identifiers
            elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '+' or ch == '-' or ch == '.' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '@' or ch == '^'  or ch == '_':
                # or ch is some other vaid first character
                # for an identifier
                #self.buf = []
                # TODO: scan an identifier into the buffer variable buf
                #while((chr(self.In.peek() != '\"' or self.In.peek() == 8220 or self.In.peek() == 8221))):
                    #self.buf[count] = chr(self.In.read())
                #count+= 1
                
                self.buf = [10]
                count = 0
                #for i in range(0, self.peek() != ' ' or self.peek() != ')'):
                    #self.buf[i] == ch
                    #ch = self.read()
                
                while self.peek() != ' ' or self.peek() != ')':
                    self.buf[count] = ch
                    ch = self.read()
                    count += 1
    
                # make sure that the character following the identifier
                # is not removed from the input stream
                return IdentToken("".join(self.buf))

            # Illegal character
            else:
                sys.stderr.write("Illegal input character '" + ch + "'\n")
                return self.getNextToken()

        except IOError:
            sys.stderr.write("IOError: error reading input file\n")
            return None


if __name__ == "__main__":
    scanner = Scanner(sys.stdin)
    tok = scanner.getNextToken()
    tt = tok.getType()
    print(tt)
    if tt == TokenType.INT:
        print(tok.getIntVal())
