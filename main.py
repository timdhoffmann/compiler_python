from lexer import Lexer, Token, TokenType

def main():
    source = "+- */"
    lexer = Lexer(source)

    token = lexer.get_token()

    while token.token_type != TokenType.EOF:
        print(token.token_type)
        token = lexer.get_token()

main()