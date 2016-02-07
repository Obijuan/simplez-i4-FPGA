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


class TestCase(unittest.TestCase):

    # -- Lexer tests
    def test_lexer_01(self):
        self.assertEqual(lexer_test(lex1), lex1_res)


# -- Main program
if __name__ == '__main__':
    unittest.main()
