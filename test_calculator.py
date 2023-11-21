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

def test_square_root():
  calc = Calculator()
  result = calc.square_root(25)
  assert result == 5

def test_square_root_of_negative_number():
  calc = Calculator()
  try:
    calc.square_root(-4)
  except ValueError as e:
    assert str(e) == "Square root of a negative number is not allowed."

def test_memory_operations():
  calc = Calculator()
  calc.add(10, 5)
  calc.store_to_memory()
  calc.subtract(8, 3)
  calc.recall_from_memory()
  assert calc.result == 15

def test_trigonometric_functions():
  calc = Calculator()
  calc.sin(30)
  assert calc.result == 0.5
  calc.cos(60)
  assert calc.result == 0.5
  calc.tan(45)
  assert calc.result == 1

def test_calculate_expression():
  calc = Calculator()
  result = calc.calculate_expression("(5 + 3) * 2 - 4 / 2")
  assert result == 14

def test_memory_clear():
  calc = Calculator()
  calc.add(10, 5)
  calc.store_to_memory()
  calc.clear_memory()
  calc.recall_from_memory()
  assert calc.result == 0

def test_factorial():
  calc = Calculator()
  calc.factorial(5)
  assert calc.result == 120