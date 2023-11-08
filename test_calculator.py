from calculator import Calculator

def test_addition():
  calc = Calculator()
  result = calc.add(3, 5)
  assert result == 8

def test_subtraction():
  calc = Calculator()
  result = calc.subtract(5, 3)
  assert result == 2