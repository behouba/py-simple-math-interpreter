from lib2to3.pgen2 import token
from tokenize import Number
import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):

  def test_empty(self):
    tokens = []
    tree = Parser(tokens).parse()
    self.assertEqual(tree, None)

  def test_numbers(self):
    tokens = [Token(TokenType.NUMBER, 51.2)]
    tree = Parser(tokens).parse()
    self.assertEqual(tree, NumberNode(51.2))

  def test_individual_operations(self):
    tokens = [
      Token(TokenType.NUMBER, 27),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 14),
    ]

    tree = Parser(tokens).parse()
    self.assertEqual(tree, AddNode(NumberNode(27), NumberNode(14)))

    tokens = [
      Token(TokenType.NUMBER, 27),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 14),
    ]

    tree = Parser(tokens).parse()
    self.assertEqual(tree, SubtractNode(NumberNode(27), NumberNode(14)))

    tokens = [
      Token(TokenType.NUMBER, 27),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 14),
    ]

    tree = Parser(tokens).parse()
    self.assertEqual(tree, MultiplyNode(NumberNode(27), NumberNode(14)))

    tokens = [
      Token(TokenType.NUMBER, 27),
      Token(TokenType.DIVIDE),
      Token(TokenType.NUMBER, 14),
    ]

    tree = Parser(tokens).parse()
    self.assertEqual(tree, DivideNode(NumberNode(27), NumberNode(14)))

  def test_full_expression(self):
    tokens = [
      # 27 + (43 / 36 - 48) * 51.2
      Token(TokenType.NUMBER, 27),
      Token(TokenType.PLUS),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 43),
      Token(TokenType.DIVIDE),
      Token(TokenType.NUMBER, 36),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 48),
      Token(TokenType.RPAREN),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 51),
    ]

    tree = Parser(tokens).parse()
    self.assertEqual(tree, AddNode(
      NumberNode(27),
      MultiplyNode(
        SubtractNode(
          DivideNode(
            NumberNode(43),
            NumberNode(36)
          ),
          NumberNode(48)
        ),
        NumberNode(51)
      )
    ))

# Assignement 3
  def test_equal_comparison(self):
    tokens = [
      # 10 == 10
      Token(TokenType.NUMBER, 10.0),
      Token(TokenType.EQUAL),
      Token(TokenType.NUMBER, 10.0),
    ]

    tree = Parser(tokens).parse()

    self.assertEqual(tree, EqualNode(
      NumberNode(10),
        NumberNode(10),
    ))

  def test_greater_comparison(self):

    tokens = [
      # 10 > 9
      Token(TokenType.NUMBER, 10.0),
      Token(TokenType.GT),
      Token(TokenType.NUMBER, 9.0),
    ]

    tree = Parser(tokens).parse()

    self.assertEqual(tree, GreaterNode(
      NumberNode(10),
      NumberNode(9)
    ))


  def test_greater_or_equal_comparison(self):

    tokens = [
      # 10 >= 9
      Token(TokenType.NUMBER, 10.0),
      Token(TokenType.GE),
      Token(TokenType.NUMBER, 9.0),
    ]

    tree = Parser(tokens).parse()

    self.assertEqual(tree, GreaterOrEqualNode(
      NumberNode(10),
      NumberNode(9)
    ))


  def test_less_comparison(self):

    tokens = tokens = [
      # 10 < 9
      Token(TokenType.NUMBER, 9.0),
      Token(TokenType.LT),
      Token(TokenType.NUMBER, 10.0),
    ]

    tree = Parser(tokens).parse()

    self.assertEqual(tree, LessNode(
      NumberNode(9),
      NumberNode(10)
    ))


  def test_less_or_equal_comparison(self):

    tokens = tokens = [
      # 10 =< 9
      Token(TokenType.NUMBER, 9.0),
      Token(TokenType.LE),
      Token(TokenType.NUMBER, 10.0),
    ]

    tree = Parser(tokens).parse()

    self.assertEqual(tree, LessOrEqualNode(
      NumberNode(9),
      NumberNode(10)
    ))