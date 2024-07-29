from lexer import Lexer

def main():
    source = "LET foobar = 123"
    lexer = Lexer(source)

    while lexer.get_lookahead_char() != '\0':
        print(lexer.current_char)
        lexer.get_next_char()

main()