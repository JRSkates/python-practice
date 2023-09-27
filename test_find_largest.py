import find_largest

def test_find_largest():

  assert find_largest.find_largest([1, 2, 3, 4, 5]) == 5

  assert find_largest.find_largest([450, 123, 1123, 2345, 854]) == 2345

  assert find_largest.find_largest([]) == None