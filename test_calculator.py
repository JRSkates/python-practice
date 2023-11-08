from calculator import Calculator

def test_addition():
  calc = Calculator()
  result = calc.add(3, 5)
  assert result == 8

def test_subtraction():
  calc = Calculator()
  result = calc.subtract(5, 3)
  assert result == 2

def test_multiply():
  calc = Calculator()
  result = calc.multiply(3, 5)
  assert result == 15