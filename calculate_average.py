def calculate_average(numbers):
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty, cannot calculate the average")
    
    # Calulate the total sum of the numbers in the list
    total = sum(numbers)

    # Calculate the average
    average = total / len(numbers)

    return average

print(calculate_average([1, 2, 3, 4, 5]))
# 3.0
print(calculate_average([-1, -2, -3, -4, -5]))
# -3.0
print(calculate_average([0.5, 1.0, 1.5, 2.0]))
# 1.25
# print(calculate_average([]))
