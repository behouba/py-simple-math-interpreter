import unittest
from tokens import Token, TokenType
from lexer import Lexer

class TestLexer(unittest.TestCase):

  def test_empty(self):
    tokens = list(Lexer("").generate_tokens())
    self.assertEqual(tokens, [], 'Failed on empty string')

  def test_empty_spaces(self):
    tokens = list(Lexer(" \t\t\t\n\n\n   \n").generate_tokens())
    self.assertEqual(tokens, [], 'Failed on empty spaces string')

  def test_one_number(self):
    tokens = list(Lexer("5").generate_tokens())
    self.assertEqual(tokens, [Token(TokenType.NUMBER, 5)], 'Failed on one number string')

  def test_spaces_with_number(self):
    tokens = list(Lexer(" \t\t\t \n\n\n   \n5").generate_tokens())
    self.assertEqual(tokens, [Token(TokenType.NUMBER, 5)], 'Failed on  spaces string')

  def test_numbers(self):
    tokens = list(Lexer("123 123.456 123. .456 .").generate_tokens())
    self.assertEqual(tokens, [
      Token(TokenType.NUMBER, 123.000),
      Token(TokenType.NUMBER, 123.456),
      Token(TokenType.NUMBER, 123.000),
      Token(TokenType.NUMBER, 000.456),
      Token(TokenType.NUMBER, 000.000),
    ])

  def test_operators(self):
    tokens = list(Lexer("+-*/").generate_tokens())
    self.assertEqual(tokens, [
      Token(TokenType.PLUS),
      Token(TokenType.MINUS),
      Token(TokenType.MULTIPLY),
      Token(TokenType.DIVIDE),
    ])

  def test_parens(self):
    tokens = list(Lexer("()").generate_tokens())
    self.assertEqual(tokens, [
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN),
    ])

  def test_all(self):
    tokens = list(Lexer("27 + (43 / 36 - 48) * 51.3").generate_tokens())
    self.assertEqual(tokens, [
      Token(TokenType.NUMBER, 27.0),
      Token(TokenType.PLUS),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 43.0),
      Token(TokenType.DIVIDE),
      Token(TokenType.NUMBER, 36.0),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 48.0),
      Token(TokenType.RPAREN),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 51.3),
    ])


# Assignement 3
  def test_comparison_signs(self):
    tokens = list(Lexer("== > >= < =<").generate_tokens())
    self.assertEqual(tokens, [
      Token(TokenType.EQUAL),
      Token(TokenType.GT),
      Token(TokenType.GE),
      Token(TokenType.LT),
      Token(TokenType.LE),
    ])


  def test_comparison_operation(self):
    tokens = list(Lexer("(7 > 8) == (9 < 10) >= 5 =< 55.9").generate_tokens())
    self.assertEqual(tokens, [
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 7.0),
      Token(TokenType.GT),
      Token(TokenType.NUMBER, 8.0),
      Token(TokenType.RPAREN),
      Token(TokenType.EQUAL),
      Token(TokenType.LPAREN),  
      Token(TokenType.NUMBER, 9.0),
      Token(TokenType.LT),
      Token(TokenType.NUMBER, 10.0),
      Token(TokenType.RPAREN),
      Token(TokenType.GE),
      Token(TokenType.NUMBER, 5.0), 
      Token(TokenType.LE),
      Token(TokenType.NUMBER, 55.9), 
    ])