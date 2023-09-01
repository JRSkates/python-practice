import say_hello

def test_hello():
    assert say_hello.say_hello("Jack") == 'Hello, Jack!'
    assert say_hello.say_hello("John") == 'Hello, John!'