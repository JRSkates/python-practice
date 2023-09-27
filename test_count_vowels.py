import count_vowels

def test_count_vowels():

  assert count_vowels.count_vowels("Hello") == 2

  assert count_vowels.count_vowels("Hi") == 1

  assert count_vowels.count_vowels("WELCOME") == 3