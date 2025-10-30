from labs.02B_add_three.add_three import add3

def test_add3():
    assert add3(1,2,3) == 6
    assert add3(0.5, 0.25, 0.25) == 1.0
