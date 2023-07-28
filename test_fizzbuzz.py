import fizzbuzz

def test_fizz():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"
    assert fizzbuzz.fizzbuzz(6) == "Fizz"
    assert fizzbuzz.fizzbuzz(9) == "Fizz"
    assert fizzbuzz.fizzbuzz(12) == "Fizz"

def test_buzz():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"
    assert fizzbuzz.fizzbuzz(10) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz.fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz.fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz.fizzbuzz(45) == "FizzBuzz"

def test_regular_number():
    assert fizzbuzz.fizzbuzz(7) == 7
    assert fizzbuzz.fizzbuzz(14) == 14
