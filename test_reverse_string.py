import reverse_string

def test_reverse_string():
    assert reverse_string.reverse_string("Hello") == "olleH"
    assert reverse_string.reverse_string("Python") == "nohtyP"
    assert reverse_string.reverse_string("") == ""
