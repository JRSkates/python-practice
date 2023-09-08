import calculate_average

def test_calculate_average():
    # Test case 1: Test with a list of positive intergers
    numbers1 = [1, 2, 3, 4, 5]
    assert calculate_average.calculate_average(numbers1) == 3.0

    # Test case 2: Test with a list of negative integers
    numbers2 = [-1, -2, -3, -4, -5]
    assert calculate_average.calculate_average(numbers2) == -3.0
    
    # Test case 3: Test with a list of floating-point numbers
    numbers3 = [0.5, 1.0, 1.5, 2.0]
    assert calculate_average.calculate_average(numbers3) == 1.25
    
    # Test case 4: Test with a list containing a single number
    numbers4 = [42]
    assert calculate_average.calculate_average(numbers4) == 42.0

    # Test case 5: Test with an empty list, should raise a ValueError
    empty_list = []  # Create an empty list

    try:
        # Try to calculate the average of the empty list
        calculate_average.calculate_average(empty_list)
    
        # If the line above doesn't raise an exception, the test has failed.
        assert False, "Expected ValueError for empty input list."
    except ValueError as e:
        # The function correctly raised a ValueError, so we check if the error message matches our expectation.
        assert str(e) == "Input list is empty, cannot calculate the average"
