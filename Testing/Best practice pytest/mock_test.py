from simple_test import make_a_dict, some_calculation

"""
2. Mock everything we don’t want to test
- isolate functions from other functions
"""


def test_make_a_dict(mocker):
    """Test the make_a_dict function to ensure it returns the expected dictionary."""
    mocker.patch("simple_test.some_calculation", return_value=5, autospec=True)

    my_dict = make_a_dict(2, 3)
    expected_dict = {"a": 2, "b": 3, "result": 5}

    assert my_dict == expected_dict


def test_some_calculation():
    """Test the some_calculation function to ensure it returns the expected value."""
    value = some_calculation(2, 3)
    expected_value = 5
    assert expected_value == value
