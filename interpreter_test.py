import unittest
from nodes import *
from interpreter import Interpreter
from values import Bool, Number

class TestInterpreter(unittest.TestCase):

  def test_empty(self):
    with self.assertRaises(Exception):
      value = Interpreter().visit(None)
    
  def test_number(self):
    value = Interpreter().visit(NumberNode(21.2))

    self.assertEqual(value,Number(21.2))

  def test_expression(self):
    # 5 - 3/3 * 10.0
    value = Interpreter().visit(
      SubtractNode(
        NumberNode(5),
        MultiplyNode(
          DivideNode(
            NumberNode(3),
            NumberNode(3)
          ),
          NumberNode(10)
        )
      )
    )

    self.assertEqual(value, Number(-5))

# Assignement 3
  def test_equal_comparison(self):
    # 5 == 5
    value = Interpreter().visit(
      EqualNode(
        NumberNode(5),
        NumberNode(5)
      )
    )

    self.assertEqual(value, Bool(True))


  def test_greater_comparison(self):
    # 6 > 2
    value = Interpreter().visit(
      GreaterNode(
       NumberNode(6),
       NumberNode(2)
      )
    )

    self.assertEqual(value, Bool(True))


  def test_greater_or_equal_comparison(self):
    # 6 >= 2
    value = Interpreter().visit(
      GreaterOrEqualNode(
       NumberNode(6),
       NumberNode(2)
      )
    )

    self.assertEqual(value, Bool(True))

  def test_less_comparison(self):
    # 2 < 6
    value = Interpreter().visit(
      LessNode(
       NumberNode(2),
       NumberNode(6)
      )
    )

    self.assertEqual(value, Bool(True))

  def test_less_or_equal_comparison(self):
    # 2 =< 6
    value = Interpreter().visit(
      LessOrEqualNode(
       NumberNode(2),
       NumberNode(6)
      )
    )

    self.assertEqual(value, Bool(True))



  def test_operations_and_comparison(self):
    # 7 * 10 > 7 + 10
    value = Interpreter().visit(
      GreaterNode(
        MultiplyNode(
          NumberNode(7),
          NumberNode(10)
        ),
        AddNode(
          NumberNode(7),
          NumberNode(10)
        )
      )
    )

    self.assertEqual(value, Bool(True))