def count_vowels(word):
  word = word.lower()
  vowel_count = 0
  for char in word:
    if char in 'aeiou':
      vowel_count += 1
  
  return vowel_count