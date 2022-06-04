import pytest

from models.user import User


@pytest.fixture
def user():
    return User("first_name", "last_name", 123456789, 18)
