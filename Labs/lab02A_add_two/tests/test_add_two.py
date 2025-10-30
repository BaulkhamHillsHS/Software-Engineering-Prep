from labs.02A_add_two.add_two import add

def test_add():
    assert add(2, 3) == 5
    assert add(2.5, 0.5) == 3.0
