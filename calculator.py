import math

class Calculator:
  def __init__(self):
    self.result = 0
    self.memory = 0

  def add(self, x, y):
    self.result = x + y
    return self.result
  
  def subtract(self, x, y):
    self.result = x - y
    return self.result
  
  def multiply(self, x, y):
    self.result = x * y
    return self.result
  
  def divide(self, x, y):
    if y == 0:
      raise ValueError("Division by zero is not allowed")
    self.result = x / y
    return self.result
  
  def square_root(self, x):
    if x < 0:
      raise ValueError("Square root of a negative number is not allowed.")
    self.result = math.sqrt(x)
    return self.result

  def raise_to_power_of(self, x, y):
    self.result = x**y
    return self.result
  
  def remainder(self, x, y):
    self.result = x % y
    return self.result
  
  def store_to_memory(self):
    self.memory = self.result

  def recall_from_memory(self):
    self.result = self.memory
    return self.result


# More to add 