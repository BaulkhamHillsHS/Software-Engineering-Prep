from labs.lab03_loops.03B_even_odd_5.even_odd_5 import label_even_odd

def test_label():
    assert label_even_odd(10) == "even"
    assert label_even_odd(9) == "odd"
