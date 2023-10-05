from rectangle import Rectangle

def test_calculate_area():
  rectangle = Rectangle(5, 10)
  assert rectangle.calculate_area() == 50

def test_is_larger():
  rectangle1 = Rectangle(5, 10)
  rectangle2 = Rectangle(3, 8)
  assert rectangle1.is_larger(rectangle2) is True
  assert rectangle2.is_larger(rectangle1) is False
