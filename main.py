from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
  text = input("algebra > ")
  if text == 'q':
    break

  lexer = Lexer(text)
  tokens = lexer.generate_tokens()

  # print("Tokens values: ", list(tokens))
  parser = Parser(tokens)
  tree = parser.parse()

  # print("Tree from parser: ", parser)
  
  if not tree: continue

  interpreter = Interpreter()
  value = interpreter.visit(tree)
  print(value)

  
