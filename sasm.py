#!/usr/bin/python3
import ply.lex as lex


COMMENT, EOL, EOF, UNKNOW = ('COMMENT', 'EOL', 'EOF', 'UNKNOW')


class Lexer(object):

    tokens = (
       'COMMENT',
       'EOL',
       'EOF',
       'UNKNOW',
       'NUMDEC',
       'NUMHEX',
       'NUMOCT'
    )

    t_ignore = ' \t\r\f\v'

    # - Comments are ignored
    def t_COMMENT(self, t):
        r';[^\n]*[\n]'
        t.type = 'COMMENT'
        t.value = t.value[1:]
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.type = 'EOL'
        t.value = '1'
        return t

    def t_eof(self, t):
        t.type = 'EOF'
        t.value = ''
        return t

    # Error handling rule
    def t_error(self, t):
        t.type = 'UNKNOW'
        t.value = t.value[0]
        t.lexer.skip(1)
        return t

    def t_NUMDEC(self, t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    def t_NUMHEX(self, t):
        r"[hH]\'[0-9a-fA-F]+"
        t.value = int(t.value[2:], 16)
        return t

    def t_NUMOCT(self, t):
        r"[oO]\'[0-7]+"
        t.value = int(t.value[2:], 8)
        return t

    def __init__(self, data):
        """Create the lexer and give the data"""
        self.lexer = lex.lex(module=self)
        self.lexer.input(data)

        # -- Read the first token
        self.current_token = self.lexer.token()

    def token(self):
        """Read the next token"""
        self.current_token = self.lexer.token()

    def test(self):
        """Test the lexer"""
        print("-----------------Testing lex")

        while self.current_token.type != EOF:
            print(self.current_token)
            self.token()


# -- Main program
if __name__ == '__main__':

    data = '''
;-- Comentario
.A , .X [] LD ST ADD BR BZ SUB HALT EI DI WAIT
'''

    data2 = '''
;-- comentario 1
;-- comentario 2
.A  ;-- Comentario 3
;-- Comentario 4
2341 0 13443   1234
h'f h'23 h'aa h'faca
o'7 o'12
'''

    # Create the lexer with some data
    l = Lexer(data2)
    l.test()
