#!/usr/bin/python3
import unittest
from sasmi4 import Lexer


# -- Lexer tests
def lexer_test(data):
    l = Lexer(data)
    log = l.test()
    print(log)
    return log

lex1 = ("""
;-- comentario 1
;-- comentario 2
        ;-- Comentario 3
;-- Comentario 4
2341 0 13443   1234
h'f h'23 h'aa h'faca
o'7 o'12
b'1111 b'1010
""")

lex1_res = ("""[1] TOKEN (EOL, 1)
[2] TOKEN (COMMENT, -- comentario 1)
[2] TOKEN (EOL, 1)
[3] TOKEN (COMMENT, -- comentario 2)
[3] TOKEN (EOL, 1)
[4] TOKEN (COMMENT, -- Comentario 3)
[4] TOKEN (EOL, 1)
[5] TOKEN (COMMENT, -- Comentario 4)
[5] TOKEN (EOL, 1)
[6] TOKEN (NUM, 2341)
[6] TOKEN (NUM, 0)
[6] TOKEN (NUM, 13443)
[6] TOKEN (NUM, 1234)
[6] TOKEN (EOL, 1)
[7] TOKEN (NUM, 15)
[7] TOKEN (NUM, 35)
[7] TOKEN (NUM, 170)
[7] TOKEN (NUM, 64202)
[7] TOKEN (EOL, 1)
[8] TOKEN (NUM, 7)
[8] TOKEN (NUM, 10)
[8] TOKEN (EOL, 1)
[9] TOKEN (NUM, 15)
[9] TOKEN (NUM, 10)
[9] TOKEN (EOL, 1)
""")

lex2 = """
;-- Reserved words
ld LD sT ST ADD BR BZ SUB HALT EI DI WAIT EQU ORG DATA RES
"""

lex2_res = """[1] TOKEN (EOL, 1)
[2] TOKEN (COMMENT, -- Reserved words)
[2] TOKEN (EOL, 1)
[3] TOKEN (RESERVED, LD)
[3] TOKEN (RESERVED, LD)
[3] TOKEN (RESERVED, ST)
[3] TOKEN (RESERVED, ST)
[3] TOKEN (RESERVED, ADD)
[3] TOKEN (RESERVED, BR)
[3] TOKEN (RESERVED, BZ)
[3] TOKEN (RESERVED, SUB)
[3] TOKEN (RESERVED, HALT)
[3] TOKEN (RESERVED, EI)
[3] TOKEN (RESERVED, DI)
[3] TOKEN (RESERVED, WAIT)
[3] TOKEN (RESERVED, EQU)
[3] TOKEN (RESERVED, ORG)
[3] TOKEN (RESERVED, DATA)
[3] TOKEN (RESERVED, RES)
[3] TOKEN (EOL, 1)
"""

lex3 = """
;-- Immediate mode
#0 #1 #100 #255
#H'0 #h'aA #h'FF #h'cafe
#o'0 #o'7 #o'12 #o'1010
#B'0 #b'1 #b'1010 #b'1111 #b'0011
"""

lex3_res = """[1] TOKEN (EOL, 1)
[2] TOKEN (COMMENT, -- Immediate mode)
[2] TOKEN (EOL, 1)
[3] TOKEN (IMM, 0)
[3] TOKEN (IMM, 1)
[3] TOKEN (IMM, 100)
[3] TOKEN (IMM, 255)
[3] TOKEN (EOL, 1)
[4] TOKEN (IMM, 0)
[4] TOKEN (IMM, 170)
[4] TOKEN (IMM, 255)
[4] TOKEN (IMM, 51966)
[4] TOKEN (EOL, 1)
[5] TOKEN (IMM, 0)
[5] TOKEN (IMM, 7)
[5] TOKEN (IMM, 10)
[5] TOKEN (IMM, 520)
[5] TOKEN (EOL, 1)
[6] TOKEN (IMM, 0)
[6] TOKEN (IMM, 1)
[6] TOKEN (IMM, 10)
[6] TOKEN (IMM, 15)
[6] TOKEN (IMM, 3)
[6] TOKEN (EOL, 1)
"""

lex4 = """
;-- Other tokens
.A , .X []
hola addr label
"""

lex4_res = """[1] TOKEN (EOL, 1)
[2] TOKEN (COMMENT, -- Other tokens)
[2] TOKEN (EOL, 1)
[3] TOKEN (REG, A)
[3] TOKEN (COMMA, ,)
[3] TOKEN (REG, X)
[3] TOKEN (LBRACK, [)
[3] TOKEN (RBRACK, ])
[3] TOKEN (EOL, 1)
[4] TOKEN (LABEL, hola)
[4] TOKEN (LABEL, addr)
[4] TOKEN (LABEL, label)
[4] TOKEN (EOL, 1)
"""


class TestCase(unittest.TestCase):

    # -- Lexer tests
    def test_lexer_01(self):
        self.assertEqual(lexer_test(lex1), lex1_res)

    def test_lexer_02(self):
        self.assertEqual(lexer_test(lex2), lex2_res)

    def test_lexer_03(self):
        self.assertEqual(lexer_test(lex3), lex3_res)

    def test_lexer_04(self):
        self.assertEqual(lexer_test(lex4), lex4_res)


# -- Main program
if __name__ == '__main__':
    unittest.main()
