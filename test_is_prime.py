import is_prime

def test_less_than_2():
    assert is_prime.is_prime(1) == False
    assert is_prime.is_prime(0) == False

def test_is_false():
    assert is_prime.is_prime(4) == False
    assert is_prime.is_prime(9) == False

def test_is_true():
    assert is_prime.is_prime(17) == True