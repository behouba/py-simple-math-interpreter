from nodes import *
from values import Number, Bool

class Interpreter:

  def visit(self, node):

    if not node: 
      raise Exception('No tree passed to interpreter')

    method_name = f'visit_{type(node).__name__}'
    method = getattr(self, method_name)
    return method(node)

  def visit_NumberNode(self, node):
    return Number(node.value)
  
  def visit_AddNode(self, node):
    return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

  def visit_SubtractNode(self, node):
    return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

  def visit_MultiplyNode(self, node):
    return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
  
  def visit_DivideNode(self, node):
    return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)

# Assignement 3
  def visit_EqualNode(self, node):
    return Bool(self.visit(node.node_a).value == self.visit(node.node_b).value)
  
  def visit_GreaterNode(self, node):
    return Bool(self.visit(node.node_a).value > self.visit(node.node_b).value)
  
  def visit_GreaterOrEqualNode(self, node):
    return Bool(self.visit(node.node_a).value >= self.visit(node.node_b).value)
  
  def visit_LessNode(self, node):
    return Bool(self.visit(node.node_a).value < self.visit(node.node_b).value)

  def visit_LessOrEqualNode(self, node):
    return Bool(self.visit(node.node_a).value <= self.visit(node.node_b).value)