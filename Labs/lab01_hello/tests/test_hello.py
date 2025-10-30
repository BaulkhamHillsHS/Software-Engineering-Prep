from labs.lab01_hello.hello import greet

def test_greet_basic():
    assert greet("Caroline") == "Hello, Caroline!"

def test_greet_strip():
    assert greet("  Ada  ".strip()) == "Hello, Ada!"
