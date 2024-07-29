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

    def abort(self):
        pass

    def consume_whitespace(self):
        pass

    def skip_comment(self):
        pass

    def get_token(self):
        pass

