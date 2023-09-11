def has_vowels(input_string):
    # Define a set of vowels
    vowels = set("AEIOUaeiou")
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is in the set of vowels
        if char in vowels:
            return True  # If a vowel is found, return True
    
    return False  # If no vowels are found, return False
