import pytest

# 3. DRY (Don’t repeat yourself)


# 🔥 parametrize
def add_numbers(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, expected_result",
    [(2, 3, 5), (-1, 3, 2), (3, -2, 1), (-4, 2, -2), (0, -1, -1)],
)
def test_add_numbers(a, b, expected_result):
    result = add_numbers(a, b)
    assert result == expected_result


# 🔥 fixture
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def is_adult(self):
        return self.age >= 18


# 🚨 Bad
def test_person_is_adult():
    person = Person("Emil")
    person.age = 19
    assert person.is_adult()


def test_person_is_not_adult():
    person = Person("Kemal")
    person.age = 15
    assert not person.is_adult()


# ✅ Good
@pytest.fixture
def person():
    person = Person("Emil")
    return person


def test_person_is_adult_2(person):
    person.age = 19
    assert person.is_adult()


def test_person_is_not_adult_2(person):
    person.age = 12
    assert not person.is_adult()
