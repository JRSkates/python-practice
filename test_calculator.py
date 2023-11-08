from calculator import Calculator

def test_addition():
  calc = Calculator()
  result = calc.add(3, 5)
  assert result == 8