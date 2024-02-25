import pytest

"""
1. Simple Test
Test one feature at a time
Small test
A single assertion
"""


def some_calculation(a, b):
    return a + b


def make_a_dict(a, b):
    if a < 0 or b < 0:
        raise ValueError("a and b must be positive")

    operation = some_calculation(a, b)

    return {"a": a, "b": b, "result": operation}


############# TESTING #############


# 🚨 Bad
def test_dict():
    assert make_a_dict(2, 3) == {"a": 2, "b": 3, "result": 5}

    with pytest.raises(ValueError):
        make_a_dict(-1, -1)


# ✅ Good
def test_make_a_dict():
    """Test the make_a_dict function to ensure it returns the expected dictionary."""
    my_dict = make_a_dict(2, 3)
    expected_dict = {"a": 2, "b": 3, "result": 5}
    assert my_dict == expected_dict


def test_make_a_dict_with_negative_values():
    """Test that make_a_dict raises a ValueError when negative values are passed."""
    with pytest.raises(ValueError):
        make_a_dict(-1, -1)
