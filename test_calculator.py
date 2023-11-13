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

def test_divide():
  calc = Calculator()
  result = calc.divide(10, 2) 
  assert result == 5

def test_raise_to_power_of():
  calc = Calculator()
  result = calc.raise_to_power_of(2, 4)
  assert result == 16

def test_remainder():
  calc = Calculator()
  result = calc.remainder(2, 5)
  assert result == 2