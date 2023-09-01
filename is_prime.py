import math

def is_prime(num):
    # Step 1: Check for numbers less than 2
    if num < 2:
        return False

    # Step 2: Check for divisors from 2 to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    # Step 3: If no divisors found, it's prime
    return True

# Test the function
print(is_prime(2))  # True
print(is_prime(17))  # True
print(is_prime(4))  # False
print(is_prime(9))  # False
