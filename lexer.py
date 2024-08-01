from enum import Enum
from token import MINUS
import sys

class TokenType(Enum):
    NONE = -2
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # Keywords.
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    # Operators.
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211

class Token:
    def __init__(self, text: str, token_type: TokenType):
        self.text = text
        self.token_type = token_type

class Lexer:
    def __init__(self, source: str) -> None:
        # Appendding a 'newline' character to simplify parsing of the last line.
        self.source = source + '\n'
        self.current_char = ''
        self.current_pos = - 1
        self.get_next_char()

    def get_next_char(self):
        self.current_pos += 1
        if self.current_pos >= len(self.source):
            # End of file.
            self.current_char = '\0'
        else:
            self.current_char = self.source[self.current_pos]

    def get_lookahead_char(self):
        if self.current_pos + 1 >= len(self.source):
            # End of file.
            return '\0'
        return self.source[self.current_pos + 1]

    def abort(self, message: str):
        sys.exit(f"Lexing error: {message}")

    def consume_whitespace(self):
        while self.current_char == ' ' or self.current_char == '\t' or \
        self.current_char == '\r':
            self.get_next_char()

    def skip_comment(self):
        pass

    def get_token(self) -> Token:
        self.consume_whitespace()
        token = Token('', TokenType.NONE)

        if self.current_char == '+':
            token = Token(self.current_char, TokenType.PLUS)
        elif self.current_char == '-':
            token = Token(self.current_char, TokenType.MINUS)
        elif self.current_char == '*':
            token = Token(self.current_char, TokenType.ASTERISK)
        elif self.current_char == '/':
            token = Token(self.current_char, TokenType.SLASH)
        elif self.current_char == '\n':
            token = Token(self.current_char, TokenType.NEWLINE)
        elif self.current_char == '\0':
            token = Token(self.current_char, TokenType.EOF)
        else:
            # Unknown token.
            self.abort(message=f"Unknown token: '{self.current_char}'")

        self.get_next_char()
        return token
