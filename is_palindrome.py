def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase
    cleaned_string = input_string.replace(" ", "").lower()

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("Racecar"))
# True
print(is_palindrome("A man a plan a canal Panama"))
# True
print(is_palindrome("Hello, World!"))
# False
print(is_palindrome(""))
# True