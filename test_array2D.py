from array import Array 

def test_valid_2darray_from_task():
    my_array = Array((3, 2), 8, 3, 4, 1, 6, 1)
    assert my_array[1][0] == 4

def test_add_2d():
    a = Array((2, 2), 1, 1, 2, 2)
    b = Array((2, 2), 3, 3, 3, 3)
    c = Array((2, 2), 4, 4, 5, 5)
    d = 3
    print(a + b)
    print(b.flat_array())

def test_sub_2D():
    a = Array((2, 2), 1, 1, 2, 2)
    b = Array((2, 2), 3, 3, 3, 3)
    c = Array((2, 2), -2, -2, -1, -1)
    assert (a - b) == c

def test_mul_2D():
    a = Array((2, 2), 1, 1, 2, 2)
    b = Array((2, 2), 3, 3, 3, 3)
    answ = Array((2, 2), 3, 3, 6, 6)
    assert a*b == answ

def test_eq_2D():
    a = Array((2, 2), 1, 1, 2, 2)
    b = Array((2, 2), 1, 1, 2, 2)
    assert a == b

# Test that the is_equal() method properly compares two Arrays or an array and a number correctly
def test_is_equal_2D():
    a = Array((3,2), 1, 2, 3, 4, 5, 6)
    c = 3
    d = Array((3,2), 0, 0, 3, 0, 0, 8)
    answ = [[False, False], [True, False], [False, False]]
    for i in range(0, 3):
        for j in range(0, 2):
            assert (a.is_equal(c))[i][j] == answ[i][j], "The is_equal method doesn't work as intended!"
            assert (a.is_equal(d))[i][j] == answ[i][j], "The is_equal method doesn't work as intended!"
