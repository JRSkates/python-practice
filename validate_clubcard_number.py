def validate_clubcard_number(card_number):
  card_number = card_number[::-1]
  total_sum = 0
  for i, digit in enumerate(card_number):
    digit = int(digit)
    if i % 2 == 1:
      doubled_digit = digit * 2
      if doubled_digit > 9:
        doubled_digit -= 9
      total_sum += doubled_digit
    else:
      total_sum += digit

  is_valid = total_sum % 10 == 0
  return "True" if is_valid else "False"
