from validate_clubcard_number import validate_clubcard_number

def test_validate_clubcard_number():
  assert validate_clubcard_number("346088187380157") == "True"

  assert validate_clubcard_number("4916283358950480") == "True"

  assert validate_clubcard_number("5454411550469035") == "False"

  assert validate_clubcard_number("4518377421351212") == "False"