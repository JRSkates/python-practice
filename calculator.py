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
    self.result = x / y
    return self.result

  def raise_to_power_of(self, x, y):
    self.result = x**y
    return self.result
  
  def remainder(self, x, y):
    self.result = x % y
    return self.result