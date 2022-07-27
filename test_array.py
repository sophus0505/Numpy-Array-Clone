from array import Array 
import pytest   

def test_init():
    wrong_shape = (-2,)
    long_shape = (1, 2, 3)
    short_shape = ()
    shape = (1, 3)
    correct_vals = [1, 2, 3]
    wrong_num_vals = [1, 2, 3, 4]
    wrong_type_vals = ["a", "b", "c"]

    with pytest.raises(ValueError):
        Array(wrong_shape, *correct_vals)
        Array(long_shape, *correct_vals)
        Array(short_shape, *correct_vals)

        Array(shape, *wrong_num_vals)
        Array(wrong_shape, *wrong_type_vals)
       
def test_print_nice_str():
    # Test if the Array class creates a nice str output for printing
    nice_str = "[1, 2, 3, 4, 5]"
    a = Array((5,), 1, 2, 3, 4, 5)
    assert nice_str == str(a), f"The __str__ method in Array doesn't work as intended!"

def test_add_element_wise():
    # Test if the Array class correctly adds to a 1d-array element-wise
    a = Array((5,), 1, 2, 3, 4, 5)
    b = Array((5,), 1, 1, 1, 1, 1)
    c = 1
    answ = [2, 3, 4, 5, 6]
    for i in range(0, 5):
        assert (a+b)[i] == answ[i] and (a+c)[i] == answ[i], "The __add__ method doesn't work as intended!"

def test_sub_element_wise():
    # Test if the Array class correctly subtracts from a 1d-array element-wise
    a = Array((5,), 1, 2, 3, 4, 5)
    b = Array((5,), 1, 1, 1, 1, 1)
    c = 1
    answ = [0, 1, 2, 3, 4]
    for i in range(0, 5):
        assert (a-b)[i] == answ[i] and (a-c)[i] == answ[i], "The __add__ method doesn't work as intended!"

def test_mult_element_wise():
    # Test if the Array class correctly multiplies a 1d-array with another 1d-array or number element-wise
    a = Array((5,), 1, 2, 3, 4, 5)
    b = Array((5,), 2, 2, 2, 2, 2)
    c = 2
    answ = [2, 4, 6, 8, 10]
    for i in range(0, 5):
        assert (a*b)[i] == answ[i] and (a*c)[i] == answ[i], "The __mul__ method doesn't work as intended!"

def test_eq():
    # Test if the __eq__ method in the Array class returns the correct results
    a = Array((5,), 1, 2, 3, 4, 5)
    b = Array((4,), 3, 4, 5, 6)
    c = Array((5,), 1, 2, 3, 4, 5)
    d = Array((4,), 3, 4, 5, 6)
    e = 5
    f = "frog"
    assert a == c, "The __eq__ method doesn't work as intended"
    assert c == a, "The __eq__ method doesn't work as intended"
    assert b == d, "The __eq__ method doesn't work as intended"

    assert not (a == d), "The __eq__ method doesn't work as intended"
    assert not (d == c), "The __eq__ method doesn't work as intended"
    assert not (b == c), "The __eq__ method doesn't work as intended"

    assert not (a == e), "The __eq__ method doesn't work as intended"
    assert not (b == f), "The __eq__ method doesn't work as intended"

def test_is_equal():
    # Test that the is_equal() method properly compares two Arrays or an array and a number correctly
    a = Array((5,), 1, 2, 3, 4, 5)
    c = 3
    d = Array((5,), 0, 0, 3, 0, 0)
    answ = [False, False, True, False, False]
    for i in range(0, 5):
        assert (a.is_equal(c))[i] == answ[i], "The is_equal method doesn't work as intended!"
        assert (a.is_equal(d))[i] == answ[i], "The is_equal method doesn't work as intended!"
    
def test_min_element():
    # Test if the min_element() method correctly returns the smallest element in the Array
    a = Array((5,), 1, 2, 3, -2, 5)
    answ = -2
    assert a.min_element() == answ, "The min_element() method doesn't work as intended!"


