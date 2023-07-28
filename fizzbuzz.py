def fizz_buzz(num):
  if num % 15 == 0:
    print("FizzBuzz")
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0:
    print("Fizz")
  else:
    print(num)

fizz_buzz(15)
# FizzBuzz
fizz_buzz(10)
# Buzz
fizz_buzz(6)
# Fizz
fizz_buzz(13)
# 13