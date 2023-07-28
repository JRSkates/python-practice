def fizzbuzz(num):
  if num % 15 == 0:
    return "FizzBuzz"
  elif num % 5 == 0:
    return "Buzz"
  elif num % 3 == 0:
    return "Fizz"
  else:
    return num

print(fizzbuzz(15))
# FizzBuzz
print(fizzbuzz(10))
# Buzz
print(fizzbuzz(6))
# Fizz
print(fizzbuzz(13))
# 13