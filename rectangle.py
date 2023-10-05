class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def calculate_area(self):
    return self.length * self.width
  
  def is_larger(self, other):
    return self.calculate_area() > other.calculate_area()