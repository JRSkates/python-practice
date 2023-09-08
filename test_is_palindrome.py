import is_palindrome

def test_is_palindrome():
    # Test case 1: Palindrome with no spaces and different letter cases
    assert is_palindrome.is_palindrome("Racecar") == True

    # Test case 2: Palindrome with spaces
    assert is_palindrome.is_palindrome("A man a plan a canal Panama") == True

    # Test case 3: Not a palindrome
    assert is_palindrome.is_palindrome("Hello, World!") == False

    # Test case 4: Empty string is a palindrome 
    assert is_palindrome.is_palindrome("") == True