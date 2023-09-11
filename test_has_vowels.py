import has_vowels

def test_has_vowels():
    # Test case 1: String contains vowels
    assert has_vowels.has_vowels("Hello, World!") == True

    # Test case 2: String contains only consonants
    assert has_vowels.has_vowels("Hll, Wrld!") == False

    # Test case 3: String is empty
    assert has_vowels.has_vowels("") == False

    # Test case 4: String contains only vowels
    assert has_vowels.has_vowels("AEIOUaeiou") == True
