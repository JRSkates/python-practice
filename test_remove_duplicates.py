from remove_duplicates import find_duplicates

def test_find_duplicates():
  assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]) == [2, 3]
  assert find_duplicates([3, 4, 5, 6, 7, 8, 9]) == []
  assert find_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
