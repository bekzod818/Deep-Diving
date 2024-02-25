from dataclasses import dataclass


@dataclass
class User:
    username: str


class InMemoryUserRepository:
    def __init__(self):
        self._users = []

    def add(self, user: User):
        self._users.append(user)

    def get_by_username(self, username: str):
        return next(user for user in self._users if user.username == username)


# 🚨 Bad
def test_add():
    user = User("john doe")
    repository = InMemoryUserRepository()
    repository.add(user)

    assert user in repository._users


def test_get_by_username():
    user = User("john doe")
    repository = InMemoryUserRepository()
    repository._users = [user]

    user_from_repository = repository.get_by_username("john doe")

    assert user == user_from_repository


# ✅ Good
def test_added_user_can_be_retrieved_by_username():
    user = User("john doe")
    repository = InMemoryUserRepository()
    repository.add(user)

    assert user == repository.get_by_username(user.username)
