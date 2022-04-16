from tokenize import Token
from tokens import TokenType
from nodes import *


class Parser:
  def __init__(self, tokens):
    self.tokens = iter(tokens)
    self.advance()

  def advance(self):
    try:
      self.current_token = next(self.tokens)
    except StopIteration:
      self.current_token = None
  
  def parse(self):
    if self.current_token == None:
      return None

    result = self.bool_expr()

    if self.current_token != None:
      raise Exception("Unparsed tokens left")

    return result
    

  def bool_expr(self): # Assignement 3
    result = self.expr()

    while self.current_token != None and self.current_token.type in (TokenType.EQUAL, TokenType.GT, TokenType.GE, TokenType.LT, TokenType.LE):
      if self.current_token.type == TokenType.EQUAL:
        self.advance()
        result = EqualNode(result, self.expr())
      elif self.current_token.type == TokenType.GT:
        self.advance()
        result = GreaterNode(result, self.expr())
      elif self.current_token.type == TokenType.GE:
        self.advance()
        result = GreaterOrEqualNode(result, self.expr())
      elif self.current_token.type == TokenType.LT:
        self.advance()
        result = LessNode(result, self.expr())
      elif self.current_token.type == TokenType.LE:
        self.advance()
        result = LessOrEqualNode(result, self.expr())
    
    return result
  


  def expr(self):
    result = self.term()
    
    while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
      if self.current_token.type == TokenType.PLUS:
        self.advance()
        result = AddNode(result, self.term())
      elif self.current_token.type == TokenType.MINUS:
        self.advance()
        result = SubtractNode(result, self.term())

      
    return result

  def term(self):
    result = self.factor()
    

    while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
      if self.current_token.type == TokenType.MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.factor())
      elif self.current_token.type == TokenType.DIVIDE:
        self.advance()
        result = DivideNode(result, self.factor())

    return result
  
  def factor(self):
    token = self.current_token
    

    if self.current_token.type == TokenType.LPAREN:
      self.advance()
      result = self.expr()

      if self.current_token.type != TokenType.RPAREN:
        raise Exception("Invalid/Unbalanced parentheses")

      self.advance()
      return result


    if self.current_token.type == TokenType.NUMBER:
      self.advance()
      return NumberNode(token.value)


    raise Exception(f"Invalid factor _token: {self.current_token}")
  
