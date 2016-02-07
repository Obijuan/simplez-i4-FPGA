#!/usr/bin/python3
import ply.lex as lex

# -- TOKEN definition
(COMMENT, EOL, EOF, UNKNOWN, NUM, COMMA, REG, LBRACK, RBRACK, LABEL, RESERVED,
    IMM) = (
   'COMMENT', 'EOL', 'EOF', 'UNKNOW', 'NUM', 'COMMA', 'REG', 'LBRACK',
   'RBRACK', 'LABEL', 'RESERVED', 'IMM')

# -- Reserved words definition
LD, ST, ADD, BR, BZ, SUB, HALT, EI, DI, WAIT, EQU, DATA, RES, ORG = (
  'LD', 'ST', 'ADD', 'BR', 'BZ', 'SUB', 'HALT', 'EI', 'DI', 'WAIT',
  'EQU', 'DATA', 'RES', 'ORG')

reserved = [LD, ST, ADD, BR, BZ, SUB, HALT, EI, DI, WAIT,
            EQU, DATA, RES, ORG]


class Lexer(object):

    tokens = [
       COMMENT,
       EOL,
       EOF,
       UNKNOWN,
       NUM,
       COMMA,
       REG,
       LBRACK,
       RBRACK,
       LABEL,
       RESERVED,
       IMM
    ]

    t_ignore = ' \t\r\f\v'

    t_COMMA = r','
    t_LBRACK = r'\['
    t_RBRACK = r'\]'

    # - Comments are ignored
    def t_COMMENT(self, t):
        r';[^\n]+'
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

    # -- Immediate (in decimal)
    def t_IMMDEC(self, t):
        r'\#[0-9]+'
        t.value = int(t.value[1:])
        t.type = IMM
        return t

    def t_IMMHEX(self, t):
        r'\#[hH]\'[0-9a-fA-F]+'
        t.value = int(t.value[3:], 16)
        t.type = IMM
        return t

    def t_IMMOCT(self, t):
        r'\#[oO]\'[0-7]+'
        t.value = int(t.value[3:], 8)
        t.type = IMM
        return t

    def t_IMMBIN(self, t):
        r'\#[bB]\'[0-1]+'
        t.value = int(t.value[3:], 2)
        t.type = IMM
        return t

    def t_NUMDEC(self, t):
        r'[0-9]+'
        t.value = int(t.value)
        t.type = NUM
        return t

    def t_NUMHEX(self, t):
        r"[hH]\'[0-9a-fA-F]+"
        t.value = int(t.value[2:], 16)
        t.type = NUM
        return t

    def t_NUMOCT(self, t):
        r"[oO]\'[0-7]+"
        t.value = int(t.value[2:], 8)
        t.type = NUM
        return t

    def t_NUMBIN(self, t):
        r"[bB]\'[0-1]+"
        t.value = int(t.value[2:], 2)
        t.type = NUM
        return t

    def t_REG(self, t):
        r'\.[aAxX]'
        t.value = t.value[1:]
        return t

    def t_LABEL(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        if t.value.upper() in reserved:
            t.type = 'RESERVED'
            t.value = t.value.upper()
        else:
            t.type = LABEL
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
        string = ""
        while self.current_token.type != EOF:
            string += "[{}] TOKEN ({}, {})\n".format(self.current_token.lineno,
                                                     self.current_token.type,
                                                     self.current_token.value)
            self.token()
        return string


# -- Main program
if __name__ == '__main__':

    data = """
    ;-- Other tokens
    .A , .X []
    hola addr label
    """

    # Create the lexer with some data
    print("-----------------Testing lex")
    l = Lexer(data)
    msg = l.test()
    print(msg)
