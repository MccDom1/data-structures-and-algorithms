import pytest

# Assuming the sum function is defined in a module named 'my_module'
from my_module import sum

# Happy Path cases
def test_should_sum_two_integers():
    expected = 3
    actual = sum(1, 2)
    assert expected == actual, "Sum of 1 and 2 should be 3"

def test_should_sum_two_larger_integers():
    expected = 1333332
    actual = sum(1234567, 98765)
    assert expected == actual, "Sum of 1234567 and 98765 should be 1333332"

# Test with less obvious values (e.g., zero and negative numbers)
def test_should_sum_negative_numbers():
    expected = 3
    actual = sum(5, -2)
    assert expected == actual, "Sum of 5 and -2 should be 3"

# Test default argument values
def test_should_handle_single_argument():
    expected = 2
    actual = sum(2)
    assert expected == actual, "Sum of 2 and nothing should be 2 because the 2nd argument defaults to 0"

# Test acceptable argument types (floats)
def test_should_sum_floats():
    expected = 5.0
    actual = sum(3.5, 1.5)
    assert expected == actual, "Sum of 3.5 and 1.5 should be 5.0"

def test_should_sum_integer_and_float():
    expected = 5.5
    actual = sum(3.5, 2)
    assert expected == actual, "Sum of 3.5 and 2 should be 5.5"

# Test unsupported argument types
def test_should_accept_only_numbers():
    with pytest.raises(TypeError):
        sum('1', 3)
